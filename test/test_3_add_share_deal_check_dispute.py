__author__ = 'pavelkosicin'
import time


def test_add_share(app):
    app.navigate.switch_to_tab(tab_name="Songwriters")
    # entity_number - entity's (songwriter or publisher) sequence number on the song editing page
    # in this test entity_number - sequence number of songwriter
    app.song.open_dropdown_menu(entity_number="1")
    # entity_number - number of songwriter or publisher
    # entity's sequence number on the song editing page (for example first songwriter)
    # function_number - button share or button deal
    # 1 - share
    # 2 - deal
    app.song.open_modal_window(entity_number="1", function_number="1")
    app.song.close_modal_window_button_close()
    app.song.open_dropdown_menu(entity_number="1")
    app.song.open_modal_window(entity_number="1", function_number="1")
    app.song.close_modal_window_button_cancel()
    app.song.open_dropdown_menu(entity_number="1")
    app.song.open_modal_window(entity_number="1", function_number="1")
    app.song.fill_share_form(
        territory="world",
        territory_locator="tt-suggestion.suggestion-0",
        percentage="60"
        )


def test_add_deal_tab_songwriter(app):
    # entity_number - entity's (songwriter or publisher) sequence number on the song editing page
    # in this test entity_number - sequence number of songwriter
    app.song.open_dropdown_menu(entity_number="1")
    # entity_number - number of songwriter or publisher
    # entity's sequence number on the song editing page (for example first songwriter)
    # function_number - button share or button deal
    # 1 - share
    # 2 - deal
    app.song.open_modal_window(entity_number="1", function_number="2")
    app.song.close_modal_window_button_close()
    app.song.open_dropdown_menu(entity_number="1")
    app.song.open_modal_window(entity_number="1", function_number="2")
    app.song.close_modal_window_button_cancel()
    app.song.open_dropdown_menu(entity_number="1")
    app.song.open_modal_window(entity_number="1", function_number="2")
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
    app.song.fill_percentage_field(percentage="50")
    app.song.save_button()
    time.sleep(3)


def test_share_in_dispute(app):
    # add second songwriter
    app.song.add_entity_link(name="person_songwriter_#2", text="writing")
    # add share for second songwriter
    # entity_number - entity's (songwriter or publisher) sequence number on the song editing page
    # in this test entity_number - sequence number of songwriter
    app.song.open_dropdown_menu(entity_number="2")
    # entity_number - number of songwriter or publisher
    # entity's sequence number on the song editing page (for example first songwriter)
    # function_number - button share or button deal
    # 1 - share
    # 2 - deal
    app.song.open_modal_window(entity_number="2", function_number="1")
    app.song.fill_share_form(
        territory="canada",
        territory_locator="tt-suggestion.suggestion-2",
        percentage="60"
        )
    # warning (share in dispute) share button color - "rgb(240, 173, 78)"
    # check share button of first songwriter
    app.song.check_share_button_in_dispute_and_not(songwriter_number="1", button_color="rgb(240, 173, 78)")
    # check share button of second songwriter
    app.song.check_share_button_in_dispute_and_not(songwriter_number="2", button_color="rgb(240, 173, 78)")


def test_edit_share(app):
    # songwriter_number - songwriter's sequence number on the song editing page
    app.song.open_share_dropdown_menu(songwriter_number="2")
    # songwriter_number - songwriter's sequence number on the song editing page
    # item_number - item`s sequence number in share dropedown menu
    # 1 - "Edit share"
    # 2 - if share in dispute - "Show dispute", if share is not in dispute - "Show countries"
    # 3 - if share in dispute - "Show countries", if share is not in dispute - there will be no item
    app.song.choose_item_in_share_dropdown_menu(songwriter_number="2", item_number="1")
    app.song.clear_share_territory_field()
    app.song.fill_share_form(
            territory="world",
            territory_locator="tt-suggestion.suggestion-0",
            percentage="40"
            )


def test_share_is_not_in_dispute(app):
    # normal (share is not in dispute) share button color - rgb(85, 201, 166)
    # check share button of first songwriter
    app.song.check_share_button_in_dispute_and_not(songwriter_number="1", button_color="rgb(85, 201, 166)")
    # check share button of second songwriter
    app.song.check_share_button_in_dispute_and_not(songwriter_number="2", button_color="rgb(85, 201, 166)")


#def test_deal_in_dispute(app):
    # add second deal in tab "Publishers"
#    app.navigate.switch_to_tab(tab_name="Publishers")
    # entity_number - entity's (songwriter or publisher) sequence number on the song editing page
    # in this test entity_number - sequence number of publisher
#    app.song.open_dropdown_menu(entity_number="1")
    # entity_number - number of songwriter or publisher
    # entity's sequence number on the song editing page (for example first songwriter)
    # function_number - button share or button deal
    # TAB "SONGWRITERS"
    # 1 - share
    # 2 - deal
    # TAB "PUBLISHERS"
    # 1 - deal
#    app.song.open_modal_window(entity_number="1", function_number="1")
#    app.song.check_entity_in_new_deal_modal_window(entity_id="publishing_select", entity_name="company_publisher_#1")
    # fill publisher field
#    app.song.fill_field_in_new_deal_modal_window(
#        field_id="publishing_select",
#        field_value="company_publisher_#1",
#        field_locator="3"
#        )
    # fill Licensed Territory field
#    app.song.fill_field_in_new_deal_modal_window(
#        field_id="licenced_territory_select",
#        field_value="World",
#        field_locator="4"
#        )
    # fill field license origin
#    app.song.fill_field_in_new_deal_modal_window(
#        field_id="license_origin_select",
#        field_value="World",
#        field_locator="5"
#        )
    # fill field media type
#    app.song.fill_field_in_new_deal_modal_window(
#        field_id="media_type_select",
#        field_value="Grand Rights",
#        field_locator="6"
#        )
#    app.song.fill_field_in_new_deal_modal_window(
#        field_id="media_type_select",
#        field_value="Mechanical/Reproduction",
#        field_locator="6"
#        )
#    app.song.fill_field_in_new_deal_modal_window(
#        field_id="media_type_select",
#        field_value="Performance Rights",
#        field_locator="6"
#        )
#    app.song.fill_field_in_new_deal_modal_window(
#        field_id="media_type_select",
#        field_value="Synchronization",
#        field_locator="6"
#        )
#    app.song.fill_field_in_new_deal_modal_window(
#        field_id="media_type_select",
#        field_value="Print Music",
#        field_locator="6"
#        )
#    app.song.fill_percentage_field(percentage="50")
#    app.song.save_button()
#    time.sleep(3)
