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


def test_add_CCI(app):
    # find Copyright Collective name on the tab "Copyright Collective Info"
    cc_name = app.song.cc_name(songwriter_number="1")
    songwriter_name = app.song.cc_songwriter_name(songwriter_number="1")
    publisher_name = app.song.cci_publisher_name(songwriter_number="1", publisher_number="1")
    app.song.open_copyright_collective_info_modal_window(
        songwriter_number="1",
        publisher_number="1"
        )
    app.song.close_modal_window_button_close()
    app.song.open_copyright_collective_info_modal_window(
        songwriter_number="1",
        publisher_number="1"
        )
    app.song.close_modal_window_button_cancel()
    app.song.open_copyright_collective_info_modal_window(
        songwriter_number="1",
        publisher_number="1"
        )
    # find default value of field "Society" in "Create Copyright Collective Info" modal window
    society = app.song.check_society_field_value()
    assert cc_name == society, "Wrong Copyright Collective default name in 'Create Copyright Collective Info' modal window"
    app.song.create_imprint(imprint_name="test_imprint")
    time.sleep(3)
    app.song.fill_percentage_field(
        percentage_field_id="payment-percentage-input",
        percentage="100"
        )
    app.song.open_represents_dropdown_field()
    represents_publisher = app.song.represents_publisher_name()
    assert publisher_name == represents_publisher, "Wrong publisher name in field 'Represents'"
    represents_songwriter = app.song.represents_songwriter_name()
    assert songwriter_name == represents_songwriter, "Wrong songwriter name in field 'Represents'"
    # represents_id - songwriter or publisher id in field "Represents" in modal window "Create Copyright Collective Info"
    # publisher id - "represented_select_item_Publisher"
    # songwriter id - "represented_select_item_Songwriter"
    app.song.choose_represents(represents_id="represented_select_item_Publisher")
    time.sleep(3)
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

def test_remove_cci(app):
    # songwriter_number - sequence number of songwriter
    # publisher_number - sequence number of publisher
    app.song.open_cci_actions_menu(
        songwriter_number="1",
        publisher_number="1"
        )
    # songwriter_number - sequence number of songwriter
    # publisher_number - sequence number of publisher
    # item_number - number of item in directive dropdown menu "actions":
    # "1" - edit
    # "3" - remove
    app.song.choose_item_in_cci_action_menu(
        songwriter_number="1",
        publisher_number="1",
        item_number="3"
        )
    app.song.close_modal_window_button_cancel()
    app.song.open_cci_actions_menu(
        songwriter_number="1",
        publisher_number="1"
        )
    app.song.choose_item_in_cci_action_menu(
        songwriter_number="1",
        publisher_number="1",
        item_number="3"
        )
    app.song.close_modal_window_button_close()
    app.song.open_cci_actions_menu(
        songwriter_number="1",
        publisher_number="1"
        )
    app.song.choose_item_in_cci_action_menu(
        songwriter_number="1",
        publisher_number="1",
        item_number="3"
        )
    app.song.check_style_of_remove_modal_window(
        element_class_name="bg-hoverblue.fg-black50.text-center",
        title="Confirm remove Copyright Collective Info",
        message="Are you sure you want to remove copyright collective info?"
        )
    app.song.confirm_remove()
    time.sleep(3)
