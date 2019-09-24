from app import User, Movie, db

user = User(name='Grey Li')
m1 = Movie(title='Leon', year='2015')
m2 = Movie(title='mahjong', year='1996')
db.session.add(user)
db.session.add(m1)
db.session.add(m2)
db.session.commit()
