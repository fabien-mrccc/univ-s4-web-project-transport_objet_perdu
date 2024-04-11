from flask import Flask, session, request, redirect, render_template, url_for
import data_model as model

app = Flask(__name__)


########################
#      GET ROUTES      #
########################

@app.get('/')
def home(): 
    return render_template('accueil.html')

@app.get('/recuperer-objet-perdu')
def recover_lost_object():
    return render_template('recuperer_objet_perdu.html')

@app.get('/ma-compagnie-de-transport')
def my_transport_company():
    return render_template('ma_compagnie_de_transport.html')

@app.get('/connexion-compagnie-transport')
def login_get():
    return render_template('connexion_compagnie_transport.html')

@app.get('/inscription-compagnie-transport')
def register_get():
    return render_template('inscription_compagnie_transport.html', email_in=False)

########################
#     POST ROUTES      #
########################

@app.post('/inscription-compagnie-transport')
def register_post():
    name = request.form["company_name"]
    website = request.form["website"]
    email = request.form["email"]
    password = request.form["password"]
    city = request.form["city"]
    postal_code = request.form["postal_code"]
    try:
        model.register_company_account(name, website, email, password, city, postal_code)
    except ValueError as err:
        return render_template('inscription_compagnie_transport.html', email_in=True)
    return redirect('/connexion-compagnie-transport')

"""
@app.post('/delete-account')
def delete_account():
"""
@app.post('/connexion-compagnie-transport')
def login_post():
    email = request.form['email']
    try:
        model.authentification(request.form['email'], request.form['password'])
    except ValueError as err:
        return render_template('connexion_compagnie_transport.html')
    session['email'] = email
    return redirect('/ma-compagnie-de-transport')



