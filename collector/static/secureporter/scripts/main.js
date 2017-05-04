define(['d3', 'draw'], function (d3, draw ) {
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
});
