"use strict"

$('#timestamp-form').submit(function(e) {
    e.preventDefault();
    e.stopPropagation();
    var jqxhr = $.getJSON('/api/timestamp/' + $('#timestamp-input').val());
    jqxhr.done(function(res) {
        $('#timestamp-output').html('<pre>' + JSON.stringify(res, null, 2) + '</pre>');
    });
    jqxhr.fail(function(jqxhr, textStatus, error) {
        $('#timestamp-output').html('<pre>' + textStatus + '</pre>');
    });
});