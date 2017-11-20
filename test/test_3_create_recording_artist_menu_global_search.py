__author__ = 'Pavel Kosicin'
from model.artist import Artist


def test_create_recording_artist(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.artist.create(Artist(name="ra_#1", note="Tranquillitatis est in vobis. Nec foris quaereret."))
    app.session.logout()
