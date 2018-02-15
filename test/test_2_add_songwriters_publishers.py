__author__ = 'pavelkosicin'


def test_search_song(app):
    app.song.search_song(query="song_A")


def test_switch_to_tab_songwriters(app):
    app.navigate.tab_songwriters()


def test_check_empty_tab_songwriters(app):
    app.songwriter.check_alert_info(alert_text="There is not one Songwriter for this song")


def create_songwriter_in_the_song(app):
    app.songwrier.create_from_song(name="person_songwriter_#1")
