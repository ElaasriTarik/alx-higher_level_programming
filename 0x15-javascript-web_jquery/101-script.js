document.addEventListener('DOMContentLoaded', function () {
	my_list = $('UL.my_list');
	$('#add_item').click(function () {
		my_list.append('<li>Item</li>');
	});
	$('#remove_item').click(function () {
		my_list.children().last().remove();
	});
	$('#clear_list').click(function () {
		my_list.empty();
	});
});
