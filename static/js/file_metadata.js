"use strict"

var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function toggleStatus() {
    var status = $('#status');
    if (status.html() === 'ready') {
        $('#metadata').html('');
        $('input[type=submit]').prop('disabled', true);
        status.html('uploading');
    }
    else {
        $('input[type=submit]').prop('disabled', false);
        status.html('ready');
    }
}

$('#form').submit(function(e) {
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
            $('#metadata').html('<pre>' + JSON.stringify(res, null, 2) + '</pre>');
            $('#form').closest('form').get(0).reset();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            $('#metadata').prepend('<pre>' + textStatus + '</pre>');
        },
        complete: function() {
            toggleStatus();
        }
    });
})