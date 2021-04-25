var motherboard_brand = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_motherboard_brand|safe }},
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
            label: ''
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


     var motherboard_integrated_items = {
     type: 'horizontalBar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_motherboard_integrated_items|safe }},
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
            label: ''
        }],
        labels: {{ labels_motherboard_integrated_items|safe }}
        },
        options: {
            title: {
                display: true,
                text: 'Інтегровані елементи'

            },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero:true,
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero: true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  }
                }]
            }
        }
     };

     var motherboard_cpus = {
     type: 'horizontalBar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_motherboard_cpu|safe }},
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
            label: ''
        }],
        labels: {{ labels_motherboard_cpu|safe }}
        },
        options: {
            title: {
                display: true,
                text: 'Центральний процесор (CPU)'

            },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero:true,
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero: true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  }
                }]
            }
        }
     };


     var motherboard_ram = {
     type: 'bar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_motherboard_ram|safe }},
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
            label: ''
        }],
        labels: {{ labels_motherboard_ram|safe }}
        },
        options: {
            title: {
                display: true,
                text: 'тип слоту ОЗУ'
                },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero:true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero: true
                  }
                }]
            }

        }
     };

     var solid_state_drive_brand = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_solid_state_drive_brand|safe }},
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
            label: ''
        }],
        labels: {{ labels_solid_state_drive_brand|safe }}
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

     var solid_state_drive_memory_size = {
     type: 'horizontalBar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_solid_state_drive_memory_size|safe }},
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
            label: ''
        }],
        labels: {{ labels_solid_state_drive_memory_size|safe }}
        },
      options: {
            title: {
                display: true,
                text: 'об\'єм памяті'

            },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero:true,
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero: true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  }
                }]
            }
        }
     };

      var hard_disk_drive_brand = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_hard_disk_drive_brand|safe }},
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
            label: ''
        }],
        labels: {{ labels_hard_disk_drive_brand|safe }}
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

     var hard_disk_drive_memory_size = {
     type: 'horizontalBar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_hard_disk_drive_memory_size|safe }},
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
            label: ''
        }],
        labels: {{ labels_hard_disk_drive_memory_size|safe }}
        },
      options: {
            title: {
                display: true,
                text: 'об\'єм памяті'

            },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero:true,
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero: true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  }
                }]
            }
        }
     };

     var power_supply_consumption = {
     type: 'horizontalBar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_power_supply_consumption|safe }},
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
            label: ''
        }],
        labels: {{ labels_power_supply_consumption|safe }}
        },
       options: {
            title: {
                display: true,
                text: 'Максимальна споживана потужність від мережі'

            },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero:true,
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero: true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  }
                }]
            }
        }
     };

     var power_supply_brand = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_power_supply_brand|safe }},
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
            label: ''
        }],
        labels: {{ labels_power_supply_brand|safe }}
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

     var lan_card_brand = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_lan_card_brand|safe }},
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
            label: ''
        }],
        labels: {{ labels_lan_card_brand|safe }}
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

     var sound_card_brand = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_sound_card_brand|safe }},
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
            label: ''
        }],
        labels: {{ labels_sound_card_brand|safe }}
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

    var optical_drive_type_drive = {
     type: 'horizontalBar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_optical_drive_type|safe }},
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
            label: ''
        }],
        labels: {{ labels_optical_drive_type|safe }}
        },
         options: {
            title: {
                display: true,
                text: 'тип приводу'

            },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero:true,
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero: true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  }
                }]
            }
        }
     };

     var optical_drive_type_connector = {
     type: 'horizontalBar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_optical_drive_type_connector|safe }},
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
            label: ''
        }],
        labels: {{ labels_optical_drive_type_connector|safe }}
        },
      options: {
            title: {
                display: true,
                text: 'тип роз\'єму'

            },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero:true,
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero: true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  }
                }]
            }
        }
     };

     var optical_drive_brand = {
     type: 'bar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_optical_drive_brand|safe }},
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
            label: ''
        }],
        labels: {{ labels_optical_drive_brand|safe }}
        },
      options: {
            title: {
                display: true,
                text: 'бренд'
                },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero:true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero: true
                  }
                }]
            }

        }
     };

     var video_card_brand = {
     type: 'doughnut',
     data: {
        datasets: [{
            data: {{ data_video_card_brand|safe }},
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
            label: ''
        }],
        labels: {{ labels_video_card_brand|safe }}
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

     var video_card_memory_size = {
     type: 'horizontalBar',
     data: {
        datasets: [{
            barPercentage: 0.5,
            barThickness: 50,
            maxBarThickness: 50,
            minBarLength: 10,
            data: {{ data_video_card_memory_size|safe }},
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
            label: ''
        }],
        labels: {{ labels_video_card_memory_size|safe }}
        },
      options: {
            title: {
                display: true,
                text: 'об\'єм памяті'

            },

            animation: {
                duration: 2700,
            },

            scales: {
                yAxes: [{
                  id: 'y-axis-0',
                  gridLines: {
                    display: false
                  },
                  ticks: {
                    beginAtZero:true,
                  },
                  afterBuildTicks: function(chart) {

                  }
                }],
                xAxes: [{
                  id: 'x-axis-0',
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    beginAtZero: true,
                    callback: function (value) { if (Number.isInteger(value)) { return value; } },
                  }
                }]
            }
        }
     };


    window.onload = function() {
      var motherboard_brand_w = document.getElementById('motherboard-brand-chart').getContext('2d');
      var motherboard_form_factor_w = document.getElementById('motherboard-form-factor-chart').getContext('2d');
      var motherboard_integrated_items_w = document.getElementById('motherboard-integrated-items-chart').getContext('2d');
      var motherboard_cpus_w = document.getElementById('motherboard-cpus-chart').getContext('2d');
      var motherboard_ram_w = document.getElementById('motherboard-ram-chart').getContext('2d');

      var solid_state_drive_brand_w = document.getElementById('solid-state-drive-brand-chart').getContext('2d');
      var solid_state_drive_memory_size_w = document.getElementById('solid-state-drive-memory-size-chart').getContext('2d');

      var hard_disk_drive_brand_w = document.getElementById('hard-disk-drive-brand-chart').getContext('2d');
      var hard_disk_drive_memory_size_w = document.getElementById('hard-disk-drive-memory-size-chart').getContext('2d');

      var power_supply_consumption_w = document.getElementById('power-supply-consumption-chart').getContext('2d');
      var power_supply_brand_w = document.getElementById('power-supply-brand-chart').getContext('2d');

      var lan_card_brand_w = document.getElementById('lan-card-brand-chart').getContext('2d');

      var sound_card_brand_w = document.getElementById('sound-card-brand-chart').getContext('2d');

      var optical_drive_type_drive_w = document.getElementById('optical-drive-type-drive-chart').getContext('2d');
      var optical_drive_type_connector_w = document.getElementById('optical-drive-type-connector-chart').getContext('2d');
      var optical_drive_brand_w = document.getElementById('optical-drive-brand-chart').getContext('2d');

      var video_card_brand_w = document.getElementById('video-card-brand-chart').getContext('2d');
      var video_card_memory_size_w = document.getElementById('video-card-memory-size-chart').getContext('2d');

      window.myPie = new Chart(motherboard_brand_w, motherboard_brand);
      window.myPie = new Chart(motherboard_form_factor_w, motherboard_form_factor);
      window.myPie = new Chart(motherboard_integrated_items_w, motherboard_integrated_items);
      window.myPie = new Chart(motherboard_cpus_w, motherboard_cpus);
      window.myPie = new Chart(motherboard_ram_w, motherboard_ram);

      window.myPie = new Chart(solid_state_drive_brand_w, solid_state_drive_brand);
      window.myPie = new Chart(solid_state_drive_memory_size_w, solid_state_drive_memory_size);

      window.myPie = new Chart(hard_disk_drive_brand_w, hard_disk_drive_brand);
      window.myPie = new Chart(hard_disk_drive_memory_size_w, hard_disk_drive_memory_size);

      window.myPie = new Chart(power_supply_consumption_w, power_supply_consumption);
      window.myPie = new Chart(power_supply_brand_w, power_supply_brand);

      window.myPie = new Chart(lan_card_brand_w, lan_card_brand);

      window.myPie = new Chart(sound_card_brand_w, sound_card_brand);

      window.myPie = new Chart(optical_drive_type_drive_w, optical_drive_type_drive);
      window.myPie = new Chart(optical_drive_type_connector_w, optical_drive_type_connector);
      window.myPie = new Chart(optical_drive_brand_w, optical_drive_brand);

      window.myPie = new Chart(video_card_brand_w, video_card_brand);
      window.myPie = new Chart(video_card_memory_size_w, video_card_memory_size);

    };

    function hideAllCharts(){
        hideMotherboardChart();
        hideSolidStateDriveChart();
        hidePowerSupplyChart();
        hideLanCardChart();
        hideSoundCardChart();
        hideOpticalDriveChart();
        hideVideoCardChart();
    }

    function hideMotherboardChart() {
        var x = document.getElementById("motherboard-chart");
        if (x.style.display === "none") {
        x.style.display = "block";
        } else {
        x.style.display = "none";
        }
    }

    function hideSolidStateDriveChart() {
        var x = document.getElementById("solid-state-drive-chart");
        if (x.style.display === "none") {
        x.style.display = "block";
        } else {
        x.style.display = "none";
        }
    }

    function hideHardDiskDriveChart() {
        var x = document.getElementById("hard-disk-drive-chart");
        if (x.style.display === "none") {
        x.style.display = "block";
        } else {
        x.style.display = "none";
        }
    }

    function hidePowerSupplyChart() {
        var x = document.getElementById("power-supply-chart");
        if (x.style.display === "none") {
        x.style.display = "block";
        } else {
        x.style.display = "none";
        }
    }

    function hideLanCardChart() {
        var x = document.getElementById("lan-card-chart");
        if (x.style.display === "none") {
        x.style.display = "block";
        } else {
        x.style.display = "none";
        }
    }

    function hideSoundCardChart() {
        var x = document.getElementById("sound-card-chart");
        if (x.style.display === "none") {
        x.style.display = "block";
        } else {
        x.style.display = "none";
        }
    }

    function hideOpticalDriveChart() {
        var x = document.getElementById("optical-drive-chart");
        if (x.style.display === "none") {
        x.style.display = "block";
        } else {
        x.style.display = "none";
        }
    }

    function hideVideoCardChart(){
        var x = document.getElementById("video-card-chart");
        if (x.style.display === "none") {
        x.style.display = "block";
        } else {
        x.style.display = "none";
        }
    }
