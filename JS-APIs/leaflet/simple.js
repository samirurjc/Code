// JavaScript for simple.html (Leaflet)

$(document).ready(function() {
    // create a map in the "map" div, set the view to a given place and zoom
    var map = L.map('map').setView([40.2838, -3.8215], 15);
    // add an OpenStreetMap tile layer
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // add a marker in the given location, attach some popup content to it and open the popup
    L.marker([40.2838, -3.8215]).addTo(map)
	.bindPopup('<a href="http://www.etsit.urjc.es">ETSIT</a> (<a href="http://www.urjc.es">URJC</a>)')
	.openPopup();
});