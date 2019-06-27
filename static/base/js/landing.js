window.onload = function(){

    // updating the copyright date
    let myDate = document.getElementById("date");
    let presentDate = new Date();
    myDate.innerHTML = presentDate.getFullYear();

    // carousel slide implementation
    let slideIndex = 0

    let showSlide = () => {
        let slides = document.getElementsByClassName('carousel__slide');
        let dots = document.getElementsByClassName('carousel__indicator');

        for(let i=0; i < slides.length; i++){
            slides[i].style.display = 'none';
        }

        slideIndex++;

        if(slideIndex > slides.length){
            slideIndex = 1;
        };

        for(let i=0; i < dots.length; i++){
            dots[i].className = dots[i].className.replace(" current-slide", "");
        }

        slides[slideIndex - 1].style.display = 'block';
        dots[slideIndex - 1].className += " current-slide";

        // setting the timer for changing the carousel slide
        setTimeout(showSlide, 5000);
    }

    showSlide();

    // start div animations
    let animItem = document.querySelectorAll('.animatable');

    function checkScroll(e){
    animItem.forEach(item => {

        let slideInAt = (window.pageYOffset + window.innerHeight) - item.getBoundingClientRect().height / 3;
        // buttom of the image
        let slideBottom = item.offsetTop + item.getBoundingClientRect().height;
        let isHalfShown = slideInAt > item.offsetTop;
        let isNotScrolledPassed = window.pageYOffset < slideBottom;

        if(isHalfShown && isNotScrolledPassed){
            item.classList.add('active');
        }else{
            item.classList.remove('active');
        }

    });
    }

    window.addEventListener('scroll', checkScroll);
}