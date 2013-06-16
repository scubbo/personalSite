$(document).ready(function() {
	$('a.moreLink').html('more...');

	$('div.moreSection').each(function() {
		var section = $(this);
		var id = section.attr('id');
		section.append('<a class="closeLink" x-target="' + id + '"></a>');
	});

	$('a.closeLink').html('close');

	$('a.moreLink').click(function() {
		var theLink = $(this);
		var target = $('div#' + theLink.attr('x-target'));
		if (theLink.hasClass('clicked')) {
			theLink.removeClass('clicked');
			target.slideUp();
		} else {
			theLink.addClass('clicked');
			target.slideDown();
		}
	});

	$('a.closeLink').click(function() {
		var theLink = $(this);
		var xTarget = theLink.attr('x-target');
		$('a.moreLink[x-target=' + xTarget + ']').removeClass('clicked');
		$('div.moreSection#' + xTarget).slideUp();
	});
});
