__author__ = 'pavelkosicin'
from model.modify import Modify
import time


#def test_create_song(app):
#    app.song.create_song(name="song_A")
#    app.song.check_cross_id()


def test_search_song(app):
    app.song.search_song(query="song_A")


#def test_modify_song_general(app):
#    app.song.fill_song_form(Modify(iswc="T-553.682.543-1", asap="8554215642", ascap="536275433", bmi="0002314566",
#                           sesac="4325666754", note="Contemplantes ad proprietate vocis disseruero, factus Buddha."))


#def test_add_secondary_song_name(app):
    # check song name
    #app.song.get_item_list(item_data="song_A")
#    app.song.add_secondary_name(new_name="new_name_song_A")
#    time.sleep(3)
    # check secondary name
    #app.song.get_item_list(item_data="new_name_song_A")


def test_edit_song_info(app):
    app.song.edit_data(Modify(name="edited_song_A_name", iswc="T-553.682.543-2", asap="8554215643", ascap="536275432", bmi="0002314562",
                            sesac="4325666752"))

