__author__ = 'Pavel Kosicin'
from model.publisher import Publisher


def test_create_publisher(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.publisher.create_from_song(Publisher(name="pb_#1", ipicae="173265490", asap="GF43-T30JT.P6WQ4-Q",
        note="Non causat aliam rationem quid patiaris."))
    app.publisher.create_from_menu_global_search(Publisher(name="pb_#2", ipicae="297613405", asap="AS1Y-73S50.W62TQ-X",
        note="Erga omnes homines - sit vera religio."))
    app.publisher.create_from_menu_companies(Publisher(name="pb_#3", ipicae="398125607", asap="NVD6-SI60C.7UG1J-Z",
        note="Non esse augendam"))
    app.session.logout()
