__author__ = 'Pavel Kosicin'
from model.songwriter import Songwriter


def test_create_songwriter(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.song.find(name="song_A")
    app.songwriter.create_from_song(Songwriter(name="sw_#1", ipicae="123637911", asap="CD9-63YNK.772ND_R",
                                               note="Quis non intelligere sua praeterita, coactus sum iterum vivendo experiatur."))
    app.navigate.menu_global_search()
    app.songwriter.create_menu_global_search(Songwriter(name="sw_#2", ipicae="182570603", asap="QW5E-X07EW.84H9S-0",
        note="Noli olim somniamus futurorum praesentia mentem rede"))
    app.navigate.menu_people()
    app.songwriter.create_menu_people(Songwriter(name="sw_#3", ipicae="500263847", asap="ZF6K-6Q103I.52P9C-I",
        note="Furor iraque peribunt cogitationes ubi oblivionis."))
    app.session.logout()
