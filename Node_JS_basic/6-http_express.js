// Simple http server using http module
// Displays Hello Holberton School! on every endpoint

const express = require('express');

// Create server and listen on port 1245
const app = express();
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
