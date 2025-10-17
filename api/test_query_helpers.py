
from database import SessionLocal
from query_helpers import *

# Créer une session
db = SessionLocal()

movie = get_movie(db, movie_id=1)
print(f"Titre: {movie.title}, Genres: {movie.genres}")
# Tester la récupération de films
movies = get_movies(db, limit=5, genre="Comedy")

for movie in movies:
    print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")


# Fermer la session
db.close()