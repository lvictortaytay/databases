"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"
    
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.String)


class Song(db.Model):
    """Song."""
    __tablename__ = "playlist_songs"
    id = db.Column(db.Integer , primary_key = True)
    playlist_id = db.Column(db.Integer , db.ForeignKey("playlists.id"))
    song_id = db.Column(db.Integer , db.ForeignKey("songs.id"))



class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "songs" 
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    artist = db.Column(db.String)





def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
