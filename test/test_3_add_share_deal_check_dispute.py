__author__ = 'pavelkosicin'
import time


def test_search_song(app):
    app.song.search_song(query="song_A")


def test_add_share(app):
    app.navigate.switch_to_tab(tab_name="Songwriters")
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


def test_add_deal_tab_songwriter(app):
    app.song.open_dropdown_menu()
    app.song.open_modal_window(text="Add deal")
    app.song.close_modal_window_button_close()
    app.song.open_dropdown_menu()
    app.song.open_modal_window(text="Add deal")
    app.song.close_modal_window_button_cancel()
    app.song.open_dropdown_menu()
    app.song.open_modal_window(text="Add deal")
    app.song.check_entity_in_new_deal_modal_window(entity_id="songwriter_select", entity_name="person_songwriter_#1")
    # fill publisher field
    app.song.fill_field_in_new_deal_modal_window(
        field_id="publishing_select",
        field_value="company_publisher_#1",
        field_locator="3"
        )
    # fill Licensed Territory field
    app.song.fill_field_in_new_deal_modal_window(
        field_id="licenced_territory_select",
        field_value="World",
        field_locator="4"
        )
    # fill field license origin
    app.song.fill_field_in_new_deal_modal_window(
        field_id="license_origin_select",
        field_value="World",
        field_locator="5"
        )
    # fill field media type
    app.song.fill_field_in_new_deal_modal_window(
        field_id="media_type_select",
        field_value="Grand Rights",
        field_locator="6"
        )
    app.song.fill_field_in_new_deal_modal_window(
        field_id="media_type_select",
        field_value="Mechanical/Reproduction",
        field_locator="6"
        )
    app.song.fill_field_in_new_deal_modal_window(
        field_id="media_type_select",
        field_value="Performance Rights",
        field_locator="6"
        )
    app.song.fill_field_in_new_deal_modal_window(
        field_id="media_type_select",
        field_value="Synchronization",
        field_locator="6"
        )
    app.song.fill_field_in_new_deal_modal_window(
        field_id="media_type_select",
        field_value="Print Music",
        field_locator="6"
        )
    app.song.fill_percentage_field(percentage="100")
    app.song.save_button()
    time.sleep(3)

