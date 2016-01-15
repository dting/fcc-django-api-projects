"use strict"

$('#request-parser-button').on('click', function() {
    var jqxhr = $.getJSON('/api/request-header-parser/');
    jqxhr.done(function(res) {
        $('#request-parser-output').html('<pre>' + JSON.stringify(res, null, 2) + '</pre>');
    });
    jqxhr.fail(function(jqxhr, textStatus, error) {
        $('#request-parser-output').html('<pre>' + textStatus + '</pre>');
    });
});