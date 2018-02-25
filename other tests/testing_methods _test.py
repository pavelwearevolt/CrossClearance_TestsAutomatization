__author__ = 'pavelkosicin'


def test_search_song(app):
    app.song.search_song(query="song_A")


def test_switch_to_tab(app):
    app.navigate.switch_to_tab(tab_name="Songwriters")


def test_edit_deal_tab_songwriters(app):
    
