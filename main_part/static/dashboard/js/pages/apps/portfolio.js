$(function () {
	$('.brands a').click(function (e) {
		$('.brands ul li').removeClass('active');
		$(this).parent('li').addClass('active');
		var itemSelected = $(this).attr('data-filter');
		$('.portfolio-item').each(function () {
			if (itemSelected == '*') {
				$(this).removeClass('filtered').removeClass('selected');
				return;
			} else if ($(this).is(itemSelected)) {
				$(this).removeClass('filtered').addClass('selected');
			} else {
				$(this).removeClass('selected').addClass('filtered');
			}
		});
	});
}); 