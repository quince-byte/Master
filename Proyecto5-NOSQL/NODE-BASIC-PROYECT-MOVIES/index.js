const express = require('express');
const { connect } = require('./utils/db');
// Importo las rutas
const moviesRoutes = require('./routes/movies.routes');

connect();

const PORT = 3000;
const server = express();

server.use(express.json());
server.use(express.urlencoded({ extended: false }));


// Uso el router de movies
server.use('/movies', moviesRoutes);

server.listen(PORT, () => {
  console.log(`Server running in http://localhost:${PORT}`);
});