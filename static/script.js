"use strict";

document.addEventListener('DOMContentLoaded', main);

function main() {

    let leftHomeButton = document.getElementById('leftHomeButton');
    let rightHomeButton = document.getElementById('rightHomeButton');

    buttonEventListener(leftHomeButton, "/recuperer-objet-perdu");
    buttonEventListener(rightHomeButton, "/ma-compagnie-de-transport");
}

function buttonEventListener(button, page) {
    button.addEventListener('click', function() {
        redirect(page);
    });
}

function redirect(page) {
    window.location.href = page; 
}
