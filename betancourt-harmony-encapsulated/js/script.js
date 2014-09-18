$(document).ready(function(){
	$('.charChard').click(function(){
		// If this is not showing already
		if(!$(this).children('span.panel').hasClass('active')){
			console.log($(this).hasClass('active'));
			// If any panels are not hidden, hide them
			if($('span.panel').hasClass('active')){
				$('span.panel').removeClass('active').addClass('hide');
			}
			// If the title panel is not hidden, hide it
			if(!$('#titlePanel').hasClass('hide')){
				$('#titlePanel').addClass('hide');
			}
			// Show current panel	
			$(this).children('span.panel').addClass('active').removeClass('hide')
		}else{
			// If it is showing, then remove
			$('span.panel').removeClass('active').addClass('hide');
			// And show title panel
			$('#titlePanel').removeClass('hide');
		}
	});
});