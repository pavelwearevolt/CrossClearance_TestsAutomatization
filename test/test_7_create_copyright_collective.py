__author__ = 'Pavel Kosicin'
from model.collective import Collective


def test_create_copyright_collective(app):
    app.collective.create_from_menu_global_search(Collective(name="cc_#1",
        note="Non est aequalis beatitudo tranquillitas."))
    app.collective.create_from_menu_companies(Collective(name="cc_#2",
        note="Nec consectetur affectum ad omne terrenum - passio."))
