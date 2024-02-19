// full_server/server.js

const express = require('express');

const app = express();
const routes = require('./routes');

const PORT = 1245;

app.use('/', routes);

export default app;

if (process.argv[1].includes('server.js')) {
  app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  });
}
