// Fade out text when clicking over some other...
//
jQuery(document).ready(function() {
    $("#faq dt").click(function() {
	$(this).fadeOut("slow");
    });
});