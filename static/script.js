"use strict";

document.addEventListener('DOMContentLoaded', main);

function main() {

    let leftHomeButton = document.getElementById('leftHomeButton');
    let rightHomeButton = document.getElementById('rightHomeButton');
    let disconnectButton = document.getElementById('disconnectButton');
    let registerButton = document.getElementById('registerButton');
    let loginButton = document.getElementById('loginButton');
    //let deleteAccoutButton = document.getElementById('deleteAccoutButton');

    buttonEventListener(leftHomeButton, "/recuperer-objet-perdu");
    buttonEventListener(rightHomeButton, "/ma-compagnie-de-transport");
    buttonEventListener(disconnectButton, "/deconnexion-compagnie-transport", true);
    buttonEventListener(registerButton, "/inscription-compagnie-transport");
    buttonEventListener(loginButton, "/connexion-compagnie-transport");
    //buttonEventListener(deleteAccoutButton, "/delete-account", true);
}

function buttonEventListener(button, page, isPost=false) {

    if (button != null) {

        button.addEventListener('click', function() {
            
            if (isPost) {
                postRedirect(page);
            }
            else {
                redirect(page);
            }
        });
    }
}

function postRedirect(page) {

    let form = document.createElement('form');
    document.body.appendChild(form);
    form.method = 'post';
    form.action = page;
    form.submit();
}

function redirect(page) {

    window.location.href = page; 
}


