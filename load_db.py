from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import User, Artist, Base, Video, VideoTrack

#engine = create_engine('sqlite:///concertvideocatalog.db')
engine = create_engine(
	'postgresql+psycopg2://catalog:udacity@localhost/catalog',
	isolation_level='READ UNCOMMITTED'
)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# CREATE USER
user1 = User(
	name="Evie Kuse",
	email="efdfkajadf@gmail.com",
	picture='https://lh3.googleusercontent.com/-2lpb8LPZ4qw/U5Tl7u9qTSI/AAAAAAAABBQ/QR8ffZeHM-0O7uOctdzNHT5h-Ke7ske8gCEwYBhgL/w208-h280-p/Favorites%2B-%2B42.JPG'
)
session.add(user1)
session.commit()

print "Creating users done..."

# CREATE SOME ARTISTS
artist1 = Artist(name="U2", user_id=1)
session.add(artist1)
session.commit()

artist2 = Artist(name="Rolling Stones", user_id=1)
session.add(artist2)
session.commit()

artist3 = Artist(name="Led Zeppelin", user_id=1)
session.add(artist3)
session.commit()

artist4 = Artist(name="Depeche Mode", user_id=1)
session.add(artist4)
session.commit()

artist5 = Artist(name="David Bowie", user_id=1)
session.add(artist5)
session.commit()

artist6 = Artist(name="Billy Joel", user_id=1)
session.add(artist6)
session.commit()

print "Creating artists done..."

# CREATE SOME VIDEOS AND TRACKS FOR VIDEO
video1 = Video(artist_id=1, title="Innocence + Experience: Live in Paris", year=2016, user_id=1)
session.add(video1)
session.commit()

track1 = VideoTrack(title="People Have the Power", track_num=1, video_id=1)
session.add(track1)
session.commit()

track2 = VideoTrack(title="The Miracle (of Joey Ramone)", track_num=2, video_id=1)
session.add(track2)
session.commit()

track3 = VideoTrack(title="Vertigo", track_num=3, video_id=1)
session.add(track3)
session.commit()

track4 = VideoTrack(title="I Will Follow", track_num=4, video_id=1)
session.add(track4)
session.commit()

track5 = VideoTrack(title="Iris (Hold Me Close)", track_num=5, video_id=1)
session.add(track5)
session.commit()

track6 = VideoTrack(title="Cedarwood Road", track_num=6, video_id=1)
session.add(track6)
session.commit()

track7 = VideoTrack(title="Song for Someone", track_num=7, video_id=1)
session.add(track7)
session.commit()

track8 = VideoTrack(title="Sunday Blood Sunday", track_num=8, video_id=1)
session.add(track8)
session.commit()

track9 = VideoTrack(title="Raised By Wolves", track_num=9, video_id=1)
session.add(track9)
session.commit()

track10 = VideoTrack(title="Until the End of the World", track_num=10, video_id=1)
session.add(track10)
session.commit()

track11 = VideoTrack(title="The Fly", track_num=11, video_id=1)
session.add(track11)
session.commit()

track12 = VideoTrack(title="Invisible", track_num=12, video_id=1)
session.add(track12)
session.commit()

track13 = VideoTrack(title="Even Better Than the Real Thing", track_num=13, video_id=1)
session.add(track13)
session.commit()

track14 = VideoTrack(title="Mysterious Ways", track_num=14, video_id=1)
session.add(track14)
session.commit()

track15 = VideoTrack(title="Elevation", track_num=15, video_id=1)
session.add(track15)
session.commit()

track16 = VideoTrack(title="Every Breaking Wave", track_num=16, video_id=1)
session.add(track16)
session.commit()

track17 = VideoTrack(title="October", track_num=17, video_id=1)
session.add(track17)
session.commit()

track18 = VideoTrack(title="Bullet the Blue Sky", track_num=18, video_id=1)
session.add(track18)
session.commit()

track19 = VideoTrack(title="Zooropa", track_num=19, video_id=1)
session.add(track19)
session.commit()

track20 = VideoTrack(title="Where the Streets Have No Name", track_num=20, video_id=1)
session.add(track20)
session.commit()


video2 = Video(artist_id=1, title="Vertigo 2005: Live from Chicago", year=2005, user_id=1)
session.add(video2)
session.commit()

