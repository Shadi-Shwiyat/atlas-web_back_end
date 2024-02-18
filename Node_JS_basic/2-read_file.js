// Function reads data from db and logs
// number of students
const fs = require('fs');

function countStudents(path) {
  try {
    // Read file synchronously
    const data = fs.readFileSync(path, 'utf-8');

    // Log the number of students
    const rows = data.split('\n');
    const rowCount = rows.length - 1;
    console.log('Number of students:', rowCount);

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
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
