$(document).ready(function() {
    $('a[href*="#"]').on('click', function(e) {
        e.preventDefault();
        var target = $(this).attr("href");
        
        $('html, body').stop().animate({
            scrollTop: $(target).offset().top
        }, 800, function() {
            window.location.hash = target;
        });
    });


    $(window).scroll(function() {
        var scrollDistance = $(window).scrollTop();
        $('.page-section').each(function(i) {
            var sectionTop = $(this).offset().top;
            var sectionBottom = sectionTop + $(this).outerHeight();
            
            console.log('Scroll Distance:', scrollDistance);
            console.log('Section Top:', sectionTop);
            console.log('Section Bottom:', sectionBottom);
            
            // Adjusting scroll distance to set active class when section is at least 50% visible
            if (scrollDistance >= sectionTop - $(window).height() / 2 && scrollDistance < sectionBottom){
                console.log('Adding active class to navbar link:', i+1);
                $('.navbar a.active').removeClass('active');
                $('.navbar a').eq(i+1).addClass('active');
            }
        });
    }).scroll();
    
});


const nav = document.querySelector('.navbar');

if(window.innerWidth > 700) {
window.addEventListener('scroll', () =>{
    if(window.scrollY >= 56){
        nav.classList.add('navbar-scrolled');
    }else if (window.screenY < 56){
        nav.classList.remove('navbar-scrolled');
    }
});
}

// Nav bar active class

const header = document.getElementById("header");
const btns = header.getElementsByClassName("nav-link");
for (let i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active")
        current[0].classList.remove("active");
        this.classList.add("active");
    });
}

const form = document.querySelector('form');