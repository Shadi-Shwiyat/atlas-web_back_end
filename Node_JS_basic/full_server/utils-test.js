const readDatabase = require('./utils.js');

readDatabase('../database.csv')
  .then(result => {
    console.log(result);
  })
  .catch(error => {
    console.error('Error:', error);
  });