track1 = VideoTrack(title="City of Blinding Lights", track_num=1, video_id=2)
session.add(track1)
session.commit()

track2 = VideoTrack(title="Vertigo", track_num=2, video_id=2)
session.add(track2)
session.commit()

track3 = VideoTrack(title="Elevation", track_num=3, video_id=2)
session.add(track3)
session.commit()

track4 = VideoTrack(title="The Cry/The Electric Co.", track_num=4, video_id=2)
session.add(track4)
session.commit()

track5 = VideoTrack(title="An Cat Dubh/Into the Heart", track_num=5, video_id=2)
session.add(track5)
session.commit()

track6 = VideoTrack(title="Beautiful Day", track_num=6, video_id=2)
session.add(track6)
session.commit()

track7 = VideoTrack(title="New Year's Day", track_num=7, video_id=2)
session.add(track7)
session.commit()

track8 = VideoTrack(title="Miracle Drug", track_num=8, video_id=2)
session.add(track8)
session.commit()

track9 = VideoTrack(title="Sometimes You Can't Make It on Your Own", track_num=9, video_id=2)
session.add(track9)
session.commit()

track10 = VideoTrack(title="Love and Peace or Else", track_num=10, video_id=2)
session.add(track10)
session.commit()

track11 = VideoTrack(title="Sunday Bloody Sunday", track_num=11, video_id=2)
session.add(track11)
session.commit()

track12 = VideoTrack(title="Bullet the Blue Sky", track_num=12, video_id=2)
session.add(track12)
session.commit()

track13 = VideoTrack(title="Running to Stand Still", track_num=13, video_id=2)
session.add(track13)
session.commit()

track14 = VideoTrack(title="Pride (In the Name of Love)", track_num=14, video_id=2)
session.add(track14)
session.commit()

track15 = VideoTrack(title="Where the Streets Have No Name", track_num=15, video_id=2)
session.add(track15)
session.commit()

track16 = VideoTrack(title="One", track_num=16, video_id=2)
session.add(track16)
session.commit()

track17 = VideoTrack(title="Zoo Station", track_num=17, video_id=2)
session.add(track17)
session.commit()

track18 = VideoTrack(title="The Fly", track_num=18, video_id=2)
session.add(track18)
session.commit()

track19 = VideoTrack(title="Mysterious Ways", track_num=19, video_id=2)
session.add(track19)
session.commit()

track20 = VideoTrack(title="All Because of You", track_num=20, video_id=2)
session.add(track20)
session.commit()


video3 = Video(artist_id=1, title="U2 Go Home: Live from Slane Castle, Ireland", year=2001, user_id=1)
session.add(video3)
session.commit()

track1 = VideoTrack(title="Elevation", track_num=1, video_id=3)
session.add(track1)
session.commit()

track2 = VideoTrack(title="Beautiful Day", track_num=2, video_id=3)
session.add(track2)
session.commit()

track3 = VideoTrack(title="Until the End of the World", track_num=3, video_id=3)
session.add(track3)
session.commit()

track4 = VideoTrack(title="New Year's Day", track_num=4, video_id=3)
session.add(track4)
session.commit()

track5 = VideoTrack(title="Out of Control", track_num=5, video_id=3)
session.add(track5)
session.commit()

track6 = VideoTrack(title="Sunday Bloody Sunday", track_num=6, video_id=3)
session.add(track6)
session.commit()

track7 = VideoTrack(title="Wake Up Dead Man", track_num=7, video_id=3)
session.add(track7)
session.commit()

track8 = VideoTrack(title="Stuck In a Moment You Can't Get Out Of", track_num=8, video_id=3)
session.add(track8)
session.commit()

track9 = VideoTrack(title="Kite", track_num=9, video_id=3)
session.add(track9)
session.commit()

track10 = VideoTrack(title="Angel of Harlem", track_num=10, video_id=3)
session.add(track10)
session.commit()


video4 = Video(artist_id=2, title="Shine a Light", year=2008, user_id=1)
session.add(video4)
session.commit()

track1 = VideoTrack(title="Jumpin' Jack Flash", track_num=1, video_id=4)
session.add(track1)
session.commit()

track2 = VideoTrack(title="Shattered", track_num=2, video_id=4)
session.add(track2)
session.commit()

