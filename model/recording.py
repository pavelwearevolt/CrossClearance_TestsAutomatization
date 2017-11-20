__author__ = 'Pavel Kosicin'


class Recording:

    def __init__(self, artist_name, recording_name):
        self.artist_name = artist_name
        self.recording_name = recording_name


class Modify:

    def __init__(self, version, isrc, asap, note):
        self.version = version
        self.isrc = isrc
        self.asap = asap
        self.note = note
