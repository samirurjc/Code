// Get some text via Ajax, and write it to the p element #second
// Now, get new text when clicking on "second"
//
$(document).ready(function() {
    $.ajax({
	type: "GET",
	url: "text.txt",
	cache: false
    }).done(function( text ) {
	$("#second").html(text);
    });
    $("#second").click(function(){
	$.ajax({
	    type: "GET",
	    url: "text2.txt",
	    cache: false
	}).done(function( text ) {
	    $("#third").html(text);
	});	
    });
});
