__author__ = 'pavelkosicin'
from model.songwriter import Songwriter


def test_search_song(app):
    app.song.search_song(query="song_A")


def test_create_songwriter_in_song(app):
    app.navigate.tab_songwriters()
    app.song.add_entity_link(name="person_songwriter_#1", text="writing")


def test_edit_songwriter_in_song(app):
    app.song.open_edit_entity_modal_window()
    app.song.close_edit_entity_modal_window()
    app.song.open_edit_entity_modal_window()
    app.song.check_songwriter_default_role(role_1="Author", role_2="Composer")
    app.song.check_cross_id(locator_path="div._15tqGvIentb7leltuBfTAA>div>div.col-xs-9>div", prefix='CCSW')
    app.song.add_secondary_name(new_name="new_name_person_songwriter_#1", text="writing")
    app.song.edit_songwriter_roles()
    app.song.fill_identifiers_fields_in_edit_songwriter_modal_window(Songwriter(
        ipicae="G-332947321-0",
        asap="4443588649923"
        ))
    app.song.edit_sonwriter_info_in_modal_window(Songwriter(
        name="edited_name_person_songwriter_#1",
        ipicae="T-332947321-2",
        asap="4443588649922"
        ))


def test_create_publisher_in_song(app):
    app.navigate.tab_publishers()
    app.song.add_entity_link(name="company_publisher_#1", text="publishing")
