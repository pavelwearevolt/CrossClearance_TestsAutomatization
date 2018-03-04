__author__ = 'pavelkosicin'
import time
from model.note import Note


def test_search_song(app):
    app.song.search_song(query="song_B")


def test_check_fields_value_default(app):
    app.song.check_fields_value_default(name="song_A")







