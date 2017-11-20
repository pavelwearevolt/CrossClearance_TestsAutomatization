__author__ = 'Pavel Kosicin'
from model.label import Label


def test_create_record_label(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.label.create_from_menu_global_search(Label(name="rl_#1", asap="WB86-8RH31.50UTS-J",
        note="Mens autem qui est in festinabat non facere bonum, voluntas in malo reperit."))
    app.label.create_from_menu_companies(Label(name="rl_#2", asap="EE8R-SGQ7H.1T2S0-A",
        note="Repleti stultus est malum, vbi etiam paulatim."))
    app.session.logout()
