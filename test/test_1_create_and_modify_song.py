__author__ = 'pavelkosicin'
from model.modify import Modify
from model.note import Note
import time


def test_create_song(app):
    app.song.create_song(name="song_A")
    app.song.check_cross_id(locator_path="div.list-group:nth-child(1)>span:nth-child(1)>li:nth-child(1)>" +\
                "div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>span:nth-child(1)", prefix="CCSN")
    app.song.check_fields_value_default(name="song_A")


def test_search_song(app):
    app.song.search_song(query="song_A")


def test_check_empty_tabs(app):
    app.navigate.switch_to_tab(tab_name="Songwriters")
    app.song.check_alert_info(alert_text="There is not one Songwriter for this song")
    app.navigate.switch_to_tab(tab_name="Publishers")
    app.song.check_alert_info(alert_text="There is not one Publisher for this song")
    app.navigate.switch_to_tab(tab_name="Directives")
    app.song.check_alert_info(alert_text="There is not deals between Songwriter and Publishers for this song.")
    app.navigate.switch_to_tab(tab_name="Copyright Collective Info")
    app.song.check_alert_info(alert_text="Copyright collective info not found.")
    app.navigate.switch_to_tab(tab_name="Master Recordings")
    app.song.check_alert_info(alert_text="There are not Master Recordings associated for this song.")


def test_modify_song_general(app):
    app.navigate.switch_to_tab(tab_name="General Info")
    app.song.fill_song_form(Modify(
        iswc="T-553.682.543-1",
        asap="8554215642",
        ascap="536275433",
        bmi="0002314566",
        sesac="4325666754"
        ))
    app.song.add_note(Note(note="Contemplantes ad proprietate vocis disseruero, factus Buddha."))


def test_edit_song_info(app):
    app.song.edit_song_info(Modify(
        name="edited_song_A_name",
        iswc="T-553.682.543-2",
        asap="8554215643",
        ascap="536275432",
        bmi="0002314562",
        sesac="4325666752"
        ))


def test_edit_note(app):
    # note_number - note's sequence number on the song editing page (for example first note)
    app.song.open_note_dropdown_menu(note_number="1")
    # note_number - note's sequence number on the song editing page (for example first note)
    # item_number - button edit or remove note
    # 1 - edit
    # 3 - remove
    app.song.choose_item_in_note_dropdown_menu(note_number="1", item_number="1")
    app.song.close_modal_window_button_close()
    app.song.open_note_dropdown_menu(note_number="1")
    app.song.choose_item_in_note_dropdown_menu(note_number="1", item_number="1")
    app.song.button_cancel_in_edit_note_modal_window()
    app.song.open_note_dropdown_menu(note_number="1")
    app.song.choose_item_in_note_dropdown_menu(note_number="1", item_number="1")
    app.song.edit_note_text(Note(note="Contemplantes ad proprietate vocis disseruero, factus Buddha!!!!!"))
    app.song.button_edit_in_edit_note_modal_window()


#def test_change_default_song_name(app):
#    app.song.add_secondary_name(new_name="new_name_song_A", text="song")

