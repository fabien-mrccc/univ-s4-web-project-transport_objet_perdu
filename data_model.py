import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

DBFILENAME = 'companies.sqlite'

###########################
# BEGIN Utility functions #
###########################

def db_fetch(query, args=(), all=False, db_name=DBFILENAME):
  with sqlite3.connect(db_name) as conn:
    # to allow access to columns by name in res
    conn.row_factory = sqlite3.Row 
    cur = conn.execute(query, args)
    # convert to a python dictionary for convenience
    if all:
      res = cur.fetchall()
      if res:
        res = [dict(e) for e in res]
      else:
        res = []
    else:
      res = cur.fetchone()
      if res:
        res = dict(res)
  return res

def db_insert(query, args=(), db_name=DBFILENAME):
  with sqlite3.connect(db_name) as conn:
    cur = conn.execute(query, args)
    conn.commit()
    return cur.lastrowid

def db_run(query, args=(), db_name=DBFILENAME):
  with sqlite3.connect(db_name) as conn:
    cur = conn.execute(query, args)
    conn.commit()
    return cur

def db_update(query, args=(), db_name=DBFILENAME):
  with sqlite3.connect(db_name) as conn:
    cur = conn.execute(query, args)
    conn.commit()
    return cur.rowcount

#########################
# END Utility functions #
#########################


def register_company_account(name, website, email, password, city, department):
    
    email_in = db_fetch("SELECT 1 FROM User WHERE Email = ? LIMIT 1", (email,))
    
    if email_in is not None:
        raise ValueError("Email already exists.")
    
    db_run('INSERT INTO User (Email, PasswordHash) VALUES (?, ?)', 
           (email, generate_password_hash(password)))

    db_run('INSERT INTO TransportCompany (Name, Website, User_Email) VALUES (?, ?, ?)', 
           (name, website, email))
  
    city_id = get_city_id(city, department)

    if city_id is None:
        db_run('INSERT INTO City (Name, Department) VALUES (?, ?)', (city, department))
  
    city_id = db_fetch("SELECT ID FROM City WHERE Name = ? AND Department = ?", (city, department))

    db_run('INSERT INTO ContactInformation (Company_ID, City_ID) VALUES ((SELECT ID FROM TransportCompany WHERE User_Email = ?), ?)', (email, city_id['ID']))


def save_contact(email, city, department, phone, address, contact_page):
    
    city_id = get_city_id(city, department)
    company = get_company(email)

    db_run('UPDATE ContactInformation SET Phone=?, Address=?, ContactPage=? WHERE Company_ID=? AND City_ID=?;',
           (phone, address, contact_page, company['ID'], city_id['ID']))

    
def delete_account(email):
    
    company = get_company(email)
    db_run("DELETE FROM ContactInformation WHERE Company_ID=?", (company['ID'],))
    db_run("DELETE FROM TransportCompany WHERE User_Email=?", (email,))
    db_run("DELETE FROM User WHERE Email=?", (email,))

    return email


def authentification(email, password):
    
    password_hash = db_fetch("SELECT PasswordHash FROM User WHERE Email = ?", (email,))

    if password_hash is not None and check_password_hash(password_hash['PasswordHash'], password):
        return email
    else:
        raise ValueError("Invalid email or password.")

  
def get_contact(company_name, city, department):
    
    city_id = get_city_id(city, department)
    company_id = db_fetch("SELECT ID FROM TransportCompany WHERE Name = ?", (company_name,))
    informations = db_fetch("SELECT Phone, Address, ContactPage FROM ContactInformation WHERE Company_ID = ? AND City_ID = ? ", (company_id['ID'], city_id['ID']))
    return informations


def get_cities():

  return db_fetch("SELECT * FROM City;", all=True)

def get_companies_names():

  companies = db_fetch("SELECT Name FROM TransportCompany;", all=True)
  return [company['Name'] for company in companies]


def get_company(email):

  return db_fetch("SELECT * FROM TransportCompany WHERE User_Email = ?;", (email,))


def get_city(email):
    
    city_ID = db_fetch("SELECT ci.City_ID AS ID FROM ContactInformation ci JOIN TransportCompany tc ON ci.Company_ID = tc.ID JOIN User u ON tc.User_Email = u.Email WHERE u.Email = ?;", (email,))
    return db_fetch("SELECT * FROM City WHERE ID = ?;", (city_ID['ID'],))
    

def get_city_id(name, department):

  return db_fetch("SELECT ID FROM City WHERE Name = ? AND Department = ?;", 
                       (name, department))


def get_contact_info(company_ID, city_ID):
  
  return db_fetch("SELECT * FROM ContactInformation WHERE Company_ID = ? AND City_ID = ?;", (company_ID, city_ID))

