__author__ = 'pavelkosicin'


def test_create_master_recording(app):
    app.recording.add_artist()
    app.recording.modify()
