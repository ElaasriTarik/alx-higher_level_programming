$(function () {
	toggle_header = $('#toggle_header');
	header = $('header');
	toggle_header.click(function () {
		if (header.hasClass('red')) {
			header.removeClass('red');
			header.addClass('green');
		} else {
			header.removeClass('green');
			header.addClass('red');
		}
	});
});
