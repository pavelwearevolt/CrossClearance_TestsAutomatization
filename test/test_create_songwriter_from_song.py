__author__ = 'Pavel Kosicin'
from model.songwriter import Songwriter


def test_create_songwriter(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.song.find(name="song_A")
    app.songwriter.create(Songwriter(name="sw_#1", ipicae="T-123637911-0", asap="CD9-63YNK.772ND2Q_R",
        note="Test note for sonwriter"))
    app.session.logout()
