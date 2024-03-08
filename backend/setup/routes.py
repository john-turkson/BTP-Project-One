from flask import request, jsonify, Blueprint
from .models import db, User, Playlist, Music
import base64

# App Routes Decorator
app_routes = Blueprint('app_routes', __name__)

# Auth endpoints
@app_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required, '}), 400

    hashed_password = User.generate_hash(data['password'])
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New user created!'})

@app_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not User.verify_hash(data['password'], user.password):
        return jsonify({'message': 'Invalid username or password'}), 400
    return jsonify({'id':user.id,'username':user.username,'message': 'Login successful'})


# User endpoints
@app_routes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username})
    else:
        return jsonify({'message': 'User not found'}), 404

@app_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        data = request.get_json()
        user.username = data['username']
        db.session.commit()
        return jsonify({'message': 'User updated!'})
    else:
        return jsonify({'message': 'User not found'}), 404

@app_routes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted!'})
    else:
        return jsonify({'message': 'User not found'}), 404


@app_routes.route('/user/<int:user_id>/music', methods=['GET'])
def get_user_music(user_id):

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_music = Music.query.filter_by(user_id=user_id).all()
    if not user_music:
        return jsonify({'message': 'No music found for this user'}), 404
    print(user_music)
    music_list = []
    for music in user_music:
        music_data = {
            'id':music.id,
            'title': music.title,
            'artist': music.artist,
            'image': base64.b64encode(music.image).decode('utf-8') if music.image else None,
            'mp3_file': base64.b64encode(music.mp3_file).decode('utf-8') if music.mp3_file else None,
            'like':music.like
        }
        music_list.append(music_data)

    return jsonify({'music': music_list}), 200

@app_routes.route('/user/<int:user_id>/favorits', methods=['GET'])
def get_user_music_favorits(user_id):

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_music = Music.query.filter_by(user_id=user_id).all()
    if not user_music:
        return jsonify({'message': 'No music found for this user'}), 404
    print(user_music)
    music_list = []
    for music in user_music:
        if music.like:
            music_data = {
                'id':music.id,
                'title': music.title,
                'artist': music.artist,
                'image': base64.b64encode(music.image).decode('utf-8') if music.image else None,
                'mp3_file': base64.b64encode(music.mp3_file).decode('utf-8') if music.mp3_file else None,
                'like':music.like
            }

            music_list.append(music_data)

    return jsonify({'music': music_list}), 200

@app_routes.route('/user/<int:user_id>/playlists', methods=['GET'])
def get_user_playlist(user_id):

    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_playlists = Playlist.query.filter_by(user_id=user_id).all()
    if not user_playlists:
        return jsonify({'message': 'No music found for this user'}), 404
    print(user_playlists)
    playlists = []
    for playlist in user_playlists:
        playlist_data = {
            'id':playlist.id,
            'name': playlist.name,
            'image': base64.b64encode(playlist.image).decode('utf-8') if playlist.image else None,
        }
        playlists.append(playlist_data)

    return jsonify({'data': playlists}), 200

# Music endpoints
@app_routes.route('/music', methods=['POST'])
def create_music():
    data = request.form
    print(data)
    user_id = data.get('user_id')
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    new_music = Music(
        title=data['title'],
        artist=data['artist'],
        image=request.files['image'].read() if 'image' in request.files else None,
        mp3_file=request.files['mp3_file'].read() if 'mp3_file' in request.files else None,
        user_id=user.id,
        like=False
    )

    db.session.add(new_music)
    db.session.commit()
    
    return jsonify({'message': 'New music created!'})

@app_routes.route('/music/<int:music_id>/add_fav', methods=['POST'])
def add_to_fav(music_id):
    music = Music.query.get(music_id)

    music.like = True
    
    db.session.commit()
    
    return jsonify({'message': 'Music added to favorits successfully'})

@app_routes.route('/music/<int:music_id>/remove_fav', methods=['POST'])
def remove_from_fav(music_id):
    music = Music.query.get(music_id)

    music.like = False
    
    db.session.commit()
    
    return jsonify({'message': 'Music removed from favorits successfully'})

# Playlist endpoints
@app_routes.route('/playlist', methods=['POST'])
def create_playlist():
    data = request.form
    new_playlist = Playlist(
        name=data['name'], 
        user_id=data['user_id'], 
        image=request.files['image'].read() if 'image' in request.files else None
    )
    db.session.add(new_playlist)
    db.session.commit()
    return jsonify({'message': 'New playlist created!'})

@app_routes.route('/playlist/<int:playlist_id>/add_music', methods=['POST'])
def add_music_to_playlist(playlist_id):
    # Assuming the request contains JSON data with music_id
    request_data = request.get_json()

    # Validate whether music_id is provided
    music_id = request_data.get('music_id')
    if music_id is None:
        return jsonify({'error': 'No music_id provided'}), 400

    # Fetch the playlist object from the database or return a 404 error if not found
    playlist = Playlist.query.get_or_404(playlist_id)

    # Fetch the music object from the database or return a 404 error if not found
    music = Music.query.get_or_404(music_id)

    # Check if the music is already in the playlist
    if music in playlist.musics:
        return jsonify({'error': 'Music is already in the playlist'}), 400

    # Add the music to the playlist
    playlist.musics.append(music)

    try:
        # Commit the changes to the database
        db.session.commit()
        return jsonify({'message': f'Music added to playlist {playlist.name} successfully'}), 200
    except Exception as e:
        # Rollback the session in case of any exception
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    
def get_music_by_playlist_id(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if playlist:
        return playlist.musics
    else:
        return []
    
@app_routes.route('/playlist/<int:playlist_id>/music', methods=['GET'])
def get_music_by_playlist(playlist_id):
    music = get_music_by_playlist_id(playlist_id)
   
    # Create a list of music data for the playlist
    music_list = [{
        'id':track.id,
        'title': track.title,
        'artist': track.artist,
        'image': base64.b64encode(track.image).decode('utf-8') if track.image else None,
        'mp3_file': base64.b64encode(track.mp3_file).decode('utf-8') if track.mp3_file else None,
        'like':track.like
        # Add more attributes as needed
    } for track in music]

    return jsonify({"music":music_list}), 200

@app_routes.route('/playlist/<int:playlist_id>', methods=['DELETE'])
def remove_playlist(playlist_id):
    # Attempt to retrieve the playlist from the database
    playlist = Playlist.query.get(playlist_id)

    # Check if the playlist exists
    if playlist:
        # Delete the playlist from the database
        db.session.delete(playlist)
        db.session.commit()
        return jsonify({'message': 'Playlist deleted successfully'}), 200
    else:
        # Return an error message if the playlist does not exist
        return jsonify({'error': 'Playlist not found'}), 404

@app_routes.route('/music/<int:music_id>', methods=['DELETE'])
def remove_music(music_id):
    # Attempt to retrieve the music track from the database
    music = Music.query.get(music_id)

    # Check if the music track exists
    if music:
        # Delete the music track from the database
        db.session.delete(music)
        db.session.commit()
        return jsonify({'message': 'Music track deleted successfully'}), 200
    else:
        # Return an error message if the music track does not exist
        return jsonify({'error': 'Music track not found'}), 404
