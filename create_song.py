# -*- coding: utf-8 -*-
__author__ = 'Pavel Kosicin'


from song import Song
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_song(app):
    app.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.create(Song(name="song_A", iswc="Q-548.132.789-0", asap="U70_S4XJQTR.1GW_P", ascap="GJ_7.031C46TSW58",
        bmi="13_E7C_W68RSI50H_U", sesac="EX.2136TH.UIS54C-0",
        note="Contemplantes ad proprietate vocis disseruero, factus Buddha."))
    app.find(name="song_A")
    app.logout()
