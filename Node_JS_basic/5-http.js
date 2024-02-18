// Simple http server using http module
// Displays Hello Holberton School! on every endpoint

const http = require('http');
const fs = require('fs');

// Create server and listen on port 1245
const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  }

  if (req.url === '/students') {
    res.write('This is the list of our students\n');

    return new Promise((resolve, reject) => {
      const path = process.argv[2];
      if (path === undefined) {
        reject(new Error('Cannot load the database'));
        res.write('Cannot load the database');
        res.end();
        return;
      }

      fs.readFile(path, 'utf-8', (err, data) => {
        if (err) {
          reject(new Error('Cannot load the database'));
          res.write('Cannot load the database');
          res.end();
          return;
        }

        // Log the number of students
        const rows = data.split('\n');
        const rowCount = rows.length - 2;
        res.write(`Number of students: ${rowCount}\n`);

        // Log number of students in cs
        let csStudents = 0;
        const csStudentsList = [];
        for (const row of rows) {
          const fields = row.split(',');
          if (fields[3] === 'CS') {
            csStudents += 1;
            const csStudentsName = fields[0];
            csStudentsList.push(csStudentsName);
          }
        }
        res.write(`Number of students in CS: ${csStudents}. List: ${csStudentsList.join(', ')}\n`);

        // Log number of students in swe
        let sweStudents = 0;
        const sweStudentsList = [];
        for (const row of rows) {
          const fields = row.split(',');
          if (fields[3] === 'SWE') {
            sweStudents += 1;
            const sweStudentsName = fields[0];
            sweStudentsList.push(sweStudentsName);
          }
        }
        res.write(`Number of students in SWE: ${sweStudents}. List: ${sweStudentsList.join(', ')}`);
        res.end();
        resolve();
      });
    });
  }

  // If request url is not found
  res.writeHead(404, { 'Content-Type': 'text/plain' });
  res.write('Not Found');
  res.end();
});

app.listen(1245);

module.exports = app;
