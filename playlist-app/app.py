from flask import Flask, redirect, render_template , session


from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"



@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")












@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    session["page"] = "playlist"
    print(session)
    return render_template("playlists.html", playlists=playlists)












@app.route("/playlists/<int:playlist_id>") 
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    # this gives back the specific playlist that you click on
  











@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form is not filled or is not valid: then redirect back to the form
    - if the form is valid , then commit the playlist to the database: then redirect to playlist list
    """

    









@app.route("/songs")
def show_all_songs():
    """Show list of songs."""
    # this works
    songs = Song.query.all()
    session["page"] = "Songs"
    print(session)
    return render_template("songs.html", songs=songs)










@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # this is when you select a particular song and it returns that specific song
















@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:
    if form not filled/valid: return add song form
    if form filled&valid: update table and return to list of songs
    """
    # if form.validate_on_submit():
    #     return redirect("/songs")
    # else:
    #     return redirect("/songs/add")














@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    # THE SOLUTION TO THIS IS IN A HINT IN THE ASSESSMENT INSTRUCTIONS

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    curr_on_playlist = ...
    form.song.choices = ...

    if form.validate_on_submit():

          # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

          return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)
