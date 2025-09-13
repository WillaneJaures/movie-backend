from database import SessionLocal
from models import Movie, Rating, Tag, Link


db = SessionLocal()
#tester la recuperation des films

movies = db.query(Movie).limit(5).all()
for movie in movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Genre: {movie.genres}")


#recuperer tous les films du genre action
action_movies = db.query(Movie).filter(Movie.genres.like('%Action%')).limit(5).all()
print("\nAction Movies:")
for movie in action_movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Genre: {movie.genres}")


#tester la recuperations des evaluations
ratings = db.query(Rating).limit(5).all()
print("\nRatings:")
for rating in ratings:
    print(f"User ID: {rating.userId}, Movie ID: {rating.movieId}, Rating: {rating.rating}, Timestamp: {rating.timestamp}")

#recuperer les filmes avec une note superieure ou egale a 4.5
high_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating, Movie.movieId == Rating.movieId)
    .filter(Rating.rating >= 4.5)
    .limit(5)
    .all()
)
print("\nHigh Rated Movies (Rating >= 4):")
for title, rating in high_rated_movies:
    print(f"Title: {title}, Rating: {rating}")



#tester la recuperation des tags
tags = db.query(Tag).limit(5).all()
print("\nTags:")
for tag in tags:
    print(f"User ID: {tag.userId}, Movie ID: {tag.movieId}, Tag: {tag.tag}, Timestamp: {tag.timestamp}")


#tester la recuperation des links

links = db.query(Link).limit(5).all()
print("\nLinks:")
for link in links:
    print(f"Movie ID: {link.movieId}, IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")


#fermer la session
db.close()