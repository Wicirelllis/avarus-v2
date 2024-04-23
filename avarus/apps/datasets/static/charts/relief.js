(function () {
    const model_data = JSON.parse(JSON.parse(document.getElementById('chart-relief-data').textContent));

    var ctx = document.getElementById('chart-relief');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['flat elevated plain', 'hill crest', 'shoulder', 'backslope', 'footslope','low plane','riparian zone','lake or pond', 'no data'],
            datasets: [{
                label: 'Relief data',
                data: [
                    model_data['EL_PLN'] ?? 0,
                    model_data['CRST'] ?? 0,
                    model_data['SHLD'] ?? 0,
                    model_data['BACK'] ?? 0,
                    model_data['FOOT'] ?? 0,
                    model_data['LW_PLN'] ?? 0,
                    model_data['RIPZN'] ?? 0,
                    model_data['LAKE'] ?? 0,
                    model_data['NONE'] ?? 0,
                ],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(155, 169, 155, 0.2)',
                    'rgba(125, 189, 23, 0.2)',
                    'rgba(225, 145, 65, 0.2)'

                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(155, 169, 155, 1)',
                    'rgba(125, 189, 23, 1)',
                    'rgba(225, 145, 65, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
})();
