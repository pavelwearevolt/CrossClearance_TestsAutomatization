__author__ = 'Pavel Kosicin'
from model.recording import Recording
from model.recording import Modify


def test_create_master_recording(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.song.find(name="song_A")
    app.recording.add_artist(Recording(artist_name="ra_#1", recording_name="mr_#1"))
    app.recording.find(name="mr_#1")
    app.recording.modify(Modify(version="test_version", isrc="QW-RE1-42-05634", asap="D7J_W9MZ38.5BA_L", note="Test note for master recording"))
    app.session.logout()
