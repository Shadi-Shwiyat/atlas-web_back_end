// Express router

const express = require('express');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

const router = express.Router();

// Link the route / to the AppController
router.get('/', AppController.index);

// Link the route /students to StudentsController.getAllStudents
router.get('/students', StudentsController.getAllStudents);

// Link the route /students/:major to StudentsController.getAllStudentsByMajor
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = router;
