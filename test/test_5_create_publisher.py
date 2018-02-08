__author__ = 'pavelkosicin'
from model.publisher import Publisher


def test_create_publisher(app):
    app.publisher.create_from_song(Publisher(name="pb_#1", ipicae="R-173265490-1", asap="GF43-T30JT.P6WQ4-Q",
        note="Non causat aliam rationem quid patiaris."))
    app.publisher.create_recording_artist(Publisher(name="pb_#2", ipicae="H-297613405-6", asap="AS1Y-73S50.W62TQ-X",
                                                    note="Erga omnes homines - sit vera religio."))
