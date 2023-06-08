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
          spaceBetween: 20,
        },},
    });

    var swiper2 = new Swiper(".mySwiper2", {
      nextButton: '.swiper-button-next2',
        prevButton: '.swiper-button-prev2',
        loop: true,
        navigation: {
          nextEl: ".swiper-button-next2",
          prevEl: ".swiper-button-prev2",
        },
        pagination: {
          el: '.swiper-pagination',
          clickable: true,
          type: 'custom',
          renderCustom: function (swiper, current, total) {
            var out = ''
            for (i = 1; i < total+1; i++) {
              if (i == current) {
                out = out + '<span class="swiper-pagination-bullet swiper-pagination-bullet-active" tabindex='+i+' role="button" aria-label="Go to slide '+i+1+'"></span>';
              }
              else {
                out = out + '<span class="swiper-pagination-bullet" tabindex='+i+' role="button" aria-label="Go to slide '+i+1+'"></span>';
              }
            };
            return out;
          },}  
        
        

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

        function openNav() {
          document.getElementById("myNav").style.width = "100%";
        }
        
        /* Close when someone clicks on the "x" symbol inside the overlay */
        function closeNav() {
          document.getElementById("myNav").style.width = "0%";
        }


        
        



