// Fade out text when clicking over some other...
// ...and fade it back when clicking over some other.
//
jQuery(document).ready(function() {
    $("#faq dt").click(function() {
	$(this).fadeOut("slow");
    });
    $("h3").click(function() {
	$("dt").fadeIn("slow");
    });
});