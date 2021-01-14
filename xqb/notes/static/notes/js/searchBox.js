$(document).ready(function() {
  $('.by').on('click', function() {
    $(this).toggleClass('active');
    if ($(this).hasClass('active')) {
      $('.options').slideUp();    
    }
    else {
      $('.options').slideDown();  
    }
  });

  $(document).on('click', '.option', function() {
    const value = $(this).attr('id');
    $('.options').attr('by', value);
    $('.selected').text(value);
  });  
});

