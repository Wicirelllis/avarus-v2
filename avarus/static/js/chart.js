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
                    'rgba(191, 0, 0, 0.2)',
                    'rgba(0, 191, 191, 0.2)',
                    'rgba(191, 95, 0, 0.2)',
                    'rgba(0, 95, 191, 0.2)',
                    'rgba(191, 191, 0, 0.2)',
                    'rgba(0, 0, 191, 0.2)',
                    'rgba(95, 191, 0, 0.2)',
                    'rgba(95, 0, 191, 0.2)',
                    'rgba(0, 191, 0, 0.2)',
                    'rgba(191, 0, 191, 0.2)',
                    'rgba(0, 191, 95, 0.2)',
                    'rgba(191, 0, 95, 0.2)',
                ],
                borderColor: [
                    'rgba(191, 0, 0, 1)',
                    'rgba(0, 191, 191, 1)',
                    'rgba(191, 95, 0, 1)',
                    'rgba(0, 95, 191, 1)',
                    'rgba(191, 191, 0, 1)',
                    'rgba(0, 0, 191, 1)',
                    'rgba(95, 191, 0, 1)',
                    'rgba(95, 0, 191, 1)',
                    'rgba(0, 191, 0, 1)',
                    'rgba(191, 0, 191, 1)',
                    'rgba(0, 191, 95, 1)',
                    'rgba(191, 0, 95, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    display: chart_type == 'pie' ? false : true,
                    suggestedMin: 0,
                    suggestedMax: 100,
                    beginAtZero: true
                }
            }
        }
    });    
})();


