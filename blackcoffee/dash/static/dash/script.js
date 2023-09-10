// function to load json data

// intensity chart
fetch('/api/intensity/')
  .then(response => response.json())
  .then(data => {
    // Use the data in your JavaScript code
    let numbersList = JSON.parse(data).map(item => item.intensity);

    // setup data block
    let gdata = {
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
    let config = {
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
    let myChart = new Chart(
      document.getElementById("myChartIntensity"),
      config,
    );
  })
  .catch(error => {
    console.error('Error:', error);
});

// Likelihood chart
fetch('/api/likelihood/')
  .then(response => response.json())
  .then(data => {
    // Use the data in your JavaScript code
    let numbersList = JSON.parse(data).map(item => item.likelihood);

    // setup data block
    let gdata = {
      labels: Array.from({ length: numbersList.length }, (_, index) => index),
      datasets: [
        {
          label: "likelihood",
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
    let config = {
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
    let myChart = new Chart(
      document.getElementById("myChartLikelihood"),
      config,
    );
  })
  .catch(error => {
    console.error('Error:', error);
});

// relevance chart
fetch('/api/relevance/')
  .then(response => response.json())
  .then(data => {
    // Use the data in your JavaScript code
    let numbersList = JSON.parse(data).map(item => item.relevance);

    // setup data block
    let gdata = {
      labels: Array.from({ length: numbersList.length }, (_, index) => index),
      datasets: [
        {
          label: "relevance",
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
    let config = {
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
    let myChart = new Chart(
      document.getElementById("myChartRelevance"),
      config,
    );
  })
  .catch(error => {
    console.error('Error:', error);
});

// year chart
fetch('/api/year/')
  .then(response => response.json())
  .then(data => {
    // Use the data in your JavaScript code
    let numbersList = JSON.parse(data).map(item => item);

    // setup data block
    let gdata = {
      labels: Array.from({ length: numbersList.length }, (_, index) => index),
      datasets: [
        {
          label: "year",
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
    let config = {
      type: "bar",
      data: gdata,
      options: {
        indexAxis: "x",
        scales: {
          y: {
            beginAtZero: false,
          },
        },
      },
    };

    // render block
    let myChart = new Chart(
      document.getElementById("myChartYear"),
      config,
    );
  })
  .catch(error => {
    console.error('Error:', error);
});
