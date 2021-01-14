$(document).ready(function() {
  $(document).on('click', '.note', function() {
    let clickedNote = $(this);
    const pk = clickedNote.attr('id');
    const url = Urls['notes:show-note']();
    $.ajax({
      url: url,
      data: {
        'pk': pk
      },
      success: function(response) {
        $('.note-container').html(response);
        $('.note').each(function() {
          $(this).css({'background-color': 'white'});
        });
        clickedNote.css({'background-color': '#F9FAFC'});
        $('.note-container pre').each(function(i, block) {
          hljs.highlightBlock(block);
        });
      }
    });
  });
});