"use strict"

$('#timestamp-form').submit(function(e) {
    e.preventDefault();
    e.stopPropagation();
    $("#timestampSubmit").prop('disabled', true); // disable the button
    var jqxhr = $.getJSON('/api/timestamp/' + $('#timestamp-input').val());
    jqxhr.done(function(res) {
        $('#timestamp-output').html('<pre>' + JSON.stringify(res, null, 2) + '</pre>');
        $("#timestampSubmit").prop('disabled', false); // enable the button
    });
    jqxhr.fail(function(jqxhr, textStatus, error) {
        $('#timestamp-output').html('<pre>' + textStatus + '</pre>');
        $("#timestampSubmit").prop('disabled', false); // enable the button
    });
});