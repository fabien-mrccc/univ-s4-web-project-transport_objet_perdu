from flask import Flask, session, request, redirect, render_template, url_for
import data_model as model
import requests

app = Flask(__name__)
app.secret_key = b'6dbb6b3863634aa6a72270de16df48e666f2564fddcc5fe3c27effe4393a7f4b'

apiUrl = "https://geo.api.gouv.fr/departements"
response = requests.get(apiUrl)

departments = response.json()

########################
#      GET ROUTES      #
########################

@app.get('/')
def home(): 
    email_deleted = session.pop('email_deleted', '')
    return render_template('accueil.html', email=email_deleted)

@app.get('/recuperer-objet-perdu')
def recover_lost_object_get():
    cities = model.db_fetch("SELECT Nom FROM Ville;", all=True)

    cities_names = [city['Nom'] for city in cities]
    
    companies = model.db_fetch("SELECT Nom FROM CompagnieDeTransport;", all=True)
    companies_names = [company['Nom'] for company in companies]

    return render_template('recuperer_objet_perdu.html', cities=cities_names, departments=departments, companies_names=companies_names, is_submitted=False, informations=None)

@app.get('/ma-compagnie-de-transport')
def my_transport_company_get():
    if 'email' in session:
        email = session['email']
        company_name = model.db_fetch("SELECT Nom FROM CompagnieDeTransport WHERE Email = ?;", (email,))
        website = model.db_fetch("SELECT SiteWeb FROM CompagnieDeTransport WHERE Email = ?;", (email,))

        city_ID = model.db_fetch("SELECT Ville_ID FROM InformationsDeContact WHERE CompagnieDeTransport_Email = ?;", (email,))
        city = model.db_fetch("SELECT Nom FROM Ville WHERE ID = ?;", (city_ID['Ville_ID'],))
        department = model.db_fetch("SELECT Departement FROM Ville WHERE ID = ?;", (city_ID['Ville_ID'],))

        phone_number = model.db_fetch("SELECT Tel FROM InformationsDeContact WHERE CompagnieDeTransport_Email = ? AND Ville_ID = ?;", (email,city_ID['Ville_ID']))
        address = model.db_fetch("SELECT Adresse FROM InformationsDeContact WHERE CompagnieDeTransport_Email = ? AND Ville_ID = ?;", (email,city_ID['Ville_ID']))
        contact_page = model.db_fetch("SELECT PageContact FROM InformationsDeContact WHERE CompagnieDeTransport_Email = ? AND Ville_ID = ?;", (email,city_ID['Ville_ID']))

        return render_template('ma_compagnie_de_transport.html', company_name = company_name['Nom'], website = website['SiteWeb'], email=email, city = city['Nom'], department = department['Departement'], phone_number = phone_number['Tel'], address = address['Adresse'], contact_page = contact_page['PageContact'])
    else:
        return redirect('/connexion-compagnie-transport')

@app.get('/connexion-compagnie-transport')
def login_get():
    return render_template('connexion_compagnie_transport.html', email_in=False)

@app.get('/inscription-compagnie-transport')
def register_get():

    return render_template('inscription_compagnie_transport.html', email_in=False, departments = departments)


########################
#     POST ROUTES      #
########################

@app.post('/inscription-compagnie-transport')
def register_post():
    name = request.form["company_name"].strip()
    website = request.form["website"].strip()
    email = request.form["email"].strip()
    password = request.form["password"].strip()
    city = request.form["city"].strip()
    department = request.form["departements"].strip()
    try:
        model.register_company_account(name, website, email, password, city, department)
    except ValueError:
        return render_template('inscription_compagnie_transport.html', email_in=True, departments = departments)
    return redirect('/connexion-compagnie-transport')

@app.post('/connexion-compagnie-transport')
def login_post():
    email = request.form['email']
    password = request.form['password']
    try:
        model.authentification(email, password)
    except ValueError:
        print("catch")
        return render_template('connexion_compagnie_transport.html', email_in=True)
    session['email'] = email
    return redirect('/ma-compagnie-de-transport')

@app.post('/deconnexion-compagnie-transport')
def logout():
    session.clear()
    return redirect('/')

@app.post('/delete-account')
def delete_account():
    email_deleted = model.delete_account(session['email'])
    session.clear()
    session['email_deleted'] = email_deleted
    return redirect('/')

@app.post('/ma-compagnie-de-transport')
def my_transport_company_post():
    email = request.form['email']
    city = request.form['city']
    department = request.form['department']
    phone = request.form['phone_number']
    address = request.form['address']
    contact_page = request.form['contact_page']

    model.save_contact(email, city, department, phone, address, contact_page)
    return redirect('/ma-compagnie-de-transport')

@app.post('/recuperer-objet-perdu')
def recover_lost_object_post():
    company_name = request.form['company_name']
    city = request.form['city']
    department = request.form['department']
    informations = model.get_contact(company_name=company_name, city = city, department= department)
    return render_template('/recuperer-objet-perdu', is_submitted=True, informations=informations)
