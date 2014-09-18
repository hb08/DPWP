$(document).ready(function(){
	$('.charChard').click(function(){
		// If any panels are not hidden, hide them
		if($('span.panel').hasClass('active')){
			$('span.panel').removeClass('active').addClass('hide');
		}
		// Show current panel	
		$(this).children('span.panel').addClass('active').removeClass('hide')	
	});
});