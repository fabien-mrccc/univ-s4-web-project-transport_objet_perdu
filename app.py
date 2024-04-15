from flask import Flask, session, request, redirect, render_template
import data_model as model
import requests

app = Flask(__name__)
app.secret_key = b'6dbb6b3863634aa6a72270de16df48e666f2564fddcc5fe3c27effe4393a7f4b'

api_url = "https://geo.api.gouv.fr/departements"
response = requests.get(api_url)

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

    recovery_sites = model.get_recovery_sites()
    return render_template('recuperer_objet_perdu.html', 
                           recovery_sites=recovery_sites, 
                           contact_info=None)


@app.get('/ma-compagnie-de-transport')
def my_transport_company_get():

    if 'email' in session:
        email = session['email']
        company = model.get_company(email)
        city = model.get_city(email)
        contact_info = model.get_contact_info(company['ID'], city['ID'])
        updated_contact_info = update_contact_info(contact_info, "")

        return render_template('ma_compagnie_de_transport.html', 
                               company_name = company['Name'], 
                               website = company['Website'], 
                               email=email, 
                               city = city['Name'], 
                               department = city['Department'], 
                               phone_number = updated_contact_info['Phone'], 
                               address = updated_contact_info['Address'], 
                               contact_page = updated_contact_info['ContactPage'])
    else:
        return redirect('/connexion-compagnie-transport')


@app.get('/connexion-compagnie-transport')
def login_get():

    return render_template('connexion_compagnie_transport.html', email_in=False)


@app.get('/inscription-compagnie-transport')
def register_get():

    return render_template('inscription_compagnie_transport.html', 
                           email_in=False, 
                           departments = departments)


#########################
#      POST ROUTES      #
#########################

@app.post('/inscription-compagnie-transport')
def register_post():

    name = request.form["company_name"].strip()
    website = request.form["website"].strip()
    email = request.form["email"].strip()
    password = request.form["password"].strip()
    city = request.form["city"].strip()
    department = request.form["departments"].strip()
    try:
        model.register_company_account(name, website, email, password, city, department)
    except ValueError:
        return render_template('inscription_compagnie_transport.html', 
                               email_in=True, 
                               departments = departments)
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

    recovery_sites = request.form['recovery-sites']
    parts = recovery_sites.split(' | ')
    company_name = parts[0]  

    city_department = parts[1].split(', ')  
    city = city_department[0]
    department = city_department[1]

    contact_info = model.get_contact(company_name, city, department)
    updated_contact_info = update_contact_info(contact_info, "Aucune information fournie")

    return render_template('recuperer_objet_perdu.html', 
                           recovery_sites=None, 
                           contact_info=updated_contact_info)


###############################
#      Utility functions      #
###############################

def update_contact_info(contact_info, error_message):

    if contact_info.get('Phone') is None or contact_info.get('Phone') == "":
        contact_info['Phone'] = error_message

    if contact_info.get('Address') is None or contact_info.get('Address') == "":
        contact_info['Address'] = error_message

    if contact_info.get('ContactPage') is None or contact_info.get('ContactPage') == "":
        contact_info['ContactPage'] = error_message

    return contact_info
