// $(window).scroll(function () {
//     var scrollh = $(this).scrollTop();

//     if (scrollh < $("#itemwrap").outerHeight()) {
//         $(".navbar-custom").removeClass("navbar-fixed-top");
//     } else {
//         $(".navbar-custom").addClass("navbar-fixed-top");
//     }
// });

$(function(){
    $(document).on( 'scroll', function(){
        if ($(window).scrollTop() > 100) {
            $('.scroll-top-wrapper').addClass('show');
        } else {
            $('.scroll-top-wrapper').removeClass('show');
        }
    });
});

$(function(){
    $(document).on( 'scroll', function(){
        if ($(window).scrollTop() > 100) {
            $('.scroll-top-wrapper').addClass('show');
        } else {
            $('.scroll-top-wrapper').removeClass('show');
        }
    });
    $('.scroll-top-wrapper').on('click', scrollToTop);
});
 
function scrollToTop() {
    verticalOffset = typeof(verticalOffset) != 'undefined' ? verticalOffset : 0;
    element = $('body');
    offset = element.offset();
    offsetTop = offset.top;
    $('html, body').animate({scrollTop: offsetTop}, 500, 'swing');
}

function infoModal(){
    $('#info-modal').modal('toggle');
}