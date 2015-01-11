// ==UserScript==
// @name           Write text on Google's logo
// @version        1.0
// @description    Write text ("Hola") on Google's logo in google.com webpage
// @include        *://www.google.tld/*
// @copyright      2014, Jesus M. Gonzalez-Barahona, GPLv3
// ==/UserScript==

function changer(id, newValue) {
    var element = document.getElementById(id);
    element.innerHTML = newValue;
}
changer('hplogo', '<H1>Hola</H1>');
