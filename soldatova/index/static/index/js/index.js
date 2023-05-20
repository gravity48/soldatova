$(document).ready(function () {
    $('#menu-button').click(function (e) {
        e.preventDefault();
        e.stopPropagation();
        $(this).toggleClass('is_close');
        $('#mobile-menu> .menu-content').animate({height: 'toggle'}, 300);
    });

    function animateScroll(elem) {
        $('html,body').stop().animate({scrollTop: $(elem).offset().top - 100}, 600);
    }

    function animateScroll150(elem) {
        $('html,body').stop().animate({scrollTop: $(elem).offset().top - 170}, 600);
    }

    $('#mobile-menu .menu-content .menu-content-ul li a').click((e) => {
        e.stopPropagation();
        e.preventDefault();
        animateScroll($(e.currentTarget).attr('href'));
        $('#menu-button').click();
    });

    $('#mobile-menu .menu-header .menu-content-ul li a').click((e) => {
        e.stopPropagation();
        e.preventDefault();
        animateScroll150($(e.currentTarget).attr('href'));
    });

    $('.custom-video-controller').click((e) => {
        e.preventDefault();
        e.stopPropagation();
        $(e.currentTarget).toggleClass('is_played');
        $(e.currentTarget).siblings('video').trigger('play');
        $(e.currentTarget).siblings('video').attr('controls', true);
        $(e.currentTarget).hide();
    });


    $(".owl-carousel").owlCarousel({
            loop: true,
            items: 1,
            center: true,
            responsiveClass: true,
            navText: ['<img src="/static/index/svg/arrow-left.svg" alt="">', '<img src="/static/index/svg/arrow-right.svg" alt="">'],
            navContainer: '#img-reviews-nav',
            dotsContainer: '#reviews-dot',
            responsive: {
                1200: {
                    items: 2,
                },
                768: {
                    items: 2,
                },
                0: {
                    items: 1,
                }
            }
        }
    );

    $('.preloader').fadeOut(1000);

});