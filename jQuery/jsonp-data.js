// Get some JSONP text via Ajax, and write it to the HTML page,
// when clicking on "third"
//
$(document).ready(function() {
    $("#third").click(function(){
	jsonp = $.ajax({url: "jsonp-data.json?callback=?",
			dataType: "jsonp",
			jsonpCallback: "example1234"});
	jsonp.success( function(data) {
	    $('#header').after('<h1>' + data.title + '</h1>');
	    list = '<ul>'
	    for (var i = 0; i < data.entries.length; i++) {
		list = list + '<li>' + data.entries[i] + '</li>';
	    }
	    list = list + '</ul>';
	    $('#second').after(list);
	});
	jsonp.fail( function(data) {
	    console.log("Something went wrong...");
	    console.log(data);
	    console.log(data.error());
	});
    });
});
