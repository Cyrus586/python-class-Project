document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', function(){
        if(window.screenY > 50 ){
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.30)';
        }else{
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.15)';
        }
    });
});

