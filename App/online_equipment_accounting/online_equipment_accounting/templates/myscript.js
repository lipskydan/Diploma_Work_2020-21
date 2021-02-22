<script>

     var motherboard_brand = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_motherboard_brand|safe }},
            backgroundColor: [
            '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3'
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
            '#808080', '#A9A9A9', '#C0C0C0', '#D3D3D3'
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

  </script>
