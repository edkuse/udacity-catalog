from flask import (Flask,
				   render_template,
				   request,
				   redirect,
				   jsonify,
				   url_for,
				   flash,
				   make_response)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Artist, Video, VideoTrack
from flask import session as login_session
from oauth2client import client, crypt
from functools import wraps
import json
import random
import requests
import string

app = Flask(__name__)

CLIENT_ID = json.loads(
	open('oauth_google.json', 'r').read()
)['web']['client_id']

# CONNECT TO DB AND CREATE DB SESSION
engine = create_engine('sqlite:///concertvideocatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog/')
def catalog():
	# PULL AND COMPILE COMPLETE LIST OF ALL ARTISTS AND THEIR VIDEOS FROM DB
	v = []
	a = []

	# QUERY JOINS Video AND Artist TABLES - SORT BY ARTIST THEN VIDEO TITLE
	for artist, video in session.query(Artist, Video).outerjoin(Video).order_by(Artist.name, Video.title):
		_artist = artist.serialize
		_video = video.serialize if video else None

		if _artist not in a:
			a.append(_artist)

			_artist2 = dict(_artist)
			_artist2.update({'videos': []})

			v.append(_artist2)

		if _video:
			v[len(v)-1]['videos'].append(_video)
	
	return render_template(
		'catalog.html',
		artists=a,
		videos=v,
		logged_in=True if 'user' in login_session else False
	)


@app.route('/video/tracks', methods=['POST'])
def get_tracks():
	video_id = request.form.get('id', 0)

	# GET TRACK LISTING FOR CONCERT VIDEO AND RETURN HTML FOR AJAX REQUEST
	tracks = session.query(VideoTrack).filter(VideoTrack.video_id==video_id).order_by(VideoTrack.track_num)
	video = session.query(Video).filter(Video.id==video_id).one()
	artist = session.query(Artist).filter(Artist.id==video.artist_id).one()

	return render_template(
		'tracks.html',
		tracks=tracks,
		video=video,
		artist=artist,
		logged_in=True if 'user' in login_session else False
	)


@app.route('/login/')
def login():
	# GENERATE RANDOM 32 CHARACTER ANTI-FORGERY STATE TOKEN
	state = ''.join(
		random.choice(string.ascii_uppercase + string.digits) for x in xrange(32)
	)

	# STORE VALUE IN USER SESSION
	login_session['state'] = state

	return render_template(
		'login.html', state=state
	)


@app.route('/google', methods=['POST'])
def gconnect():
	token = request.form.get('token')
	state = request.form.get('state')

	# VALIDATE STATE TOKEN GENERATED IN login()
	if state != login_session['state']:
		response = make_response(json.dumps('Invalid STATE parameter value'), 401)
		response.headers['Content-Type'] = 'application/json'
		
		return response

	# VALIDATE GOOGLE ID TOKEN USING tokeninfo ENDPOINT
	result = requests.post(
		'https://www.googleapis.com/oauth2/v3/tokeninfo',
		data={'id_token': token}
	)

	# IF ERROR RETURNED, ABORT AND SEND BACK 500 RESPONSE
	if result.status_code != requests.codes.ok:
		response = make_response(json.dumps('Token from Google could not be validated.'), 500)
		response.headers['Content-Type'] = 'application/json'

		return response

	profile = result.json()

	# VERIFY THAT aud VALUE FROM GOOGLE RESPONSE EQUALS CLIENT ID
	if profile['aud'] != CLIENT_ID:
		response = make_response(json.dumps("Token's client ID does not match app."), 401)
		response.headers['Content-Type'] = 'application/json'

		return response

	# STORE SESSION VARIABLES
	login_session['name'] = profile['name']
	login_session['picture'] = profile['picture']
	login_session['email'] = profile['email']
	login_session['provider'] = 'google'
	login_session['google_token'] = token

	# CHECK IF USER ALREADY EXISTS, ELSE CREATE
	user = get_user(profile["email"])

	if not user:
		user = create_user(login_session)

	login_session['user'] = user

	flash("You are now logged in as %s" % login_session['name'], "success")

	return jsonify(profile)


@app.route('/logout/')
def logout():
	del login_session['google_token']
	del login_session['provider']
	del login_session['name']
	del login_session['email']
	del login_session['picture']
	del login_session['user']

	flash('You have been logged out of application.', 'success')
	return redirect(url_for('catalog'))


#
# LOGIN DECORATOR
#
def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if 'user' not in login_session:
			return redirect('/login')
		return f(*args, **kwargs)
	return decorated_function


#
# ADD NEW ARTIST (LOGIN REQUIRED)
#
@app.route('/artist/add', methods=['POST'])
@login_required
def artist_add():
	name = request.form.get('artist')

	if name:
		a = Artist(name=name, user_id=login_session['user'])
		session.add(a)
		session.commit()

		flash("Artist '{}' has been added!".format(name), 'success')

	else:
		flash("Oops.  Artist '{}' could not be added!".format(name), 'error')

	return redirect(url_for('catalog'))


#
# UPDATE ARTIST (LOGIN REQUIRED)
#
@app.route('/artist/edit', methods=['POST'])
@login_required
def artist_edit():
	artist_id = request.form.get('id')
	name = request.form.get('artist')

	# NOTE: LOGGED IN USERS CAN UPDATE ANY ARTIST, EVEN ONES THEY DID NOT CREATE

	if artist_id and name:
		a = session.query(Artist).filter_by(id=artist_id).one()
		a.name = name
		session.commit()

		flash("Artist has been updated!", 'success')

	else:
		flash("Oops.  Artist update could not be saved!", 'error')

	return redirect(url_for('catalog'))


