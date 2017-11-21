__author__ = 'Pavel Kosicin'
from model.artist import Artist


def test_create_recording_artist(app):
    app.artist.create_from_menu_global_search(Artist(name="ra_#1", note="Tranquillitatis est in vobis. Nec foris quaereret."))
    app.artist.create_from_menu_people(Artist(name="ra_#2", note="Animae suae vir verax est."))
