__author__ = 'pavelkosicin'
from model.songwriter import Songwriter
from model.publisher import Publisher


def test_create_songwriter_in_song(app):
    app.navigate.switch_to_tab(tab_name="Songwriters")
    app.song.add_entity_link(name="person_songwriter_#1", text="writing")


def test_edit_songwriter_in_song(app):
    app.song.open_edit_entity_modal_window()
    app.song.close_edit_entity_modal_window()
    app.song.open_edit_entity_modal_window()
    app.song.check_songwriter_default_role(role_1="Author", role_2="Composer")
    app.song.check_cross_id(locator_path="div._15tqGvIentb7leltuBfTAA>div>div.col-xs-9>div", prefix='CCSW')
    app.song.add_secondary_name(new_name="new_name_person_songwriter_#1", text="writing")
    app.song.edit_songwriter_roles()
    app.song.fill_identifiers_fields_in_edit_entity_modal_window(Songwriter(
        ipicae="G-332947321-0",
        asap="4443588649923"
        ), entity="songwriter")
    app.song.edit_entity_info_in_modal_window(Songwriter(
        name="edited_name_person_songwriter_#1",
        ipicae="T-332947321-2",
        asap="4443588649922"
        ), entity_name="writing", entity_identifier="songwriter")


def test_create_publisher_in_song(app):
    app.navigate.switch_to_tab(tab_name="Publishers")
    app.song.add_entity_link(name="company_publisher_#1", text="publishing")


def test_edit_publisher_in_song(app):
    app.song.open_edit_entity_modal_window()
    app.song.close_edit_entity_modal_window()
    app.song.open_edit_entity_modal_window()
    app.song.check_cross_id(locator_path="div._15tqGvIentb7leltuBfTAA>div>div.col-xs-9>div", prefix='CCPB')
    app.song.add_secondary_name(new_name="new_name_company_publisher_#1", text="publishing")
    app.song.fill_identifiers_fields_in_edit_entity_modal_window(Publisher(
        ipicae="Q-562975093-1",
        asap="566487389203"
        ), entity="publisher")
    app.song.edit_entity_info_in_modal_window(Publisher(
        name="edited_name_company_publisher_#1",
        ipicae="H-562975093-2",
        asap="566487389202"
        ), entity_name="publishing", entity_identifier="publisher")
