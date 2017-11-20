__author__ = 'Pavel Kosicin'


def test_create_master_recording(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.search.global_search(name="song_A")
    app.recording.add_artist()
    app.recording.modify()
    app.session.logout()
