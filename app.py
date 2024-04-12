from flask import Flask, session, request, redirect, render_template, url_for
import data_model as model

app = Flask(__name__)
app.secret_key = b'6dbb6b3863634aa6a72270de16df48e666f2564fddcc5fe3c27effe4393a7f4b'


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
    if 'email' in session:
        return render_template('ma_compagnie_de_transport.html')
    else:
        return redirect('/connexion-compagnie-transport')

@app.get('/connexion-compagnie-transport')
def login_get():
    return render_template('connexion_compagnie_transport.html', email_in=False)

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
    except ValueError:
        return render_template('inscription_compagnie_transport.html', email_in=True)
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
def logout_post():
    session.clear()
    return redirect('/')

"""
@app.post('/delete-account')
def delete_account():
"""

