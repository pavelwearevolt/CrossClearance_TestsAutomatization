__author__ = 'pavelkosicin'
import time


def test_add_copyright_collective(app):
    app.navigate.switch_to_tab(tab_name="Copyright Collective Info")
    app.song.open_copyright_collective_modal_window(songwriter_number="1")
    app.song.close_modal_window_button_close()
    app.song.open_copyright_collective_modal_window(songwriter_number="1")
    app.song.close_modal_window_button_cancel()
    app.song.open_copyright_collective_modal_window(songwriter_number="1")
    app.song.add_copyright_collective(
        collective_name="Association of International Collective Management of Audiovisual Works",
        collective="tt-suggestion.suggestion-0"
        )
    app.song.save_button()
    time.sleep(3)


def test_remove_copyright_collective(app):
    app.song.open_cc_actions_menu(songwriter_number="1")
    app.song.choose_item_in_cc_action_menu(songwriter_number="1", item_number="3")
    app.song.close_modal_window_button_cancel()
    app.song.open_cc_actions_menu(songwriter_number="1")
    app.song.choose_item_in_cc_action_menu(songwriter_number="1", item_number="3")
    app.song.close_modal_window_button_close()
    app.song.open_cc_actions_menu(songwriter_number="1")
    app.song.choose_item_in_cc_action_menu(songwriter_number="1", item_number="3")
    app.song.check_style_of_remove_modal_window(
        element_class_name="ubt0rrA0Vc2i7qRFrCM8X",
        title="Remove copyright collective",
        message="Are you sure you want to remove the copyright collective?"
        )
    app.song.confirm_remove()
    time.sleep(3)

