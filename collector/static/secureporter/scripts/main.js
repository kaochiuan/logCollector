define(['d3', 'wq/pandas', 'wq/chart'], function (d3, pandas, chart) {
    var svg = d3.select("#chart").append("svg")
    var plot = chart.timeSeries();
    pandas.get('/report-json?format=json', function (data) {
        svg.datum(data).call(plot);
    });
});