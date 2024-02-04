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
console.log(header)
const btns = header.getElementsByClassName("nav-link");
for (let i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
        var current = document.getElementsByClassName("active")
        current[0].classList.remove("active");
        this.classList.add("active");
        console.log(current[1])
    });
}
