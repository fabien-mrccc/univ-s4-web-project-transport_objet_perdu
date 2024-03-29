from flask import Flask, session, request, redirect, render_template
import data_model as model

app = Flask(__name__)


########################
#      GET ROUTES      #
########################

@app.route('/')
def home(): 
    render_template('accueil.html')
