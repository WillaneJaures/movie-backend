from database import SessionLocal
from models import Movie, Rating, Tag, Link


db = SessionLocal()
movies = db.query(Movie).limit(10).all()

for movie in movies:
    print(f"ID : {movie.movieId}, Titre : {movie.title}, Genres : {movie.genres}")

else:
    print("No movies found.")

#  Récupérer les films du genre Action
action_movies = db.query(Movie).filter(Movie.genres.like("%Action%")).limit(5).all()

for movie in action_movies:
    print(f"ID : {movie.movieId}, Titre : {movie.title}, Genres : {movie.genres}")


# Tester la récupération de quelques évaluations (ratings)
Ratings = db.query(Rating).limit(5).all()

for rating in Ratings:
    print(f"User ID : {rating.userId}, Movie ID : {rating.movieId}, Rating : {rating.rating}, Timestamp : {rating.timestamp}")


# Films avec une note supérieure ou égale à 4
# Query should select the movie title and the rating value so we get tuples
high_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4)
    .limit(5)
    .all()
)

for title, rating in high_rated_movies:
    print(title, rating)


# Récupération des tags associés aux films
tags = db.query(Tag).limit(5).all()

for tag in tags:  
    print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}, Timestamp : {tag.timestamp}")
# Tester la classe Link
links = db.query(Link).limit(5).all()

for link in links:
    print(f"Movie ID : {link.movieId}, IMDB ID : {link.imdbId}, TMDB ID : {link.tmdbId}")
# fermer la Session
db.close()