track3 = VideoTrack(title="She Was Hot", track_num=3, video_id=4)
session.add(track3)
session.commit()

track4 = VideoTrack(title="All Down the Line", track_num=4, video_id=4)
session.add(track4)
session.commit()

track5 = VideoTrack(title="Loving Cup", track_num=5, video_id=4)
session.add(track5)
session.commit()

track6 = VideoTrack(title="As Tears Go By", track_num=6, video_id=4)
session.add(track6)
session.commit()

track7 = VideoTrack(title="Some Girls", track_num=7, video_id=4)
session.add(track7)
session.commit()

track8 = VideoTrack(title="Just My Imagination", track_num=8, video_id=4)
session.add(track8)
session.commit()

track9 = VideoTrack(title="Far Away Eyes", track_num=9, video_id=4)
session.add(track9)
session.commit()

track10 = VideoTrack(title="Champagne & Reefer", track_num=10, video_id=4)
session.add(track10)
session.commit()

track11 = VideoTrack(title="Tumbling Dice", track_num=11, video_id=4)
session.add(track11)
session.commit()

track12 = VideoTrack(title="You Got the Silver", track_num=12, video_id=4)
session.add(track12)
session.commit()

track13 = VideoTrack(title="Connection", track_num=13, video_id=4)
session.add(track13)
session.commit()

track14 = VideoTrack(title="Sympathy for the Devil", track_num=14, video_id=4)
session.add(track14)
session.commit()

track15 = VideoTrack(title="Live With Me", track_num=15, video_id=4)
session.add(track15)
session.commit()

track16 = VideoTrack(title="Start Me Up", track_num=16, video_id=4)
session.add(track16)
session.commit()

track17 = VideoTrack(title="Brown Sugar", track_num=17, video_id=4)
session.add(track17)
session.commit()

track18 = VideoTrack(title="(I Can't Get No) Satisfaction", track_num=18, video_id=4)
session.add(track18)
session.commit()

track19 = VideoTrack(title="Shine a Light", track_num=19, video_id=4)
session.add(track19)
session.commit()


video5 = Video(artist_id=2, title="Hyde Park Live", year=2013, user_id=1)
session.add(video5)
session.commit()

track1 = VideoTrack(title="Start Me Up", track_num=1, video_id=5)
session.add(track1)
session.commit()

track2 = VideoTrack(title="It's Only Rock & Roll", track_num=2, video_id=5)
session.add(track2)
session.commit()

track3 = VideoTrack(title="Tumbling Dice", track_num=3, video_id=5)
session.add(track3)
session.commit()

track4 = VideoTrack(title="Emotional Rescue", track_num=4, video_id=5)
session.add(track4)
session.commit()

track5 = VideoTrack(title="Street Fighting Man", track_num=5, video_id=5)
session.add(track5)
session.commit()

track6 = VideoTrack(title="Ruby Tuesday", track_num=6, video_id=5)
session.add(track6)
session.commit()

track7 = VideoTrack(title="Doom and Gloom", track_num=7, video_id=5)
session.add(track7)
session.commit()

track8 = VideoTrack(title="Honky Tonk Women", track_num=8, video_id=5)
session.add(track8)
session.commit()

track9 = VideoTrack(title="Paint It Black", track_num=9, video_id=5)
session.add(track9)
session.commit()

track10 = VideoTrack(title="You Got the Silver", track_num=10, video_id=5)
session.add(track10)
session.commit()


video6 = Video(artist_id=3, title="Celebration Day", year=2007, user_id=1)
session.add(video6)
session.commit()

track1 = VideoTrack(title="Good Times Bad Times", track_num=1, video_id=6)
session.add(track1)
session.commit()

track2 = VideoTrack(title="Ramble On", track_num=2, video_id=6)
session.add(track2)
session.commit()

track3 = VideoTrack(title="Black Dog", track_num=3, video_id=6)
session.add(track3)
session.commit()

track4 = VideoTrack(title="In My Time of Dying", track_num=4, video_id=6)
session.add(track4)
session.commit()

track5 = VideoTrack(title="For Your Life", track_num=5, video_id=6)
session.add(track5)
session.commit()

track6 = VideoTrack(title="Trampled Under Foot", track_num=6, video_id=6)
session.add(track6)
session.commit()

track7 = VideoTrack(title="Nobody's Fault But Mine", track_num=7, video_id=6)
session.add(track7)
session.commit()

