from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))


class Artist(Base):
	__tablename__ = 'artist'

	id = Column(Integer, primary_key=True)
	name = Column(String(100), nullable=False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'id': self.id,
			'name': self.name,
			'user': self.user_id
		}

class Video(Base):
	__tablename__ = 'video'

	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	year = Column(Integer, nullable=False)
	artist_id = Column(Integer, ForeignKey('artist.id'))
	artist = relationship(Artist, backref=backref('videos', cascade='delete'))
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'id': self.id,
			'title': self.title,
			'year': self.year,
			'artist': self.artist_id,
			'user': self.user_id
		}


class VideoTrack(Base):
	__tablename__ = 'video_track'

	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	track_num = Column(Integer, nullable=False)
	video_id = Column(Integer, ForeignKey('video.id'))
	video = relationship(Video, backref=backref('tracks', cascade='delete'))

	@property
	def serialize(self):
		"""Return object data in easily serializeable format"""
		return {
			'id': self.id,
			'title': self.title,
			'tracknum': self.track_num,
			'video': self.video_id
		}


#engine = create_engine('sqlite:///concertvideocatalog.db')
engine = create_engine(
	'postgresql+psycopg2://catalog:udacity@localhost/catalog',
	isolation_level='READ UNCOMMITTED'
)

Base.metadata.create_all(engine)
