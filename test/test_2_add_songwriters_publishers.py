__author__ = 'pavelkosicin'
from model.songwriter import Songwriter


def test_search_song(app):
    app.song.search_song(query="song_A")


#def test_switch_to_tab_songwriters(app):
#    app.navigate.tab_songwriters()


#def test_check_empty_tab_songwriters(app):
#    app.songwriter.check_alert_info_tab_songwriter(alert_text="There is not one Songwriter for this song")


#def test_create_songwriter_in_song(app):
#    app.songwriter.add_songwriter(name="person_songwriter_#1")


#def test_edit_songwriter_on_the_song(app):
    #app.song.open_edit_songwriter_modal_window()
    #app.song.close_edit_songwriter_modal_window()
    #app.song.open_edit_songwriter_modal_window()
    #app.song.check_songwriter_default_role(role_1="Author", role_2="Composer")
    #app.song.check_cross_id(locator_path="div._15tqGvIentb7leltuBfTAA>div>div.col-xs-9>div", prefix='CCSW')
    #app.song.add_secondary_name(new_name="new_name_person_songwriter_#1", text="writing")
    #app.song.edit_songwriter_roles()
    #app.song.fill_identifiers_fields_in_edit_songwriter_modal_window(Songwriter(ipicae="G-332947321-0",
    #                                                                           asap="4443588649923"))
    #app.song.edit_sonwriter_info_in_modal_window(Songwriter(name="edited_name_person_songwriter_#1", ipicae="T-332947321-2",
    #                                                        asap="4443588649922"))
