from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from epdm.schema import Song

engine = create_engine('sqlite:///songs.sqlite3')

Session = sessionmaker(bind=engine)
session = Session()

# def add_song(title=None, author=None, position=None):
#     new_song = Song(title=title, author=author, position=position)
#     session.add(new_song)
#     session.commit()

def get_all_songs():
    #limit 100 4 performance
    songs = session.query(Song).limit(100).all()
    for song in songs:
        print(song.key_id, song.title, song.author, song.position)

def get_song(title):
    song = session.query(Song).filter(Song.title == title).first()
    print(song.key_id, song.title, song.author, song.position)

def get_song_by_key(key_id):
    song = session.query(Song).filter(Song.key_id == key_id).first()
    print(song.key_id, song.title, song.author, song.position)

# def update_title_song(key_id, new_title):
#     song_to_update = session.query(Song).filter(Song.key_id == key_id).first()
#     song_to_update.title = new_title
#     session.commit()
#     get_song_by_key()

def get_all_ranked_top_songs():
    # limit to 1000
    songs = session.query(Song).filter(Song.position == 1).all()
    for song in songs:
        print(song.key_id, song.title, song.author, song.position)

def get_all_ranked_top_songs_distinct():
    songs = (
        session.query(Song)
        .filter(Song.position == 1)
        .group_by(Song.title, Song.author, Song.position)
        .all()
    )
    for song in songs:
        print(song.title, song.author, song.position)


# def delete_song(key_id):
#     #not tested
#     song_to_delete = session.query(Song).filter(Song.key_id == key_id).first()
#     session.delete(song_to_delete)
#     session.commit()

def logout():
    session.close()

def demo():
    get_all_songs()
    get_all_ranked_top_songs()
    get_all_ranked_top_songs_distinct()