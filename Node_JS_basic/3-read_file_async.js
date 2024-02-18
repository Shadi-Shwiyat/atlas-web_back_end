// Function reads data from db and logs
// number of students
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Log the number of students
      const rows = data.split('\n');
      const rowCount = rows.length - 2;
      console.log(`Number of students: ${rowCount}`);

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
      console.log(`Number of students in CS: ${csStudents}. List: ${csStudentsList.join(', ')}`);

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
      console.log(`Number of students in SWE: ${sweStudents}. List: ${sweStudentsList.join(', ')}`);
      resolve();
    });
  });
}

module.exports = countStudents;
