// function to load json data
fetch('/api/dashboard_data/')
  .then(response => response.json())
  .then(data => {
    // Use the data in your JavaScript code
    const numbersList = JSON.parse(data).map(item => item.intensity);

    // setup data block
    const gdata = {
      labels: Array.from({ length: numbersList.length }, (_, index) => index),
      datasets: [
        {
          label: "intensity",
          data: numbersList,
          backgroundColor: [
            'red',
            'green',
            'blue',
            'yellow',
            'orange',
            'purple',
          ],
        },
      ],
    };

    // config block
    const config = {
      type: "bar",
      data: gdata,
      options: {
        indexAxis: "x",
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    };

    // render block
    const myChart = new Chart(
      document.getElementById("myChart"),
      config,
    );
  })
  .catch(error => {
    console.error('Error:', error);
  });
