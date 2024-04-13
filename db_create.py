import sqlite3

DBFILENAME = 'companies.sqlite'

# Utility function
def db_run(query, args=(), db_name=DBFILENAME):
  with sqlite3.connect(db_name) as conn:
    cur = conn.execute(query, args)
    conn.commit()


def load(db_name=DBFILENAME):
  
  db_run('DROP TABLE IF EXISTS TransportCompany')
  db_run('DROP TABLE IF EXISTS City')
  db_run('DROP TABLE IF EXISTS ContactInformation')
  db_run('DROP TABLE IF EXISTS User')

  db_run("""
          CREATE TABLE User (
              Email TEXT PRIMARY KEY,
              PasswordHash TEXT
          );
         """)
  
  db_run("""
          CREATE TABLE TransportCompany (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              Name TEXT,
              Website TEXT,
              User_Email TEXT,
              FOREIGN KEY (User_Email) REFERENCES User(Email)
          );
         """)

  db_run("""
          CREATE TABLE City (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              Name TEXT,
              Department TEXT
          );
         """)

  db_run("""
          CREATE TABLE ContactInformation (
              Company_ID INTEGER,
              City_ID INTEGER,
              Phone TEXT,
              Address TEXT,
              ContactPage TEXT,
              PRIMARY KEY (Company_ID, City_ID),
              FOREIGN KEY (Company_ID) REFERENCES TransportCompany(ID),
              FOREIGN KEY (City_ID) REFERENCES City(ID)
          );
         """)

# load recipe data
load()