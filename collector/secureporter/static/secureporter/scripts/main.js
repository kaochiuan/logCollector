define(['d3', 'draw'], function (d3, draw) {
    var start = "2017-04-20";
    var end = "2017-04-25";

    var parseDate = d3.timeParse("%Y-%m-%d");
    var formatDate = d3.timeFormat("%Y-%m-%d");
    d3.select('#renderReport')
        .on("click", function () {
            d3.select('svg').remove();
            d3.select('table').remove();
            start = formatDate(parseDate(document.getElementById('date_start').value));
            end = formatDate(parseDate(document.getElementById('date_end').value));

            draw.renderReport(start, end);
        });

    d3.select('#clearRecords')
        .on("click", function () {
            if (confirm('All historical data will be clear, are you sure?') == true) {
                d3.select('svg').remove();
                d3.select('table').remove();
                d3.json('/delete_everything', function (error, data) {
                    d3.select("#fail_rate").text();
                    d3.select("#fail_count").text();
                    d3.select("#total_count").text();
                    d3.select("#result").html("")
                        .append('h1').html(data.result);
                });
            }
        });
});
