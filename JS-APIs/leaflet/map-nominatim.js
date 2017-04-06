// JavaScript for map-nominatim.html (Leaflet)

function addrSearch() {
    var inp = document.getElementById("addr");

    $.getJSON('http://nominatim.openstreetmap.org/search?format=json&limit=5&q=' + inp.value, function(data) {
	var items = [];

	$.each(data, function(key, val) {
	    items.push(
		"<li><a href='#' onclick='chooseAddr(" +
		    val.lat + ", " + val.lon + ", \"" + val.type + "\");return false;'>" + val.display_name +
		    '</a></li>'
	    );
	});
	$('#results').empty();
	if (items.length != 0) {
	    $('<p>', { html: "Search results:" }).appendTo('#results');
	    $('<ul/>', {
		'class': 'my-new-list',
		html: items.join('')
	    }).appendTo('#results');
	} else {
	    $('<p>', { html: "No results found" }).appendTo('#results');
	}
	$('<p>', { html: "<button id='close' type='button'>Close</button>" }).appendTo('#results');
	$("#close").click(removeResults);
    });
}

function removeResults() {
    $("#results").empty();
}

function chooseAddr(lat, lng, type) {
    var location = new L.LatLng(lat, lng);
    map.panTo(location);

    if (type == 'city' || type == 'administrative') {
	map.setZoom(10);
    } else {
	map.setZoom(13);
    }
}


$(document).ready(function() {

    $("div#search button").click(addrSearch);
    // Create a map in the "map" div
    map = L.map('map');
    L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
	attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012'
}).addTo(map);;

    // Show lat and long at cliked (event) point, with a popup
    var popup = L.popup();
    function showPopUp(e) {
	popup
            .setLatLng(e.latlng)
            .setContent("Coordinates: " + e.latlng.toString())
            .openOn(map);
    }
    // Subscribe to the "click" event
    map.on('click', showPopUp);

    // Show a circle around current location
    function onLocationFound(e) {
	var radius = e.accuracy / 2;
	L.marker(e.latlng).addTo(map)
            .bindPopup("You are within " + radius +
		       " meters from this point<br/>" +
		       "Coordinates: " + e.latlng.toString())
	    .openPopup();
	L.circle(e.latlng, radius).addTo(map);
    }
    // Subscribe to the "location found" event
    map.on('locationfound', onLocationFound);

    // Show alert if geolocation failed
    function onLocationError(e) {
	alert(e.message);
    }
    // Subscribe to the "location error" event
    map.on('locationerror', onLocationError);

    // Set the view to current location
    map.locate({setView: true, maxZoom: 16});
});
