(function () {
    const model_data = JSON.parse(JSON.parse(document.getElementById('chart-soil-data').textContent));

    var ctx = document.getElementById('chart-soil');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['gravel or coarser', 'sand', 'loam', 'clay', 'silt','organic (if no mineral soil)', 'no data'],
            datasets: [{
                label: 'Soil texture data',
                data: [
                    model_data['GRV'] ?? 0,
                    model_data['SND'] ?? 0,
                    model_data['LOM'] ?? 0,
                    model_data['CLY'] ?? 0,
                    model_data['SLT'] ?? 0,
                    model_data['ORG'] ?? 0,
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
