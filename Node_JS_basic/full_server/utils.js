// Reads a database asynchronously,
// returns a promise

const fs = require('fs');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        // Split the CSV data into rows
        const rows = data.split('\n').map((row) => row.trim());

        // Extract headers and remove empty rows
        const headers = rows[0].split(',').map((header) => header.trim());
        const records = rows.slice(1).filter((row) => row !== '').map((row) => row.split(','));

        // Group students by field and add firstname to list
        const result = {};
        records.forEach((record) => {
          const student = {};
          headers.forEach((header, index) => {
            student[header] = record[index].trim();
          });

          const { firstname, field } = student;
          if (!result[field]) {
            result[field] = [];
          }
          result[field].push(firstname);
        });

        resolve(result);
      }
    });
  });
}

module.exports = readDatabase;
