$.ajax({
  method: "GET",
  url: "bubble-chart",
  success: function (data) {
    india_storage = [];
    for (i = 0; i < data.india_views.length; i++) {
      x = data.india_labels[i];
      y = data.india_views[i];
      z = data.india_likes[i] / 1000000;
      var json = { x: x, y: y, r: z };
      india_storage.push(json);
    }
      india_storage = [];
      for (i = 0; i < data.india_views.length; i++) {
          x = data.india_labels[i];
          y = data.india_likes[i];
          z = (data.india_views[i] / 300000000);
          var json = { x: x, y: y, r: z };
          india_storage.push(json);
      }
      us_storage = [];
      for (i = 0; i < data.us_views.length; i++) {
          x = data.us_labels[i];
          y = data.us_likes[i];
          z = (data.us_views[i] / 300000000);
          var json = { x: x, y: y, r: z };
          us_storage.push(json);
      }
      uk_storage = [];
      for (i = 0; i < data.uk_views.length; i++) {
          x = data.uk_labels[i];
          y = data.uk_likes[i];
          z = (data.uk_views[i] / 300000000);
          var json = { x: x, y: y, r: z };
          uk_storage.push(json);
      }
    console.log(data.india_views);
    var config = {
      type: "bubble",
      data: {
        datasets: [
          {
            label: "India",
            backgroundColor: "#581845",
            data: india_storage,
          },
          {
            label: "US",
            backgroundColor: "#c70039",
            data: us_storage,
          },
          {
            label: "UK",
            backgroundColor: "#ffc300",
            data: uk_storage,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Bubble Chart of views and Likes in a particular category of a Country",
        },
          scales: {
              yAxes: [{
                  scaleLabel: {
                      display: true,
                      labelString: "Likes"
                  }
              }],
              xAxes: [{
                  scaleLabel: {
                      display: true,
                      labelString: "Category"
                  }
              }]
          }
      },
    };
    var ctx = document.getElementById("bubble-chart").getContext("2d");
    new Chart(ctx, config);
  },
  error: function (error_data) {
    console.log(error_data);
  },
});
