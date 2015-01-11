// Changing colors in a document
// To be used as file custom.js with StarterKit

jQuery(document).ready(function() {
    $("#orderedlist").addClass("red");
    $("#orderedlist > li").addClass("blue");
    $("#orderedlist > li:last").hover(function() {
	$(this).addClass("green");
    },function(){
	$(this).removeClass("green");
    });
});