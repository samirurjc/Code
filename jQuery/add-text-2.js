// Add some text to li elements in #orderedlist element
// And some text when hovering over other elements...
//
jQuery(document).ready(function() {
    // do something here
    $("#orderedlist").find("li").each(function(i) {
     $(this).append( " This is li number " + i );
   });
    $("#orderedlist2 > li:last > ul > li").hover(function() {
	$(this).append(" Hello!");
    },function(){
	$(this).append(" Bye!");
    });
});