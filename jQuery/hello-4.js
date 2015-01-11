// hello-4.js

$(document).ready(function() {
    // Code to run after document is loaded
    $("a").click(function(event) {
	alert("Hello world! (but now the link will not be followed)");
	event.preventDefault();
    });
});
