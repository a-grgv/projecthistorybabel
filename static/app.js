$(document).ready(function() {

    $('#generate_button').on('click', function() {
        var title = $('#title').val();
        var article = $('#article').val();
        $('#loading').attr("style", 'display: "block"');

        req = $.ajax({
            url : '/create',
            type : 'POST',
            data : { article : article, title : title}
        });

        req.done(function(data) {
            $('#loading').attr("style", 'display: "none"');
            console.log(data);
            $('#summary_box').attr("style", 'display: "block"');
            $('#summary').text(data.doc_summary);
            $('#event_box').attr("style", 'display: "block"');
            $.each(data.doc_events, function (i) {
                $("#event").find('tbody')
                        .append($('<tr>')
                        .append($('<td>')
                                .text(data.doc_events[i][1])
                        )
                        .append($('<td>')
                                .text(data.doc_events[i][2])
                        )
                );
             });
        });

    });

});