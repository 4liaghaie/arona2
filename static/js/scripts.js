var swiper1 = new Swiper(".mySwiper1", {
    
    slidesPerView: 2,
    spaceBetween: 30,
    pagination: {
      el: ".swiper-pagination1",
      clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next1",
        prevEl: ".swiper-button-prev1",
      },
      breakpoints: {
        800: {
       
          slidesPerView: 3,
          spaceBetween: 10,
        },},
    });

    var swiper2 = new Swiper(".mySwiper2", {
        loop: true,
        pagination: {
            el: ".swiper-pagination2",
            clickable: true,
          },
        
        navigation: {
          nextEl: ".swiper-button-next2",
          prevEl: ".swiper-button-prev2",
        },
      });

      var swiper3 = new Swiper(".mySwiper3", {
        navigation: {
          nextEl: ".swiper-button-next3",
          prevEl: ".swiper-button-prev3",
        },
        
    
        });
        document
        .querySelector('.button1')
        .addEventListener('click', function (e) {
          e.preventDefault();
          swiper3.slideTo(0, 0);
        });

        document
        .querySelector('.button2')
        .addEventListener('click', function (e) {
          e.preventDefault();
          swiper3.slideTo(4, 0);
        });
        document
        .querySelector('.button3')
        .addEventListener('click', function (e) {
          e.preventDefault();
          swiper3.slideTo(16, 0);
        });
        document
        .querySelector('.button4')
        .addEventListener('click', function (e) {
          e.preventDefault();
          swiper3.slideTo(17, 0);
        });
        document
        .querySelector('.button5')
        .addEventListener('click', function (e) {
          e.preventDefault();
          swiper3.slideTo(20, 0);
        });
        document
        .querySelector('.button6')
        .addEventListener('click', function (e) {
          e.preventDefault();
          swiper3.slideTo(1, 0);
        });


        
        



