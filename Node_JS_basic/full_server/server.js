// full_server/server.js

const express = require('express');

const app = express();
const routes = require('./routes');

const PORT = 1245;

// Use the routes defined in full_server/routes/index.js
app.use('/', routes);

// Export the express app
export default app;

// If the server.js file is executed directly, start the server
if (require.main === module) {
  const databaseFilename = process.argv[2];

  if (!databaseFilename) {
    console.error('Please provide the database filename as a command line argument.');
    process.exit(1);
  }

  // Start the server on port 1245
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
    console.log(`Database filename: ${databaseFilename}`);
  });
}