track8 = VideoTrack(title="No Quarter", track_num=8, video_id=6)
session.add(track8)
session.commit()

track9 = VideoTrack(title="Since I've Been Loving You", track_num=9, video_id=6)
session.add(track9)
session.commit()

track10 = VideoTrack(title="Dazed and Confused", track_num=10, video_id=6)
session.add(track10)
session.commit()

track11 = VideoTrack(title="Stairway to Heaven", track_num=11, video_id=6)
session.add(track11)
session.commit()

track12 = VideoTrack(title="The Song Remains the Same", track_num=12, video_id=6)
session.add(track12)
session.commit()

track13 = VideoTrack(title="Misty Mountain Hop", track_num=13, video_id=6)
session.add(track13)
session.commit()

track14 = VideoTrack(title="Kashmir", track_num=14, video_id=6)
session.add(track14)
session.commit()

track15 = VideoTrack(title="Whole Lotta Love", track_num=15, video_id=6)
session.add(track15)
session.commit()

track16 = VideoTrack(title="Rock and Roll", track_num=16, video_id=6)
session.add(track16)
session.commit()


video7 = Video(artist_id=3, title="The Song Remains the Same", year=1976, user_id=1)
session.add(video7)
session.commit()

track1 = VideoTrack(title="Bron-Yr-Aur", track_num=1, video_id=7)
session.add(track1)
session.commit()

track2 = VideoTrack(title="Rock and Roll", track_num=2, video_id=7)
session.add(track2)
session.commit()

track3 = VideoTrack(title="Black Dog", track_num=3, video_id=7)
session.add(track3)
session.commit()

track4 = VideoTrack(title="Since I've Been Loving You", track_num=4, video_id=7)
session.add(track4)
session.commit()

track5 = VideoTrack(title="No Quarter", track_num=5, video_id=7)
session.add(track5)
session.commit()


video8 = Video(artist_id=4, title="101", year=1989, user_id=1)
session.add(video8)
session.commit()

track1 = VideoTrack(title="Master and Servant", track_num=1, video_id=8)
session.add(track1)
session.commit()

track2 = VideoTrack(title="Pimpf", track_num=2, video_id=8)
session.add(track2)
session.commit()

track3 = VideoTrack(title="Behind the Wheel", track_num=3, video_id=8)
session.add(track3)
session.commit()

track4 = VideoTrack(title="Strangelove", track_num=4, video_id=8)
session.add(track4)
session.commit()

track5 = VideoTrack(title="Blasphemous Rumours", track_num=5, video_id=8)
session.add(track5)
session.commit()

track6 = VideoTrack(title="Stripped", track_num=6, video_id=8)
session.add(track6)
session.commit()

track7 = VideoTrack(title="Somebody", track_num=7, video_id=8)
session.add(track7)
session.commit()

track8 = VideoTrack(title="Black Celebration", track_num=8, video_id=8)
session.add(track8)
session.commit()

track9 = VideoTrack(title="Pleasure, Little Treasure", track_num=9, video_id=8)
session.add(track9)
session.commit()

track10 = VideoTrack(title="Just Can't Get Enough", track_num=10, video_id=8)
session.add(track10)
session.commit()

track11 = VideoTrack(title="Everything Counts", track_num=10, video_id=8)
session.add(track11)
session.commit()

track12 = VideoTrack(title="Never Let Me Down Again", track_num=10, video_id=8)
session.add(track12)
session.commit()


video9 = Video(artist_id=4, title="One Night in Paris", year=2001, user_id=1)
session.add(video9)
session.commit()

track1 = VideoTrack(title="Dream On (Guitar Intro)", track_num=1, video_id=9)
session.add(track1)
session.commit()

track2 = VideoTrack(title="The Dead of Night", track_num=2, video_id=9)
session.add(track2)
session.commit()

track3 = VideoTrack(title="The Sweetest Condition", track_num=3, video_id=9)
session.add(track3)
session.commit()

track4 = VideoTrack(title="Halo", track_num=4, video_id=9)
session.add(track4)
session.commit()

track5 = VideoTrack(title="Walking In My Shoes", track_num=5, video_id=9)
session.add(track5)
session.commit()

track6 = VideoTrack(title="Dream On", track_num=6, video_id=9)
session.add(track6)
session.commit()

