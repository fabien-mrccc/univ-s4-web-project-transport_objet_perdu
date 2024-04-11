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
def login():
    return render_template('connexion_compagnie_transport.html')

@app.get('/inscription-compagnie-transport')
def register_get():
    return render_template('inscription_compagnie_transport.html')


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
    model.register_company_account(name, website, email, password, city, postal_code)
    return redirect(url_for('connexion-compagnie-transport'))
