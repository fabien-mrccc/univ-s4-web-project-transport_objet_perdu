import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash

DBFILENAME = 'companies.sqlite'

# BEGIN Utility functions
#
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
#  
# END Utility functions 
 
def register_company_account(name, website, email, password, city, postal_code):

  email_in = db_fetch("SELECT 1 FROM CompagnieDeTransport WHERE email = ? LIMIT 1", (email,))
    
  if email_in is not None:
    raise ValueError("Email already exists.")
    
  db_run('INSERT INTO CompagnieDeTransport (Nom, SiteWeb, Email, MotDePasseHash) VALUES (?,?,?,?)',
         (name, website, email, generate_password_hash(password)))
  
  city_in = db_fetch("SELECT 1 FROM Ville WHERE Nom = ? AND CodePostal = ? LIMIT 1" , (city, postal_code))

  if city_in is None:
    db_run('INSERT INTO Ville (Nom, CodePostal) VALUES (?,?)', (city, postal_code))
  
  city_dict = db_fetch("SELECT ID FROM Ville WHERE Nom = ? AND CodePostal = ?;", (city, postal_code))

  db_run('INSERT INTO InformationsDeContact (CompagnieDeTransport_Email, Ville_ID) VALUES (?,?)', (email, city_dict['ID']))

def save_contact(company_id, city_id, phone, address, contact_page):
    db_run("""
           UPDATE InformationsDeContact SET Tel=?, Adresse=?, PageContact=? 
           WHERE CompagnieDeTransport_ID=? AND Ville_ID=?;""" 
           (phone, address, contact_page, company_id, city_id))
    
def delete_account(email):

  city_id = db_fetch("SELECT Ville_ID FROM InformationsDeContact WHERE CompagnieDeTransport_Email=?", (email,))

  db_run("DELETE FROM InformationsDeContact WHERE CompagnieDeTransport_Email=?", (email,))
  db_run("DELETE FROM CompagnieDeTransport WHERE Email=?", (email,))

  city_in = db_fetch("SELECT Ville_ID FROM InformationsDeContact WHERE Ville_ID = ?", (city_id['Ville_ID'],))

  if city_in is None:
    db_run("DELETE FROM Ville WHERE ID=?", (city_id['Ville_ID'],))

  return email

def authentification(email, password):
  password_hash = db_fetch("SELECT MotDePasseHash FROM CompagnieDeTransport WHERE Email = ?", (email,))

  if( password_hash is not None and check_password_hash(password_hash['MotDePasseHash'], password)):
    return email
  else:
    raise ValueError("Invalid email or password.")
