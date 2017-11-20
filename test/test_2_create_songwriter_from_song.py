__author__ = 'Pavel Kosicin'
from model.songwriter import Songwriter


def test_create_songwriter(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.song.find(name="song_A")
    app.songwriter.create(Songwriter(name="sw_#1", ipicae="123637911", asap="CD9-63YNK.772ND2Q_R",
        note="Quis non intelligere sua praeterita, coactus sum iterum vivendo experiatur."))
    app.session.logout()
