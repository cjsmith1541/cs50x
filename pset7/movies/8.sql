SELECT name FROM movies, people, stars WHERE movies.id = stars.movie_id AND stars.person_id = people.id AND title LIKE 'Toy Story';