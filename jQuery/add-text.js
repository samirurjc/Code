// Add some text to li elements in #orderedlist element
//
jQuery(document).ready(function() {
    // do something here
    $("#orderedlist").find("li").each(function(i) {
     $(this).append( " This is li number " + i );
   });
});