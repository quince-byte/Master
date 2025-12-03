function averageMovieDuration(movies) {
  let totalDuration = 0;
  for (const movie of movies) {
    totalDuration += movie.duration;
  }
  return totalDuration / movies.length;
}