from flask import Flask, session, request, redirect, render_template, url_for
import data_model as model

app = Flask(__name__)
app.secret_key = b'6dbb6b3863634aa6a72270de16df48e666f2564fddcc5fe3c27effe4393a7f4b'


########################
#      GET ROUTES      #
########################

@app.get('/')
def home(): 
    email_deleted = session.pop('email_deleted', '')
    return render_template('accueil.html', email=email_deleted)

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
    name = request.form["company_name"].strip()
    website = request.form["website"].strip()
    email = request.form["email"].strip()
    password = request.form["password"].strip()
    city = request.form["city"].strip()
    postal_code = request.form["postal_code"].strip()
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

@app.post('/delete-account')
def delete_account():
    email_deleted = model.delete_account(session['email'])
    session.clear()
    session['email_deleted'] = email_deleted
    return redirect('/')