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
    $("#fourth").click(function(){
	var request = $.ajax({
	    type: "GET",
	    url: "text3.txt",
	    cache: false
	});
	request.done(function( text ) {
	    $("#fiveth").html(text);
	});	
	request.fail(function( text ) {
	    $("#fiveth").html("Error getting text");
	});	
    });

});
