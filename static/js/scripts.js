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

        var swiper4 = new Swiper(".mySwiper4", {
          navigation: {
            nextEl: ".swiper-button-next4",
            prevEl: ".swiper-button-prev4",
          },
          });
  



        function openNav() {
          document.getElementById("myNav").style.width = "100%";
        }
        
        /* Close when someone clicks on the "x" symbol inside the overlay */
        function closeNav() {
          document.getElementById("myNav").style.width = "0%";
        }
        var btnContainer = document.getElementById("navdown");

        // Get all buttons with class="btn" inside the container
        var btns = btnContainer.getElementsByClassName("down-link");
        
        // Loop through the buttons and add the active class to the current/clicked button
        for (var i = 0; i < btns.length; i++) {
          btns[i].addEventListener("click", function() {
            var current = document.getElementsByClassName("active");
            current[0].className = current[0].className.replace(" active", "");
            this.className += " active";
          });
        }
        window.onload = function(){
          const links = document.querySelectorAll('.down-link');
          const divs = document.querySelectorAll('.gallery');
        
          const hide = function(evt){
            divs.forEach(function(d){
               if(evt.target.getAttribute('itemNo') != d.getAttribute('itemNo')) d.classList.add('display-none');
               else d.classList.remove('display-none');
            });
          }
        
          links.forEach(function(d){ d.onclick = hide; })
        }

       