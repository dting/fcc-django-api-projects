"use strict"

$('#request-parser-button').on('click', function() {
    $('#request-parser-button').prop('disabled', true);
    var jqxhr = $.getJSON('/api/request-header-parser/');
    jqxhr.done(function(res) {
        $('#request-parser-output').html('<pre>' + JSON.stringify(res, null, 2) + '</pre>');
        $('#request-parser-button').prop('disabled', false);
    });
    jqxhr.fail(function(jqxhr, textStatus, error) {
        $('#request-parser-output').html('<pre>' + textStatus + '</pre>');
        $('#request-parser-button').prop('disabled', false);
    });
});