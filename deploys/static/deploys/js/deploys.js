(function($) {
    var start_byte = 0
    function get_log() {
        $.get('/get_log/' + btoa($('#log-path').val()) + '/' + start_byte, function(data) {
            if (start_byte == 0) {
                $('.console-log-output').find('code').text('');
            }
            start_byte = data['end_byte'];
            $('.console-log-output').find('code').append(data['content']);
            setTimeout(function() {
                get_log()
            }, 3000);
        });
    };
    $(function() {
        get_log()
    });
})(django.jQuery);
