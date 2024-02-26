//
const nav = document.querySelector('.navbar');

if(window.innerWidth > 700) {
    console.log('gdsafg')
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
        console.log(current[1])
    });
}


// animations

const divs = document.querySelectorAll('div');

function handleScroll() {
    divs.forEach(sec => {
        const offset = sec.offsetTop;
  
        const height = sec.offsetHeight;

        const top = window.scrollY; 
        // Check if the current scroll position is within the section
        if (top >= offset && top < offset + height) {
            // Add the show-animate class if the section is in view
            sec.classList.add('show-animate');
        } else {
            // Remove the show-animate class if the section is not in view
            sec.classList.remove('show-animate');
        }
    });
}
window.addEventListener('scroll', handleScroll);
handleScroll();

var owl = $('.owl-carousel');
owl.owlCarousel({
    items:4, 
  // items change number for slider display on desktop
  
    loop:true,
    margin:10,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:true
});
