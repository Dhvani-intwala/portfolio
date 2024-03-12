
const nav = document.querySelector('#nav');

if(window.innerWidth > 700) {
window.addEventListener('scroll', () =>{
    if(window.scrollY >= 56){
        nav.classList.add('navbar-scrolled');
    }else if (window.screenY < 56){
        nav.classList.remove('navbar-scrolled');
    }
});
}
$(document).ready(function() {
    // $('a[href*="#"]').on('click', function(e) {
    //     e.preventDefault();
    //     var target = $(this).attr("href");
    //     // Check if the target is not empty and starts with #
    //     if (target && target.startsWith('#')) {
    //         $('html, body').stop().animate({
    //             scrollTop: $(target).offset().top
    //         }, 1000, function() {
    //             window.location.hash = target;
    //         });
    //     }
    // });
    

    $(window).scroll(function() {
        var scrollDistance = $(window).scrollTop();
        $('.page-section').each(function(i) {
            var sectionTop = $(this).offset().top;
            var sectionBottom = sectionTop + $(this).outerHeight();
            // Adjusting scroll distance to set active class when section is at least 50% visible
            if (scrollDistance >= sectionTop - $(window).height() / 2 && scrollDistance < sectionBottom) {
                $('#nav a.active').removeClass('active');
                $('#nav a').eq(i+1).addClass('active');
            }
        });
    }).scroll();
});

document.getElementById('contact-form').addEventListener('submit', function () {
    document.getElementById('scroll_position').value = window.scrollY;
});

