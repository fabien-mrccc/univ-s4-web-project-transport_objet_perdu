from flask import Flask, session, request, redirect, render_template
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