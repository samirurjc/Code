// Fade out text when clicking over some other...
// ...and write the faded text somewhere else
//
jQuery(document).ready(function() {
    $("#faq dt").click(function() {
	$(this).fadeOut("slow", function(){
	    $("h3").html("Text faded: " + $(this).html());
	});
    });
});