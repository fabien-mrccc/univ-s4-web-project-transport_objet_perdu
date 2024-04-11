import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
import math

DBFILENAME = 'companies.sqlite'

# Utility functions
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
  
def register_company_account(name, website, email, password, city, postal_code):
  db_run('INSERT INTO CompagnieDeTransport (Nom, SiteWeb, Email, MotDePasseHash) VALUES (?,?,?,?)',(name,website,email, generate_password_hash(password),))
  if db_run('SELECT Nom, CodePostal FROM Ville WHERE Nom = ? AND CodePostal = ?', (city, postal_code,)) == None:
    db_run('INSERT INTO Ville (Nom, CodePostal) VALUES (?,?)', (city, postal_code,))
  
  CompagnieDeTransport_ID = db_fetch("SELECT ID FROM CompagnieDeTransport WHERE SiteWeb = ? and Email = ?", (website, email,))
  print(CompagnieDeTransport_ID.keys)
  Ville_ID = db_fetch("SELECT ID FROM Ville WHERE Nom = ? AND CodePostal = ?;", (city, postal_code))
  print(Ville_ID.keys)
  db_run('INSERT INTO InformationsDeContact (CompagnieDeTransport_ID, Ville_ID) VALUES (?,?)', (CompagnieDeTransport_ID['CompagnieDeTransport_ID'], Ville_ID['Ville_ID'],))
