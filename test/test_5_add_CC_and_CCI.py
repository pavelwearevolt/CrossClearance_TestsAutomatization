__author__ = 'pavelkosicin'
import time


def test_add_copyright_collective(app):
    app.navigate.switch_to_tab(tab_name="Copyright Collective Info")
    app.song.open_copyright_collective_modal_window(songwriter_number="1")
    app.song.close_modal_window_button_close()
    app.song.open_copyright_collective_modal_window(songwriter_number="1")
    app.song.close_directive_modal_window_button_cancel()
    app.song.open_copyright_collective_modal_window(songwriter_number="1")
    app.song.add_copyright_collective(
        collective_name="Association of International Collective Management of Audiovisual Works",
        collective="tt-suggestion.suggestion-0"
        )
    app.song.save_button()
    time.sleep(3)
