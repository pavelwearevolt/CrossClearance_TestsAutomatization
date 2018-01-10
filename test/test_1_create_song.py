# -*- coding: utf-8 -*-
__author__ = 'Pavel Kosicin'
from model.song import Song


def test_create_song(app):
    app.song.create_song(Song(name="song_A", iswc="T-553.682.543-1", asap="8554215642",
                              ascap="536275433", bmi="0002314566", sesac="4325666754",
                              note="Contemplantes ad proprietate vocis disseruero, factus Buddha."))
    app.song.search_created_song()
    app.song.check_cross_id()
