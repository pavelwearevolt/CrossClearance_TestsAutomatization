__author__ = 'Pavel Kosicin'
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class RecordingHelper:

    def __init__(self, app):
        self.app = app

    def add_artist(self):
        wd = self.app.wd
        # navigate menu global search
        self.app.navigate.menu_global_search()
        # find song
        self.app.search.global_search(name="song_A")
        # open master recording tab
        wd.find_element_by_xpath("//nav[@class='collapse in']/ul/li[6]/a").click()
        # find recording artist, artist name see in test_3_create_recording_artist_global_search
        wd.find_element_by_id("master_recording_search").click()
        wd.find_element_by_id("master_recording_search").clear()
        wd.find_element_by_id("master_recording_search").send_keys("ra_#1")
        wd.find_element_by_css_selector("p.complex-suggestion").click()
        # fill master recording create form
        # edit master recording name
        wd.find_element_by_name("masterRecordingName").click()
        wd.find_element_by_name("masterRecordingName").clear()
        wd.find_element_by_name("masterRecordingName").send_keys("mr_#1")
        # edit Recording Artist role
        wd.find_element_by_id("role_select_role_clear").click()
        wd.find_element_by_id("role_select_role_item_9").click()
        wd.find_element_by_id("role_select_role_item_10").click()
        wd.find_element_by_id("role_select_role_item_11").click()
        # edit Type
        wd.find_element_by_id("undefined_clear").click()
        wd.find_element_by_id("undefined_item_2").click()
        # create master recording
        wd.find_element_by_xpath("//div[@class='modal-footer']//button[.='Create']").click()
        time.sleep(5)
        self.app.navigate.menu_master_recording()
        self.app.search.object_search(name="mr_#1")

    def modify(self):
        wd = self.app.wd
        wait = self.app.wait
        # modify recording type
        wd.find_element_by_id("recording_type_box").click()
        wd.find_element_by_xpath("//*[@id='recording_type_box']/option[3]").click()
        # modify recording version
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div/div/a").click()
        wd.find_element_by_id("master_recording_recording_version").click()
        wd.find_element_by_id("master_recording_recording_version").clear()
        wd.find_element_by_id("master_recording_recording_version").send_keys("test_version")
        wd.find_element_by_id("master_recording_recording_version_save").click()
        # modify copyright date
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[5]/div/div/div/select[1]").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[5]/div/div/div/select[1]/option[3]").click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//form[@class='form-horizontal']/div[5]/div/div/div/select[2]"))).click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[5]/div/div/div/select[2]/option[3]").click()
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//form[@class='form-horizontal']/div[5]/div/div/div/select[3]"))).click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[5]/div/div/div/select[3]/option[30]").click()
        # modify identificator ISRC
        wd.find_element_by_id("master_recording_isrc_identification_new").click()
        wd.find_element_by_id("master_recording_isrc_identification_new").clear()
        wd.find_element_by_id("master_recording_isrc_identification_new").send_keys("QW-RE1-42-05634")
        wd.find_element_by_id("master_recording_isrc_identification_new_add").click()
        # modify identificator ASAP
        wd.find_element_by_id("master_recording_asap_identification_new").click()
        wd.find_element_by_id("master_recording_asap_identification_new").clear()
        wd.find_element_by_id("master_recording_asap_identification_new").send_keys("D7J_W9MZ38.5BA_L")
        wd.find_element_by_id("master_recording_asap_identification_new_add").click()
        # modify note
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys("Tibi causa doloris certamine concessuros quae tua.")
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()
        time.sleep(2)
