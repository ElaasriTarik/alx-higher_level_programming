$(function () {
	add_item = $('DIV#add_item');
	my_list = $('UL.my_list');
	add_item.click(function () {
		my_list.append('<li>Item</li>');
	});
});
