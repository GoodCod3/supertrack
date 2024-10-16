/* globals Chart:false */

(() => {
    'use strict'
  
    // Graphs
    // const ctx = document.getElementById('myChart')
    // // eslint-disable-next-line no-unused-vars
    // new Chart(ctx, {
    //   type: 'line',
    //   data: {
    //     labels: [
    //       'Sunday',
    //       'Monday',
    //       'Tuesday',
    //       'Wednesday',
    //       'Thursday',
    //       'Friday',
    //       'Saturday'
    //     ],
    //     datasets: [{
    //       data: [
    //         15339,
    //         21345,
    //         18483,
    //         24003,
    //         23489,
    //         24092,
    //         12034
    //       ],
    //       lineTension: 0,
    //       backgroundColor: 'transparent',
    //       borderColor: '#007bff',
    //       borderWidth: 4,
    //       pointBackgroundColor: '#007bff'
    //     }]
    //   },
    //   options: {
    //     plugins: {
    //       legend: {
    //         display: false
    //       },
    //       tooltip: {
    //         boxPadding: 3
    //       }
    //     }
    //   }
    // })

    // Chart 2
        // Graphs
        const ctx2 = document.getElementById('myChart2');
        const numbers = [];
        const values = [];
        for (let index = 0; index < 31; index++) {
          numbers.push(index);
          values.push(Math.floor(Math.random() * 20));
          
        }
        // eslint-disable-next-line no-unused-vars
        new Chart(ctx2, {
          type: 'line',
          data: {
            labels: numbers,
            datasets: [{
              data: values,
              lineTension: 0,
              backgroundColor: 'transparent',
              borderColor: '#007bff',
              borderWidth: 4,
              pointBackgroundColor: '#007bff'
            }]
          },
          options: {
            plugins: {
              legend: {
                display: false
              },
              tooltip: {
                boxPadding: 3
              }
            }
          }
        })
    
  })()