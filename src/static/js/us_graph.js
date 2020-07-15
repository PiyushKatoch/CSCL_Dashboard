// Pie Charts
var colorBackground = [
  "#581845",
  "#93007d",
  "#900C35",
  "#c70039",
  "#d10667",
  "#e72b59",
  "#f74a48",
  "#ff6936",
  "#ff5733",
  "#ff8821",
  "#ffc300",
  "#aebf18",
  "#61b241",
  "#009f61",
  "#008977",
  "#00717d",
];

$.ajax({
  method: "GET",
  url: "us-category-count-chart",
  success: function (data) {
    var config = {
      type: "doughnut",
      data: {
        datasets: [
          {
            data: data.data,
            backgroundColor: colorBackground,
          },
        ],
        labels: data.labels,
      },
      options: {
        title: {
          display: true,
          text: "No of trending videos in a Particular Category",
        },
        legend: {
          display: false,
        },
        responsive: true,
      },
    };

    var ctx = document.getElementById("category-count-chart").getContext("2d");
    new Chart(ctx, config);
  },
  error: function (error_data) {
    console.log(error_data);
  },
});

// Line Chart
$.ajax({
  method: "GET",
  url: "us-category-graph-line",
  success: function (data) {
    var config = {
      type: "line",
      data: {
        labels: data.labels,
        datasets: [
          {
            data: data.data_likes,
            label: "Likes",
            borderColor: "#581845",
            fill: false,
          },
          {
            data: data.data_dislikes,
            label: "Dislikes",
            borderColor: "#c70039",
            fill: false,
          },
          {
            data: data.data_comments,
            label: "Comments",
            borderColor: "#ffc300",
            fill: false,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Comparison of comments, likes and dislikes",
        },
      },
    };

    var ctx = document.getElementById("category-graph-line").getContext("2d");
    new Chart(ctx, config);
  },
  error: function (error_data) {
    console.log(error_data);
  },
});
$.ajax({
  method: "GET",
  url: "us-most-trending-channel",
  success: function (data) {
    console.log(data.data_likes);
    var config = {
      type: "bar",
      data: {
        labels: data.labels,
        datasets: [
          {
            backgroundColor: colorBackground,
            label: "Channels",
            data: data.data,
          },  
        ],
      },
      options: {
        title: {
          display: true,
          text: "Most trending Channels",
        },
      },
    };

    var ctx = document.getElementById("most-trending-channel").getContext("2d");
    new Chart(ctx, config);
  },
  error: function (error_data) {
    console.log(error_data);
  },
});