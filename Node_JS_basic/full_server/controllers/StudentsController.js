// Student class that provides static
// methods for retrieving student db info

const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(request, response) {
    try {
      const filepath = 'path/to/your/database/file'; // Replace with the actual path
      const data = readDatabase(filepath);
      if (!data) {
        throw new Error('Cannot load the database');
      }

      const keys = Object.keys(data);
      const fields = keys.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

      response.status(200).send('This is the list of our students\n');

      fields.forEach((field) => {
        const studentsInField = data[field].length;
        const studentList = data[field].sort().join(', ');
        response.write(`Number of students in ${field}: ${studentsInField}. List: ${studentList}\n`);
      });

      response.end();
    } catch (error) {
      response.status(500).send(`Cannot load the database. Error: ${error.message}`);
    }
  }

  static getAllStudentsByMajor(request, response) {
    try {
      const filepath = 'path/to/your/database/file'; // Replace with the actual path
      const data = readDatabase(filepath);
      if (!data) {
        throw new Error('Cannot load the database');
      }

      const { major } = request.query;
      if (major && (major.toUpperCase() === 'CS' || major.toUpperCase() === 'SWE')) {
        const studentsInMajor = data[major.toUpperCase()].sort().join(', ');
        response.status(200).send(`List: ${studentsInMajor}\n`);
      } else {
        response.status(500).send('Major parameter must be CS or SWE');
      }
    } catch (error) {
      response.status(500).send(`Cannot load the database. Error: ${error.message}`);
    }
  }
}

module.exports = StudentsController;
