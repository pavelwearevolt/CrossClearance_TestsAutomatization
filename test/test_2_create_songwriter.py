__author__ = 'Pavel Kosicin'
from model.songwriter import Songwriter


def test_create_songwriter(app):
    app.songwriter.create_from_song(Songwriter(name="sw_#1", ipicae="Q-123637911-0", asap="CD9-63YNK.772ND_R",
        note="Quis non intelligere sua praeterita, coactus sum iterum vivendo experiatur."))
    app.songwriter.create_menu_global_search(Songwriter(name="sw_#2", ipicae="B-182570603-6", asap="QW5E-X07EW.84H9S-0",
        note="Noli olim somniamus futurorum praesentia mentem rede"))
