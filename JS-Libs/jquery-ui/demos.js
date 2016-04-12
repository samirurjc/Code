// JavaScript for demos.html

$(function() {
    $( "#menu" ).menu();
    $( "#draggable" ).draggable({ revert: true, opacity: 0.35, stack: "#droppable"});
    $( "#draggable2" ).draggable({ stack: "#droppable"});
    $( "#droppable" ).droppable({
	drop: function( event, ui ) {
	    $( this )
		.addClass( "ui-state-highlight" )
		.find( "p" )
		.html( "Dropped!" );
	},
	out: function( event, ui ) {
	    $( this )
		.removeClass( "ui-state-highlight" )
		.find( "p" )
		.html( "Drop here" );
	}
    });
    $( "#droppable" ).resizable( { animate: true, autoHide: true, ghost: true } );
    $( "#datepicker" ).datepicker();
});