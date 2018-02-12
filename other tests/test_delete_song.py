__author__ = 'Pavel Kosicin'


def test_create_song(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.song.find(name="song_A")
    app.song.delete()
    app.session.logout()
