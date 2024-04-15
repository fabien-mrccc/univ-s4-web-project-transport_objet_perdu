import sqlite3
from werkzeug.security import generate_password_hash
DBFILENAME = 'companies.sqlite'

# Utility function
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
  
  # RTM Company:
  email = 'anthony.randolph@rtm.fr'
  password = 'service'
  password_hash = generate_password_hash(password)
  company_name = 'RTM'
  website = 'https://www.rtm.fr/'
  city_name = 'Marseille'
  department = 'Bouches-du-Rhône'
  phone = '04 91 91 92 10'
  address = 'immeuble Astrolabe, 79 bd de dunkerque'
  contact_page = 'https://www.rtm.fr/objets-trouves-perdus-voles'
  db_run('INSERT INTO USER (Email, PasswordHash) VALUES (?,?)',(email, password_hash))
  db_run('INSERT INTO TransportCompany (Name, Website, User_Email) VALUES (?,?,?)',(company_name, website, email))
  db_run('INSERT INTO City (Name, Department) VALUES (?,?)',(city_name, department))
  company_ID = db_fetch('SELECT ID FROM TransportCompany WHERE User_Email = ?', (email,))
  city_ID = db_fetch('SELECT ID FROM City WHERE Name = ? AND Department = ?', (city_name, department))
  db_run('INSERT INTO ContactInformation (Company_ID, City_ID, Phone, Address, ContactPage) VALUES (?,?,?,?,?)',(company_ID['ID'], city_ID['ID'], phone, address, contact_page))

  # FlixBus Company:
  email = 'service@flixbus.fr'
  password = 'service'
  password_hash = generate_password_hash(password)
  company_name = 'FlixBus'
  website = 'https://www.flixbus.fr/'
  city_name = 'Lyon'
  department = 'Rhône'
  phone = '01 76 36 04 12'
  address = '2 Cr de Verdun Perrache, 69002 Lyon'
  contact_page = 'https://help.flixbus.com/s/article/PSSP-J-ai-laiss%C3%A9-quelque-chose-%C3%A0-bord-Que-doisje-faire?language=fr'
  db_run('INSERT INTO USER (Email, PasswordHash) VALUES (?,?)',(email, password_hash))
  db_run('INSERT INTO TransportCompany (Name, Website, User_Email) VALUES (?,?,?)',(company_name, website, email))
  db_run('INSERT INTO City (Name, Department) VALUES (?,?)',(city_name, department))
  company_ID = db_fetch('SELECT ID FROM TransportCompany WHERE User_Email = ?', (email,))
  city_ID = db_fetch('SELECT ID FROM City WHERE Name = ? AND Department = ?', (city_name, department))
  db_run('INSERT INTO ContactInformation (Company_ID, City_ID, Phone, Address, ContactPage) VALUES (?,?,?,?,?)',(company_ID['ID'], city_ID['ID'], phone, address, contact_page))

    # BlaBlaBus Company:
  email = 'service.client@blablabus.fr'
  password = 'service'
  password_hash = generate_password_hash(password)
  company_name = 'BlaBlaBus'
  website = 'https://www.blablacar.fr/'
  city_name = 'Paris'
  department = 'Paris'
  phone = '08 91 15 04 47'
  address = 'BlaBlaCar - 84 avenue de la République - 75011 Paris'
  contact_page = 'https://support.blablacar.com/hc/fr/articles/4416925807505-Comment-obtenir-de-l-aide-ou-contacter-BlaBlaCar'
  db_run('INSERT INTO USER (Email, PasswordHash) VALUES (?,?)',(email, password_hash))
  db_run('INSERT INTO TransportCompany (Name, Website, User_Email) VALUES (?,?,?)',(company_name, website, email))
  db_run('INSERT INTO City (Name, Department) VALUES (?,?)',(city_name, department))
  company_ID = db_fetch('SELECT ID FROM TransportCompany WHERE User_Email = ?', (email,))
  city_ID = db_fetch('SELECT ID FROM City WHERE Name = ? AND Department = ?', (city_name, department))
  db_run('INSERT INTO ContactInformation (Company_ID, City_ID, Phone, Address, ContactPage) VALUES (?,?,?,?,?)',(company_ID['ID'], city_ID['ID'], phone, address, contact_page))

    # eurolines Company:
  email = 'service-bagages@transdev-eurolines.com'
  password = 'service'
  password_hash = generate_password_hash(password)
  company_name = 'eurolines'
  website = 'https://eurolines.fr/'
  city_name = 'Villeneuve La Garenne'
  department = 'Hauts-de-Seine'
  phone = '08 92 89 12 00'
  address = 'Eurolines France - Service Après-Vente TSA 600001, 92399 Villeneuve La Garenne CEDEX'
  contact_page = 'https://eurolines.fr/contact/'
  db_run('INSERT INTO USER (Email, PasswordHash) VALUES (?,?)',(email, password_hash))
  db_run('INSERT INTO TransportCompany (Name, Website, User_Email) VALUES (?,?,?)',(company_name, website, email))
  db_run('INSERT INTO City (Name, Department) VALUES (?,?)',(city_name, department))
  company_ID = db_fetch('SELECT ID FROM TransportCompany WHERE User_Email = ?', (email,))
  city_ID = db_fetch('SELECT ID FROM City WHERE Name = ? AND Department = ?', (city_name, department))
  db_run('INSERT INTO ContactInformation (Company_ID, City_ID, Phone, Address, ContactPage) VALUES (?,?,?,?,?)',(company_ID['ID'], city_ID['ID'], phone, address, contact_page))

    # LeCar Company:
  email = 'service@lecar.fr'
  password = 'service'
  password_hash = generate_password_hash(password)
  company_name = 'LeCar'
  website = 'https://www.lecaraixmarseille.com/'
  city_name = 'Marseille'
  department = 'Bouches-du-Rhône'
  phone = '08 00 71 31 37'
  contact_page = 'https://www.lecaraixmarseille.com/contact'
  db_run('INSERT INTO USER (Email, PasswordHash) VALUES (?,?)',(email, password_hash))
  db_run('INSERT INTO TransportCompany (Name, Website, User_Email) VALUES (?,?,?)',(company_name, website, email))
  db_run('INSERT INTO City (Name, Department) VALUES (?,?)',(city_name, department))
  company_ID = db_fetch('SELECT ID FROM TransportCompany WHERE User_Email = ?', (email,))
  city_ID = db_fetch('SELECT ID FROM City WHERE Name = ? AND Department = ?', (city_name, department))
  db_run('INSERT INTO ContactInformation (Company_ID, City_ID, Phone, ContactPage) VALUES (?,?,?,?)',(company_ID['ID'], city_ID['ID'], phone, contact_page))

    # SNCF Company:
  email = 'service@sncf.com'
  password = 'service'
  password_hash = generate_password_hash(password)
  company_name = 'SNCF'
  website = 'https://www.sncf-connect.com/'
  city_name = 'Marseille'
  department = 'Bouches-du-Rhône'
  phone = '08 00 11 40 23'
  contact_page = 'https://www.sncf-connect.com/aide/contact'
  db_run('INSERT INTO USER (Email, PasswordHash) VALUES (?,?)',(email, password_hash))
  db_run('INSERT INTO TransportCompany (Name, Website, User_Email) VALUES (?,?,?)',(company_name, website, email))
  db_run('INSERT INTO City (Name, Department) VALUES (?,?)',(city_name, department))
  company_ID = db_fetch('SELECT ID FROM TransportCompany WHERE User_Email = ?', (email,))
  city_ID = db_fetch('SELECT ID FROM City WHERE Name = ? AND Department = ?', (city_name, department))
  db_run('INSERT INTO ContactInformation (Company_ID, City_ID, Phone, ContactPage) VALUES (?,?,?,?)',(company_ID['ID'], city_ID['ID'], phone, contact_page))

# load recipe data
load()