$(document).ready(function() {
    $('.has-submenu').click(function() {
      $(this).toggleClass('active');
      $(this).children('.menu-item').children('.arrow').toggleClass('rotated');
      if ($(this).hasClass('active')) {
        $(this).children('.submenu').slideDown("slow");
      }
      else {
        $(this).children('.submenu').slideUp("slow");
      }
    });  
  });