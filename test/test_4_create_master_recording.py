__author__ = 'Pavel Kosicin'


def test_create_master_recording(app):
    app.recording.add_artist()
    app.recording.modify()