#
# DELETE ARTIST (LOGIN REQUIRED)
#
@app.route('/artist/delete', methods=['POST'])
@login_required
def artist_delete():
	artist_id = request.form.get('id')

	if artist_id:
		a = session.query(Artist).filter_by(id=artist_id).one()

		if login_session['user'] != a.user_id:
			return jsonify({'result': False, 'error': 'You are not authorized to remove artist!'})
		else:
			session.delete(a)
			session.commit()
	else:
		return jsonify({'result': False, 'error': 'Artist could not be removed.'})

	return jsonify({'result': True})


#
# ADD NEW VIDEO (LOGIN REQUIRED)
#
@app.route('/video/add', methods=['POST'])
@login_required
def video_add():
	artist = request.form.get('artistid')
	title = request.form.get('video')
	year = request.form.get('year')

	if artist and title and year:
		v = Video(title=title, year=year, artist_id=artist, user_id=login_session['user'])
		session.add(v)
		session.commit()

		flash("Concert Video '{0} ({1})' has been added!".format(title, year), 'success')

	else:
		flash("Oops.  Concert Video '{}' could not be added!".format(title), 'error')

	return redirect("{0}#artist{1}".format(url_for('catalog'), artist))


#
# UPDATE VIDEO (LOGIN REQUIRED)
#
@app.route('/video/edit', methods=['POST'])
@login_required
def video_edit():
	video_id = request.form.get('id')
	title = request.form.get('video')
	year = request.form.get('year')
	artist = request.form.get('artistid')

	# NOTE: LOGGED IN USERS CAN EDIT OTHER USER'S VIDEOS

	if video_id and title and year:
		v = session.query(Video).filter_by(id=video_id).one()
		v.title = title
		v.year = year
		session.commit()

		flash("Concert Video has been updated!", 'success')

	else:
		flash("Oops.  Video update could not be saved!", 'error')

	return redirect("{0}#artist{1}".format(url_for('catalog'), artist))


#
# DELETE VIDEO (LOGIN REQUIRED)
#
@app.route('/video/delete', methods=['POST'])
@login_required
def video_delete():
	video_id = request.form.get('id')

	if video_id:
		v = session.query(Video).filter_by(id=video_id).one()

		if login_session['user'] != v.user_id:
			return jsonify({'result': False, 'error': 'You are not authorized to remove video!'})
		else:
			session.delete(v)
			session.commit()

	else:
		return jsonify({'result': False, 'error': 'Video could not be removed.'})

	return jsonify({'result': True})


#
# ADD NEW TRACK (LOGIN REQUIRED)
#
@app.route('/track/add', methods=['POST'])
@login_required
def track_add():
	title = request.form.get('tracktitle')
	tracknum = request.form.get('tracknum')
	video = request.form.get('videoid')
	artist = request.form.get('artistid')

	if title and tracknum and video:
		t = VideoTrack(title=title, track_num=tracknum, video_id=video)
		session.add(t)
		session.commit()

		flash("Track '{0} - {1}' has been added!".format(tracknum, title), 'success')

	else:
		flash("Oops.  Track '{}' could not be added!".format(title), 'error')

	return redirect("{0}#artist{1}".format(url_for('catalog'), artist))


#
# UPDATE TRACK (LOGIN REQUIRED)
#
@app.route('/track/edit', methods=['POST'])
@login_required
def track_edit():
	track_id = request.form.get('id')
	title = request.form.get('tracktitle')
	num = request.form.get('tracknum')
	artist = request.form.get('artistid')

	# NOTE: LOGGED IN USERS CAN UPDATE OTHER USER'S VIDEO TRACKS

	if track_id and title and num:
		t = session.query(VideoTrack).filter_by(id=track_id).one()
		t.title = title
		t.track_num = num
		session.commit()

		flash("Track has been updated!", 'success')
	else:
		flash("Oops. Track could not be saved!", 'error')

	return redirect("{0}#artist{1}".format(url_for('catalog'), artist))


#
# DELETE TRACK (LOGIN REQUIRED)
#
@app.route('/track/delete', methods=['POST'])
@login_required
def track_delete():
	track_id = request.form.get('id')

	# NOTE: LOGGED IN USERS CAN DELETE ANY USER'S VIDEO TRACKS

	if track_id:
		t = session.query(VideoTrack).filter_by(id=track_id).one()
		session.delete(t)
		session.commit()

	else:
		return jsonify({'result': False, 'error': 'Track could not be removed.'})

	return jsonify({'result': True})


#
# JSON ENDPOINTS
#
@app.route('/artist/json')
def artist_json():
	artists = session.query(Artist).all()

	return jsonify(artists=[a.serialize for a in artists])


@app.route('/video/json')
def video_json():
	videos = session.query(Video).all()

	return jsonify(videos=[v.serialize for v in videos])


@app.route('/artist/<int:artist_id>/video/json')
def artist_video_json(artist_id):
	artist = session.query(Artist).filter_by(id=artist_id).one()
	videos = session.query(Video).filter_by(artist_id=artist_id).all()

	return jsonify(Videos=[v.serialize for v in videos])


@app.route('/video/<int:video_id>/tracks/json')
def video_tracks_json(video_id):
	tracks = session.query(VideoTrack).filter_by(video_id=video_id).all()

	return jsonify(Tracks=[t.serialize for t in tracks])


def get_user(email):
	user = session.query(User).filter_by(email=email)

	return user.one().id if user.count() else None


def create_user(data):
	u = User(
		name=data['name'],
		email=data['email'],
		picture=data['picture']
	)
	session.add(u)
	session.commit()

	user = session.query(User).filter_by(email=data['email']).one()

	return user.id


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=8000)
	