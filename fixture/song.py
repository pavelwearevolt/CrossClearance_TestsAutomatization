__author__ = 'Pavel Kosicin'
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class SongHelper:

    def __init__(self, app):
        self.app = app

    def create_from_global_search(self, song):
        wd = self.app.wd
        # create song
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(song.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='modal-body']//button[.='song']").click()
        # song modification
        self.fill_song_form(song)
        self.app.navigate.menu_global_search()
        self.app.search.global_search(name="song_A")

    def create_from_menu_songs(self, song):
        wd = self.app.wd
        # navigate menu songs
        self.app.navigate.menu_songs()
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(song.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        # song modification
        self.fill_song_form(song)
        self.app.navigate.menu_global_search()
        self.app.search.global_search(name="song_B")

    def fill_song_form(self, song):
        wd = self.app.wd
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

    def merge(self):
        wd = self.app.wd
        # navigate to the global search
        self.app.navigate.menu_global_search()
        self.app.search.global_search(name="song_A")
        # click button merge song
        wd.find_element_by_css_selector("button.btn-outlined.btn.btn-warning").click()
        # find second song for merge
        wd.find_element_by_xpath("//div[@class='col-md-3']/form/div[2]/div/input").click()
        wd.find_element_by_xpath("//div[@class='col-md-3']/form/div[2]/div/input").clear()
        wd.find_element_by_xpath("//div[@class='col-md-3']/form/div[2]/div/input").send_keys("Song_B")
        wd.find_element_by_xpath("//div[@class='col-md-3']/form/div[3]/div").click()
        time.sleep()
        wd.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/button[1]").click()
        time.sleep(3)
        wd.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/form/div[2]/div/div/div/a").click()
        time.sleep(30)
        wd.refresh()

#    def delete_song(self):
#        wd = self.app.wd
#        wait = self.app.wait
#        wd.find_element_by_xpath("//div[@class='rubix-panel']//button[.='Delete Song']").click()
#        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='modal-footer']//button[.='Delete']"))).click()

