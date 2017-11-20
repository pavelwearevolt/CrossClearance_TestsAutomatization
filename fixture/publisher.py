__author__ = 'Pavel Kosicin'
import time


class PublisherHelper:

    def __init__(self, app):
        self.app = app

    def create_from_song(self, publisher):
        wd = self.app.wd
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
        self.fill_field(publisher)
        # click button 'Ok' on the publisher modal window
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        # find created publisher, open publisher edit page
        self.app.navigate.menu_companies()
        self.app.search.object_search(name="pb_#1")
        # add notes
        self.add_note(publisher)

    def fill_field(self, publisher):
        wd = self.app.wd
        wd.find_element_by_id("publisher_ipicae_identification_new").click()
        wd.find_element_by_id("publisher_ipicae_identification_new").clear()
        wd.find_element_by_id("publisher_ipicae_identification_new").send_keys(publisher.ipicae)
        wd.find_element_by_id("publisher_ipicae_identification_new_add").click()
        wd.find_element_by_id("publisher_asap_identification_new").click()
        wd.find_element_by_id("publisher_asap_identification_new").clear()
        wd.find_element_by_id("publisher_asap_identification_new").send_keys(publisher.asap)
        wd.find_element_by_id("publisher_asap_identification_new_add").click()

    def add_note(self, publisher):
        wd = self.app.wd
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(publisher.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()
        time.sleep(3)
