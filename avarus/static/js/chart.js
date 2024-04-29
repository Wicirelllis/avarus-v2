(function () {
    const model_data_id = document.currentScript.getAttribute('model_data_id');
    const model_data = JSON.parse(document.getElementById(model_data_id).textContent);
    const canvas_id = document.currentScript.getAttribute('canvas_id');
    const chart_type = document.currentScript.getAttribute('chart_type');

    var ctx = document.getElementById(canvas_id);
    var myChart = new Chart(ctx, {
        type: chart_type,
        data: {
            labels: model_data['labels'],
            datasets: [{
                label: model_data['title'],
                data: model_data['data'],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
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


