"use strict"

$('#image-search-form').submit(function(e) {
    e.preventDefault();
    e.stopPropagation();
    $('#imageSearchSubmit').prop('disabled', true);
    var url = '/api/image-search/search/' + encodeURIComponent($('#image-search-terms').val());
    var offset = $('#image-search-offset').val();
    if (offset && !isNaN(+offset)) {
        url += '?offset=' + +offset;
    }
    var jqxhr = $.getJSON(url);
    jqxhr.done(function(res) {
        $('#image-search-output').html('<pre>' + JSON.stringify(res, null, 2) + '</pre>');
        $('#imageSearchSubmit').prop('disabled', false);
    });
    jqxhr.fail(function(jqxhr, textStatus, error) {
        $('#image-search-output').html('<pre>' + textStatus + '</pre>');
        $('#imageSearchSubmit').prop('disabled', false);
    });
});


$('#image-search-latest-button').on('click', function() {
    var jqxhr = $.getJSON('/api/image-search/latest/');
    $('#image-search-latest-button').prop('disabled', true);
    jqxhr.done(function(res) {
        $('#image-search-latest-output').html('<pre>' + JSON.stringify(res, null, 2) + '</pre>');
        $('#image-search-latest-button').prop('disabled', false);
    });
    jqxhr.fail(function(jqxhr, textStatus, error) {
        $('#image-search-latest-output').html('<pre>' + textStatus + '</pre>');
        $('#image-search-latest-button').prop('disabled', false);
    });
});