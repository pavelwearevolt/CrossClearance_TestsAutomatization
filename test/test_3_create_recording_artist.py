__author__ = 'pavelkosicin'
from model.artist import Artist


def test_create_recording_artist(app):
    app.artist.create_recording_artist(Artist(name="ra_#1", note="Tranquillitatis est in vobis. Nec foris quaereret."))

