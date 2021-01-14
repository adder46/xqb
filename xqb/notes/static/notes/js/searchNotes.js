$(document).ready(function() {
  $('#search-box').on('input', function() {
    const notebook = window.location.href.split('/')[4];
    const by = $('.options').attr('by');
    const url = Urls['notes:search-notes'](notebook, by);
    console.log(url);
    const searchQuery = $(this).val();
    $.ajax({
      url: url,
      data: {
        'query': searchQuery
      },
      success: function(response) {
        $('.notes').html(response);
        $('.notes pre').each(function(i, block) {
          hljs.highlightBlock(block);
        });
      }
    });
  });
});