__author__ = 'Pavel Kosicin'
from model.pubilisher import Publisher


def create_publisher(app):
    app.navigate.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.publisher.create_from_song(Publisher(name="pb_#1", ipicae="173265490", asap="GF43-T30JT.P6WQ4-Q",
        note="Non causat aliam rationem quid patiaris."))
    app.navigate.logout()
