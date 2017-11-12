# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from song import Song
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class create_song(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
    
    def test_create_song(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="pavel.kosicin@wearevolt.com", password="abcd1234")
        self.create(wd, Song(name="song_A", iswc="Q-548.132.789-0", asap="U70_S4XJQTR.1GW_P", ascap="GJ_7.031C46TSW58",
                    bmi="13_E7C_W68RSI50H_U", sesac="EX.2136TH.UIS54C-0",
                    note="Contemplantes ad proprietate vocis disseruero, factus Buddha."))
        self.return_to_global_search(wd)
        self.find(wd, name="song_A")
        self.logout(wd)
        self.assertTrue(success)

    def open_home_page(self, wd):
        wd.get("https://cross-auth-staging.herokuapp.com/?redirect_uri=https%3A%2F%2Fcross-edit-staging-frontend.herokuapp.com%2F")

    def login(self, wd, username, password):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='sign-in-control-box']//button[.='Log In']").click()

    def create(self, wd, song):
        # create song
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(song.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='modal-body']//button[.='song']").click()
        # song modification
        wd.find_element_by_id("song_iswc_identification_new").click()
        wd.find_element_by_id("song_iswc_identification_new").clear()
        wd.find_element_by_id("song_iswc_identification_new").send_keys(song.iswc)
        wd.find_element_by_id("song_iswc_identification_new_add").click()
        wd.find_element_by_id("song_asap_identification_new").click()
        wd.find_element_by_id("song_asap_identification_new").clear()
        wd.find_element_by_id("song_asap_identification_new").send_keys(song.asap)
        wd.find_element_by_id("song_asap_identification_new_add").click()
        wd.find_element_by_id("song_ascap_identification_new").click()
        wd.find_element_by_id("song_ascap_identification_new").clear()
        wd.find_element_by_id("song_ascap_identification_new").send_keys(song.ascap)
        wd.find_element_by_id("song_ascap_identification_new_add").click()
        wd.find_element_by_id("song_bmi_identification_new").click()
        wd.find_element_by_id("song_bmi_identification_new").clear()
        wd.find_element_by_id("song_bmi_identification_new").send_keys(song.bmi)
        wd.find_element_by_id("song_bmi_identification_new_add").click()
        wd.find_element_by_id("song_sesac_identification_new").click()
        wd.find_element_by_id("song_sesac_identification_new").clear()
        wd.find_element_by_id("song_sesac_identification_new").send_keys(song.sesac)
        wd.find_element_by_id("song_sesac_identification_new_add").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(song.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()

    def return_to_global_search(self, wd):
        wd.find_element_by_link_text("Global search").click()

    def find(self, wd, name):
        # find created song
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(name)
        # choose found song
        wd.find_element_by_link_text(name.title()).click()

    def logout(self, wd):
        # logout
        wd.find_element_by_xpath("//nav[@id='rubix-nav-header']/div/div/div[3]/div/ul/li[7]/a/span").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
