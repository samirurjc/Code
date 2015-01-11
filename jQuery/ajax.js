// Get some text via Ajax, and write it to the p element #second

$(document).ready(function() {
    $.ajax({
	type: "GET",
	url: "text.txt",
	cache: false
    }).done(function( text ) {
	$("#second").html(text);
    });
});
