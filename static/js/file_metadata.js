"use strict"

function toggleStatus() {
    var status = $('#file-metadata-status');
    if (status.html() === 'ready') {
        $('#file-metadata-output').html('');
        $('input[type=submit]').prop('disabled', true);
        status.html('uploading');
    }
    else {
        $('input[type=submit]').prop('disabled', false);
        status.html('ready');
    }
}

$('#file-metadata-form').submit(function(e) {
    e.preventDefault();
    e.stopPropagation();
    toggleStatus();
    $.ajax({
        url: '/api/file-metadata/',
        type: 'post',
        data: new FormData(this),
        processData: false,
        contentType: false,
        success: function(res) {
            $('#file-metadata-output').html('<pre>' + JSON.stringify(res, null, 2) + '</pre>');
            $('#file-metadata-form').closest('form').get(0).reset();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $('#file-metadata-output').html('<pre>' + textStatus + '</pre>');
        },
        complete: function() {
            toggleStatus();
        }
    });
});