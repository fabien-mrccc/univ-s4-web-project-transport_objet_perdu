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
  
def save_contact(company_id, city_id, phone, address, contact_page):
    db_run("""
           UPDATE InformationsDeContact SET Tel=?, Adresse=?, PageContact=? 
           WHERE CompagnieDeTransport_ID=? AND Ville_ID=?;""" 
           (phone, address, contact_page, company_id, city_id))
    
def delete_account(company_id):
  db_run("DELETE FROM CompagnieDeTransport WHERE ID=?", (company_id))