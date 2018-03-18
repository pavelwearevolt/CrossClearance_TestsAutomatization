__author__ = 'pavelkosicin'
import time


def test_add_directives(app):
    app.navigate.switch_to_tab(tab_name="Directives")
    # songwriter_number - the songwriter's serial number in which the directive is created
    app.song.open_add_directives_modal_window(songwriter_number="2")
    app.song.close_modal_window_button_close()
    app.song.open_add_directives_modal_window(songwriter_number="2")
    app.song.close_directive_modal_window_button_cancel()
    app.song.open_add_directives_modal_window(songwriter_number="2")
    app.song.fill_territory_field(
        territory_field_id="license_origin_select_search",
        territory="world",
        territory_locator="tt-suggestion.suggestion-0"
        )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="1"
        )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="2"
        )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="3"
        )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="5"
        )
    app.song.choose_media_types_directives(
        field_id="media_type_select",
        item_number="4"
        )
    app.song.fill_percentage_field(
        percentage_field_id="payment-percentage-input",
        percentage="50"
        )
    app.song.save_button()
    time.sleep(3)


def test_remove_directive(app):
    # songwriter_number - sequence number of songwriter
    # directive_number - sequence number of directive in current songwriter
    app.song.open_directive_actions_menu(
        songwriter_number="1",
        directive_number="1"
        )
    # songwriter_number - sequence number of songwriter
    # directive_number - sequence number of directive in current songwriter
    # item_number - number of item in directive dropdown menu "actions":
    # "1" - edit
    # "3" - remove
    app.song.choose_item_in_action_menu(
        songwriter_number="1",
        directive_number="1",
        item_number="3"
        )
    app.song.close_directive_modal_window_button_cancel()
    app.song.open_directive_actions_menu(
        songwriter_number="1",
        directive_number="1"
        )
    app.song.choose_item_in_action_menu(
        songwriter_number="1",
        directive_number="1",
        item_number="3"
        )
    app.song.close_modal_window_button_close()
    app.song.open_directive_actions_menu(
        songwriter_number="1",
        directive_number="1"
        )
    app.song.choose_item_in_action_menu(
        songwriter_number="1",
        directive_number="1",
        item_number="3"
        )
    app.song.check_style_of_remove_modal_window(
        title="Confirm remove Directive",
        message="Are you sure you want to remove directive?"
        )
    app.song.confirm_remove()
    time.sleep(3)
