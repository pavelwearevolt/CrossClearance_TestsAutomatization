__author__ = 'pavelkosicin'
import time


class SongwriterHelper:

    def __init__(self, app):
        self.app = app

    def check_alert_info(self, alert_text):
        wd = self.app.wd
        element = wd.find_element_by_class_name("alert.alert-info").text
        assert element == alert_text, "Wrong alert text or songwriters tab is not empty"

    def create_from_song(self, name):
        wd = self.app.wd
        # create songwriter
        wd.find_element_by_id("writing_new_search").click()
        wd.find_element_by_id("writing_new_search").clear()
        wd.find_element_by_id("writing_new_search").send_keys(name)
        wd.find_element_by_id("writing_new_create").click()

    def create_menu_global_search(self, songwriter):
        wd = self.app.wd
        # navigate menu global search
        self.app.navigate.menu_global_search()
        # create songwriter
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(songwriter.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='NTialWg8eHGF9sNIWyhYH']//button[.='person']").click()
        # select person type
        self.type()
        # find created songwriter
        self.app.navigate.menu_global_search()
        self.app.search.find_entity(query="sw_#2")
        # fill fields on the songwriter edit page
        self.fill_fields(songwriter)
        # add notes
        self.add_notes(songwriter)

    def type(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/button").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/ul/li[1]").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(3)

    def fill_fields(self, songwriter):
        wd = self.app.wd
        wd.find_element_by_id("songwriter_ipicae_identification_new").click()
        wd.find_element_by_id("songwriter_ipicae_identification_new").clear()
        wd.find_element_by_id("songwriter_ipicae_identification_new").send_keys(songwriter.ipipcae)
        wd.find_element_by_id("songwriter_ipicae_identification_new_add").click()
        wd.find_element_by_id("songwriter_asap_identification_new").click()
        wd.find_element_by_id("songwriter_asap_identification_new").clear()
        wd.find_element_by_id("songwriter_asap_identification_new").send_keys(songwriter.asap)
        wd.find_element_by_id("songwriter_asap_identification_new_add").click()

    def add_notes(self, songwriter):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[6]/div/div/div[1]/textarea").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[6]/div/div/div[1]/textarea").clear()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[6]/div/div/div[1]/textarea").send_keys(songwriter.note)
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[6]/div/div/div[1]/button").click()
        time.sleep(3)
