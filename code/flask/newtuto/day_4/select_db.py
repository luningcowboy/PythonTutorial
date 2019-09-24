from app import db, User, Movie

movie = Movie.query.first()
print(movie.title, movie.year)
print(Movie.query.all())
print(Movie.query.count())
print(Movie.query.get(1))
print(Movie.query.filter_by(title='mahjong').first())
print(Movie.query.filter(Movie.title=='mahjong').first())

movie = Movie.query.get(2)
movie.title = 'WALL-E'
movie.year = '2008'
db.session.commit()
print(Movie.query.get(2).title)

movie = Movie.query.get(1)
db.session.delete(movie)
db.session.commit()

