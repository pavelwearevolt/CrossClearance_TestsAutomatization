__author__ = 'pavelkosicin'


def test_search_song(app):
    app.song.search_song(query="song_A")


def test_switch_to_tab_songwriters(app):
    app.navigate.switch_to_tab(tab_name="Songwriters")


def test_add_share(app):
    app.song.open_dropdown_menu()
    app.song.open_modal_window(text="Add share")
    app.song.close_modal_window_button_close()
    app.song.open_dropdown_menu()
    app.song.open_modal_window(text="Add share")
    app.song.close_modal_window_button_cancel()
    app.song.open_dropdown_menu()
    app.song.open_modal_window(text="Add share")
    app.song.fill_share_form(
        territory="world",
        territory_locator="tt-suggestion.suggestion-0",
        percentage="100"
        )
