let energyChart;

function updateChart(energyType) {
  fetch(`/data/${energyType}`)
    .then(response => response.json())
    .then(data => {
      const ctx = document.getElementById('energyChart').getContext('2d');
      if (energyChart) {
        energyChart.destroy();
      }
      energyChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: data.labels,
          datasets: [{
            label: energyType,
            data: data.values,
            borderColor: '#001f3f',
            backgroundColor: 'rgba(0, 191, 255, 0.2)',
            tension: 0.3,
            fill: true,
            pointRadius: 2
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              labels: { color: 'white' }
            }
          },
          scales: {
            x: {
              ticks: { color: 'white' }
            },
            y: {
              ticks: { color: 'white' },
              beginAtZero: true
            }
          }
        }
      });
    });
}
