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


def register_company_account(company_name, website, email, password, city, department):
    
    email_in = db_fetch("SELECT 1 FROM User WHERE Email = ? LIMIT 1", (email,))

    company_in = db_fetch("""SELECT 1 FROM TransportCompany tc 
                          JOIN ContactInformation ci ON tc.ID = ci.Company_ID 
                          JOIN City c ON ci.City_ID = c.ID 
                          JOIN User u ON tc.User_Email = u.Email 
                          WHERE tc.Name = ? AND c.Name = ? AND c.Department = ? LIMIT 1""", 
                          (company_name, city, department))
    
    if email_in is not None or company_in is not None:
        raise ValueError
    
    db_run('INSERT INTO User (Email, PasswordHash) VALUES (?, ?)', 
           (email, generate_password_hash(password)))

    db_run('INSERT INTO TransportCompany (Name, Website, User_Email) VALUES (?, ?, ?)', 
           (company_name, website, email))
  
    city_id = get_city_id(city, department)

    if city_id is None:
        db_run('INSERT INTO City (Name, Department) VALUES (?, ?)', (city, department))
  
    city_id = db_fetch("SELECT ID FROM City WHERE Name = ? AND Department = ?", (city, department))

    company = get_company(email)
    db_run("""INSERT INTO ContactInformation (Company_ID, City_ID) 
           VALUES (?, ?)""", (company['ID'], city_id['ID']))


def save_contact(email, city, department, phone, address, contact_page):
    
    city_id = get_city_id(city, department)
    company = get_company(email)

    db_run("""UPDATE ContactInformation SET Phone=?, Address=?, ContactPage=? 
           WHERE Company_ID=? AND City_ID=?;""",
           (phone, address, contact_page, company['ID'], city_id['ID']))

    
def delete_account(email):
  
    city = get_city(email)
    
    company = get_company(email)
    db_run("DELETE FROM ContactInformation WHERE Company_ID=?", (company['ID'],))
    db_run("DELETE FROM TransportCompany WHERE User_Email=?", (email,))
    db_run("DELETE FROM User WHERE Email=?", (email,))

    city_in = db_fetch("SELECT 1 FROM ContactInformation WHERE City_ID = ? LIMIT 1", (city['ID'],))
    if city_in is None:
      db_run("DELETE FROM City WHERE ID = ?", (city['ID'],))

    return email


def authentification(email, password):
    
    password_hash = db_fetch("SELECT PasswordHash FROM User WHERE Email = ?", (email,))

    if password_hash is not None and check_password_hash(password_hash['PasswordHash'], password):
        return email
    else:
        raise ValueError("Invalid email or password.")

  
def get_contact(company_name, city, department):
    
    city_id = get_city_id(city, department)
    print(city_id)
    contact_info = db_fetch("""SELECT tc.Name as Name, 
                            c.Department AS Department, 
                            c.Name AS City, 
                            ci.Phone AS Phone, 
                            ci.Address AS Address, 
                            ci.ContactPage AS ContactPage, 
                            tc.Website AS Website 
                            FROM ContactInformation ci 
                            JOIN TransportCompany tc ON ci.Company_ID = tc.ID 
                            JOIN City c ON ci.City_ID = c.ID 
                            WHERE tc.Name = ? AND City_ID = ?;""", (company_name, city_id['ID']))
    return contact_info


def get_company(email):

  return db_fetch("SELECT * FROM TransportCompany WHERE User_Email = ?;", (email,))


def get_city(email):
    
    company = get_company(email)
    if company:
        city_id = db_fetch("SELECT City_ID FROM ContactInformation WHERE Company_ID = ?", (company['ID'],))
        if city_id:
            return db_fetch("SELECT * FROM City WHERE ID = ?", (city_id['City_ID'],))
    return None
    

def get_city_id(name, department):

  return db_fetch("SELECT ID FROM City WHERE Name = ? AND Department = ?;", 
                       (name, department))


def get_contact_info(company_ID, city_ID):
  
  return db_fetch("SELECT * FROM ContactInformation WHERE Company_ID = ? AND City_ID = ?;", 
                  (company_ID, city_ID))

def get_recovery_sites():
   
   return db_fetch("""SELECT tc.Name AS Name, 
                   c.Department AS Department, 
                   c.Name AS City 
                   FROM ContactInformation ci 
                   JOIN TransportCompany tc ON ci.Company_ID = tc.ID 
                   JOIN City c ON ci.City_ID = c.ID ORDER BY Name;""", all=True)

