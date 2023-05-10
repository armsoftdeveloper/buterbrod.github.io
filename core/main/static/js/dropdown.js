$('.dropdown > .caption').on('click', function() {
    $(this).parent().toggleClass('open');
});

// $('.price').attr('data-currency', 'RUB');

$('.dropdown > .list > .item').on('click', function() {
    $('.dropdown > .list > .item').removeClass('selected');
    $(this).addClass('selected').parent().parent().removeClass('open').children('.caption').html($(this).html());
});

$(document).on('keyup', function(evt) {
    if ((evt.keyCode || evt.which) === 27) {
        $('.dropdown').removeClass('open');
    }
});

$(document).on('click', function(evt) {
    if ($(evt.target).closest(".dropdown > .caption").length === 0) {
        $('.dropdown').removeClass('open');
    }
});