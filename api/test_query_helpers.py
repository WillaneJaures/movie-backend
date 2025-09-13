from database import SessionLocal
from query_helpers import *



db = SessionLocal()

# --- Films ---
print("Testing get_movie:")
movie = get_movies(db, limit=5)
for movie in movie:
    print(f"ID: {movie.movieId}, movie: {movie.title}, genres: {movie.genres}")

db.close()