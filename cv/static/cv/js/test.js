(function ($) {
  $(document).ready(function(){
	

  $(window).scroll(function(e) {
      var scroll = $(window).scrollTop();
      if (scroll >= 10) {
          $('.navbar').removeClass("navbar-hide");
      }
      else{
        $('.navbar').addClass("navbar-hide");
      }

  })


});
  }(jQuery));
