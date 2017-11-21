__author__ = 'Pavel Kosicin'
import time


class PublisherHelper:

    def __init__(self, app):
        self.app = app

    def create_from_song(self, publisher):
        wd = self.app.wd
        # navigate to the menu global search
        self.app.navigate.menu_global_search()
        # find song
        self.app.search.global_search(name="song_A")
        # open tab publishers
        wd.find_element_by_link_text("Publishers").click()
        # create publisher
        wd.find_element_by_id("publishing_new_search").click()
        wd.find_element_by_id("publishing_new_search").clear()
        wd.find_element_by_id("publishing_new_search").send_keys(publisher.name)
        wd.find_element_by_id("publishing_new_create").click()
        # open edit publisher modal window
        wd.find_element_by_link_text(publisher.name).click()
        # fill fields on the edit publisher modal window
        self.fill_fields_modal_window(publisher)
        # click button 'Ok' on the publisher modal window
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        # find created publisher, open publisher edit page
        self.app.navigate.menu_companies()
        self.app.search.object_search(name="pb_#1")
        # add notes
        self.add_notes(publisher)

    def create_from_menu_global_search(self, publisher):
        wd = self.app.wd
        # navigate menu global search
        self.app.navigate.menu_global_search()
        # create publisher
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(publisher.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='NTialWg8eHGF9sNIWyhYH']//button[.='company']").click()
        # select type
        self.type()
        # find created songwriter
        self.app.navigate.menu_companies()
        self.app.search.object_search(name="pb_#2")
        # fill fields on the publisher edit page
        self.fill_fields_pulisher_edit_page(publisher)
        # add notes
        self.add_notes(publisher)

    def create_from_menu_companies(self, publisher):
        wd = self.app.wd
        # navigate menu companies
        self.app.navigate.menu_companies()
        # create publisher
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(publisher.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        # select person type
        self.type()
        # find created songwriter
        self.app.navigate.menu_global_search()
        self.app.search.global_search(name="pb_#3")
        # fill fields on the songwriter edit page
        self.fill_fields_pulisher_edit_page(publisher)
        # add notes
        self.add_notes(publisher)

    def fill_fields_modal_window(self, publisher):
        wd = self.app.wd
        wd.find_element_by_id("publisher_ipicae_identification_new").click()
        wd.find_element_by_id("publisher_ipicae_identification_new").clear()
        wd.find_element_by_id("publisher_ipicae_identification_new").send_keys(publisher.ipicae)
        wd.find_element_by_id("publisher_ipicae_identification_new_add").click()
        wd.find_element_by_id("publisher_asap_identification_new").click()
        wd.find_element_by_id("publisher_asap_identification_new").clear()
        wd.find_element_by_id("publisher_asap_identification_new").send_keys(publisher.asap)
        wd.find_element_by_id("publisher_asap_identification_new_add").click()

    def fill_fields_pulisher_edit_page(self, publisher):
        wd = self.app.wd
        # fill ipicae
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[1]/div/div[1]/input").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[1]/div/div[1]/input").clear()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[1]/div/div[1]/input").send_keys(publisher.ipicae)
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[1]/div/div[1]/div").click()
        # fill asap
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[2]/div/div[1]/input").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[2]/div/div[1]/input").clear()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[2]/div/div[1]/input").send_keys(publisher.asap)
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[2]/div/div[1]/div").click()

    def add_notes(self, publisher):
        wd = self.app.wd
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(publisher.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()
        time.sleep(3)

    def type(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/button").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/ul/li[2]").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(3)
