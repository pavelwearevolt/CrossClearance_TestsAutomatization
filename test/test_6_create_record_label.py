__author__ = 'Pavel Kosicin'
from model.label import Label


def test_create_record_label(app):
    app.label.create_recording_artist(Label(name="rl_#1", asap="WB86-8RH31.50UTS-J",
                                            note="Mens autem qui est in festinabat non facere bonum, voluntas in malo reperit."))
