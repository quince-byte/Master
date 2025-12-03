const express = require('express');
const Movie = require('../models/Movie'); // Importo el modelo subiendo un nivel

const router = express.Router();

// Obtengo todas las películas
router.get('/', async (req, res) => {
	try {
		const movies = await Movie.find();
		return res.status(200).json(movies);
	} catch (err) {
		return res.status(500).json(err);
	}
});

// Obtengo por ID
router.get('/id/:id', async (req, res) => {
	const id = req.params.id;
	try {
		const movie = await Movie.findById(id);
		if (movie) {
			return res.status(200).json(movie);
		} else {
			return res.status(404).json('No movie found by this id');
		}
	} catch (err) {
		return res.status(500).json(err);
	}
});

// Obtengo por Título
router.get('/title/:title', async (req, res) => {
	const { title } = req.params;

	try {
		const movieByTitle = await Movie.find({ title });
		return res.status(200).json(movieByTitle);
	} catch (err) {
		return res.status(500).json(err);
	}
});

// Obtengo por Género
router.get('/genre/:genre', async (req, res) => {
	const { genre } = req.params;

	try {
		const movieByGenre = await Movie.find({ genre });
		return res.status(200).json(movieByGenre);
	} catch (err) {
		return res.status(500).json(err);
	}
});

// Obtengo por Año
router.get('/year/:year', async (req, res) => {
	const { year } = req.params;

	try {
		const movieByYear = await Movie.find({ year: { $gt: year } });
		return res.status(200).json(movieByYear);
	} catch (err) {
		return res.status(500).json(err);
	}
});

router.post('/', async (req, res) => {
    try {
        // Creo una instancia del modelo con los datos que vienen en el body
        const newMovie = new Movie(req.body);
        // Guardo en base de datos
        const createdMovie = await newMovie.save();
        return res.status(201).json(createdMovie);
    } catch (err) {
        return res.status(500).json(err);
    }
});

// Modificar una película por ID
router.put('/id/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const putMovie = new Movie(req.body);
        putMovie._id = id;
        const updatedMovie = await Movie.findByIdAndUpdate(id, putMovie, { new: true });

        if (!updatedMovie) {
            return res.status(404).json({ message: 'Movie not found' });
        }
        return res.status(200).json(updatedMovie);
    } catch (err) {
        return res.status(500).json(err);
    }
});

// Eliminar una película por ID
router.delete('/id/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const deletedMovie = await Movie.findByIdAndDelete(id);

        if (!deletedMovie) {
            return res.status(404).json({ message: 'Movie not found' });
        }
        return res.status(200).json(deletedMovie);
    } catch (err) {
        return res.status(500).json(err);
    }
});

module.exports = router;