// Simple http server using http module
// Displays Hello Holberton School! on every endpoint

const http = require('http');

// Create server and listen on port 1245
const app = http.createServer((req, res) => {
  res.write('Hello Holberton School!');
  res.end();
});

app.listen(1245);
