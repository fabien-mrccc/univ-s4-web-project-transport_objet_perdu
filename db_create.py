import sqlite3

DBFILENAME = 'companies.sqlite'

# Utility function
def db_run(query, args=(), db_name=DBFILENAME):
  with sqlite3.connect(db_name) as conn:
    cur = conn.execute(query, args)
    conn.commit()

def load(db_name=DBFILENAME):
  db_run('DROP TABLE IF EXISTS CompagnieDeTransport')
  db_run('DROP TABLE IF EXISTS Ville')
  db_run('DROP TABLE IF EXISTS InformationsDeContact')

  db_run('CREATE TABLE CompagnieDeTransport (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT, SiteWeb TEXT UNIQUE, Email TEXT UNIQUE, PasswordHash TEXT)')
  db_run('CREATE TABLE Ville (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nom TEXT, CodePostal TEXT)')
  db_run("""
          CREATE TABLE InformationsDeContact (
              CompagnieDeTransport_ID INTEGER,
              Ville_ID INTEGER,
              Tel TEXT,
              Adresse TEXT,
              PageContact TEXT,
              FOREIGN KEY (CompagnieDeTransport_ID) REFERENCES CompagnieDeTransport(ID) ON DELETE CASCADE,
              FOREIGN KEY (Ville_ID) REFERENCES Ville(ID),
              PRIMARY KEY (CompagnieDeTransport_ID, Ville_ID)
          )
         """)
  
  db_run("""
        INSERT INTO CompagnieDeTransport (Nom, SiteWeb, Email, PasswordHash) 
        VALUES ('Transports Dupont', 'https://www.transports-dupont.com', 'contact@transports-dupont.com', 'hash_du_mot_de_passe');
        """)
  
  db_run("""
        INSERT INTO Ville (Nom, CodePostal) 
        VALUES ('Paris', '75000');
        """)
  
  db_run("""
        INSERT INTO InformationsDeContact (CompagnieDeTransport_ID, Ville_ID, Tel, Adresse, PageContact) 
        VALUES (1, 1, '01 23 45 67 89', '123 rue de Paris, 75000 Paris', 'https://www.transports-dupont.com/contact');
        """)

# load recipe data
load()