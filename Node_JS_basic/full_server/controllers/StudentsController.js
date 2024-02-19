// Student class that provides static
// methods for retrieving student db info

const readDatabase = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const data = await readDatabase('./database.csv');
      // Process data and generate response
      let response = 'This is the list of our students\n';

      // Iterate over fields in alphabetic order
      Object.keys(data).sort((a, b) => a.localeCompare(b)).forEach((field) => {
        const numberOfStudents = data[field].length;
        const listOfFirstNames = data[field].join(', ');

        response += `Number of students in ${field}: ${numberOfStudents}. List: ${listOfFirstNames}\n`;
      });

      res.status(200).send(response);
    } catch (error) {
      res.status(500).send(`Cannot load the database: ${error}`);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const data = await readDatabase('./database.csv');
      // Process data for the specified major and generate response
      const response = `List: ${data[major].join(', ')}`;

      res.status(200).send(response);
    } catch (error) {
      res.status(500).send(`Cannot load the database: ${error}`);
    }

    // Default return statement in case of an unexpected code path
    return res.status(500).send('Unexpected error in getAllStudentsByMajor');
  }
}

module.exports = StudentsController;
