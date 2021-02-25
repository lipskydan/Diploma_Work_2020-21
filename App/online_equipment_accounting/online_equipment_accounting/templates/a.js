var motherboard_brand = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_motherboard_brand|safe }},
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            label: ''
        }],
        labels: {{ labels_motherboard_brand|safe }}
        },
        options: {
            title: {
                display: true,
                text: 'Бренд'

            },
            animation: {
                duration: 2700,
            }
        }
     };

     var motherboard_form_factor = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_motherboard_form_factor|safe }},
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            label: {{ labels_motherboard_form_factor|safe }}
        }],
        labels: {{ labels_motherboard_form_factor|safe }}
        },
        options: {
            title: {
                display: true,
                text: 'Форм-фактор'
            },
            animation: {
                duration: 2700,
            }
        }
     };

    window.onload = function() {
      var motherboard_brand_w = document.getElementById('motherboard-brand-chart').getContext('2d');
      var motherboard_form_factor_w = document.getElementById('motherboard-form-factor-chart').getContext('2d');
      window.myPie = new Chart(motherboard_brand_w, motherboard_brand);
      window.myPie = new Chart(motherboard_form_factor_w, motherboard_form_factor);
    };