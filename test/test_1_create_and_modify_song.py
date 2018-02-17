__author__ = 'pavelkosicin'
from model.modify import Modify
from model.note import Note


def test_create_song(app):
    app.song.create_song(name="song_A")
    app.song.check_cross_id(locator_path="div.list-group:nth-child(1)>span:nth-child(1)>li:nth-child(1)>" +\
                "div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>span:nth-child(1)", prefix="CCSN")


def test_search_song(app):
    app.song.search_song(query="song_A")


def test_switch_to_tab_songwriters(app):
    app.navigate.tab_songwriters()


def test_check_empty_tab_songwriters(app):
    app.song.check_alert_info(alert_text="There is not one Songwriter for this song")


def test_switch_to_tab_publishers(app):
    app.navigate.tab_publishers()


def test_check_empty_tab_publishers(app):
    app.song.check_alert_info(alert_text="There is not one Publisher for this song")


def test_switch_to_tab_directives(app):
    app.navigate.tab_directives()


def test_check_empty_tab_directives(app):
    app.song.check_alert_info(alert_text="There is not deals between Songwriter and Publishers for this song.")


def test_switch_to_tab_copyrigt_collective_info(app):
    app.navigate.tab_copyrigt_collective_info()


def test_check_empty_tab_copyrigt_collective_info(app):
    app.song.check_alert_info(alert_text="Copyright collective info not found.")


def test_switch_to_tab_master_recordings(app):
    app.navigate.tab_master_recordings()


def test_check_empty_tab_master_recordings(app):
    app.song.check_alert_info(alert_text="There are not Master Recordings associated for this song.")


def test_switch_to_tab_general_info(app):
    app.navigate.tab_general_info()


def test_modify_song_general(app):
    app.song.fill_song_form(Modify(
        iswc="T-553.682.543-1",
        asap="8554215642",
        ascap="536275433",
        bmi="0002314566",
        sesac="4325666754"
        ))
    app.song.add_note(Note(note="Contemplantes ad proprietate vocis disseruero, factus Buddha."))


def test_add_secondary_song_name(app):
    # check song name
#    app.song.get_item_list(item_data="song_A")
    app.song.add_secondary_name(new_name="new_name_song_A", text="song")
#    time.sleep(3)
    # check secondary name
#    app.song.get_item_list(item_data="new_name_song_A")


def test_edit_song_info(app):
    app.song.edit_song_info(Modify(
        name="edited_song_A_name",
        iswc="T-553.682.543-2",
        asap="8554215643",
        ascap="536275432",
        bmi="0002314562",
        sesac="4325666752"
        ))