track7 = VideoTrack(title="When the Body Speaks", track_num=7, video_id=9)
session.add(track7)
session.commit()

track8 = VideoTrack(title="Waiting for the Night", track_num=8, video_id=9)
session.add(track8)
session.commit()

track9 = VideoTrack(title="It Doesn't Matter Two", track_num=9, video_id=9)
session.add(track9)
session.commit()

track10 = VideoTrack(title="Breathe", track_num=10, video_id=9)
session.add(track10)
session.commit()


video10 = Video(artist_id=4, title="Live in Berlin", year=2014, user_id=1)
session.add(video10)
session.commit()

video11 = Video(artist_id=5, title="Ziggy Stardust and the Spiders from Mars", year=1973, user_id=1)
session.add(video11)
session.commit()

track1 = VideoTrack(title="Opening Credits/Intro", track_num=1, video_id=11)
session.add(track1)
session.commit()

track2 = VideoTrack(title="Hang On to Yourself", track_num=2, video_id=11)
session.add(track2)
session.commit()

track3 = VideoTrack(title="Ziggy Stardust", track_num=3, video_id=11)
session.add(track3)
session.commit()

track4 = VideoTrack(title="Watch That Man", track_num=4, video_id=11)
session.add(track4)
session.commit()

track5 = VideoTrack(title="Wild Eyed Boy from Freecloud", track_num=5, video_id=11)
session.add(track5)
session.commit()

track6 = VideoTrack(title="All the Young Dudes", track_num=6, video_id=11)
session.add(track6)
session.commit()


video12 = Video(artist_id=5, title="A Reality Tour", year=2004, user_id=1)
session.add(video12)
session.commit()

track1 = VideoTrack(title="Concert Introduction", track_num=1, video_id=12)
session.add(track1)
session.commit()

track2 = VideoTrack(title="Rebel Rebel", track_num=2, video_id=12)
session.add(track2)
session.commit()

track3 = VideoTrack(title="New Killer Star", track_num=3, video_id=12)
session.add(track3)
session.commit()

track4 = VideoTrack(title="Reality", track_num=4, video_id=12)
session.add(track4)
session.commit()

track5 = VideoTrack(title="Fame", track_num=5, video_id=12)
session.add(track5)
session.commit()

track6 = VideoTrack(title="Cactus", track_num=6, video_id=12)
session.add(track6)
session.commit()

track7 = VideoTrack(title="Sister Midnight", track_num=7, video_id=12)
session.add(track7)
session.commit()

track8 = VideoTrack(title="Afraid", track_num=8, video_id=12)
session.add(track8)
session.commit()

track9 = VideoTrack(title="All the Young Dudes", track_num=9, video_id=12)
session.add(track9)
session.commit()

track10 = VideoTrack(title="Be My Wife", track_num=10, video_id=12)
session.add(track10)
session.commit()


video13 = Video(artist_id=6, title="Live at Shea Stadium: The Concert", year=2013, user_id=1)
session.add(video13)
session.commit()

track1 = VideoTrack(title="Prelude/Angry Young Man", track_num=1, video_id=13)
session.add(track1)
session.commit()

track2 = VideoTrack(title="My Life", track_num=2, video_id=13)
session.add(track2)
session.commit()

track3 = VideoTrack(title="Summer, Highland Falls", track_num=3, video_id=13)
session.add(track3)
session.commit()

track4 = VideoTrack(title="The Entertainer", track_num=4, video_id=13)
session.add(track4)
session.commit()

track5 = VideoTrack(title="Everybody Loves You Now", track_num=5, video_id=13)
session.add(track5)
session.commit()

track6 = VideoTrack(title="Zanzibar", track_num=6, video_id=13)
session.add(track6)
session.commit()

track7 = VideoTrack(title="New York State of Mind", track_num=7, video_id=13)
session.add(track7)
session.commit()

track8 = VideoTrack(title="Allentown", track_num=8, video_id=13)
session.add(track8)
session.commit()

track9 = VideoTrack(title="The Ballad of Billy the Kid", track_num=9, video_id=13)
session.add(track9)
session.commit()

track10 = VideoTrack(title="She's Always a Woman", track_num=10, video_id=13)
session.add(track10)
session.commit()


print "Creating videos and tracks done..."
