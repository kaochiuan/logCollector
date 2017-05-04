define(['d3', 'wq/chart'], function (d3, chart) {
    return {
        renderReport: function (start, end) {
            // clear garbage element
            d3.select('#summary > div').remove();
            d3.select('#chart > div').remove();
            d3.select('#raw_table > div').remove();
            d3.select("#result > div").remove();

            // load raw data to table
            d3.json('/records?format=json&start=' + start + '&end=' + end, function (error, data) {
                function tabulate(data, columns) {
                    d3.select('#raw_table').append('div');
                    d3.select('#raw_table > div').append('hr');
                    d3.select('#raw_table > div').append('h1').text("Raw data");
                    d3.select('#raw_table > div').append('p');
                    var table = d3.select('#raw_table > div').append('table');
                    var thead = table.append('thead')
                    var tbody = table.append('tbody');

                    // append the header row
                    thead.append('tr')
                        .selectAll('th')
                        .data(columns).enter()
                        .append('th')
                        .text(function (column) { return column; });

                    // create a row for each object in the data
                    var rows = tbody.selectAll('tr')
                        .data(data)
                        .enter()
                        .append('tr');

                    // create a cell in each row for each column
                    var cells = rows.selectAll('td')
                        .data(function (row) {
                            return columns.map(function (column) {
                                return { column: column, value: row[column] };
                            });
                        })
                        .enter()
                        .append('td')
                        .text(function (d) { return d.value; });

                    return table;
                }

                // render the table(s)
                tabulate(data, ['record_id', 'device', 'record_dt', 'is_success', 'spent_seconds']); // 5 column table

            });

            // text the count and rate of data
            d3.json('/failure_rate?start=' + start + '&end=' + end, function (error, data) {
                d3.select('#summary').append('div');
                d3.select('#summary > div').append('h1').text("Summary");
                d3.select('#summary > div').append('p');
                d3.select('#summary > div').append('span').text('Fail count:' + data.total_count);
                d3.select('#summary > div').append('br');
                d3.select('#summary > div').append('span').text('Fail count:' + data.fail_count);
                d3.select('#summary > div').append('br');
                d3.select('#summary > div').append('span').text('Fail rate:' + data.fail_rate);
            });

            // draw response time of data
            d3.json('/plotdata?start=' + start + '&end=' + end, function (error, data) {
                d3.select('#chart').append('div');
                d3.select('#chart > div').append('hr');
                d3.select('#chart > div').append('h1').text("Response trend chart");
                d3.select('#chart > div').append('p');
                var svg = d3.select('#chart > div').append('svg');
                var plot = chart.timeSeries()
                    .timeFormat("%Y-%m-%dT%H:%M:%S%Z")
                    .width(800)
                    .height(300);

                svg.datum(data).call(plot);
            });

        }
    }

});
