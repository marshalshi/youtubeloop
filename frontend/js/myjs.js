$(document).ready(function(){
    $('.filter-top').css('display','none');
    $('.search-pager').css('display', 'none');
    $('#yt-masthead-container').css('display', 'none');
    $('#search-results a').click(function(){
        var this_id = $(this).attr('href').slice(9);
        $(this).attr('href',this_id);
    });
});