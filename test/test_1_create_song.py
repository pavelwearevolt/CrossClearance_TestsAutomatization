# -*- coding: utf-8 -*-
__author__ = 'Pavel Kosicin'
from model.song import Song


def test_create_song(app):
    app.song.create_from_global_search(Song(name="song_A", iswc="Q-548.132.789-0", asap="U70_S4XJQTR.1GW_P",
        ascap="GJ_7.031C46TSW58", bmi="13_E7C_W68RSI50H_U", sesac="EX.2136TH.UIS54C-0",
        note="Contemplantes ad proprietate vocis disseruero, factus Buddha."))
    app.song.create_from_menu_songs(Song(name="song_B", iswc="W-104.559.141-9", asap="D23_B53FG5E.1GW_P",
        ascap="VN_4.035F55SQA60", bmi="82_HD5_MN5TXSP50_Q", sesac="DN.6301ND.CXZ59I-3",
        note="Realizing corruptibilis creata sunt: et ecce in aeternum permanet."))
