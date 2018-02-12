__author__ = 'pavelkosicin'
from model.collective import Collective


def test_create_copyright_collective(app):
    app.collective.create_copyright_collective(Collective(name="cc_#1",
                                                      note="Non est aequalis beatitudo tranquillitas."))
