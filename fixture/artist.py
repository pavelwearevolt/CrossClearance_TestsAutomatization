__author__ = 'Pavel Kosicin'
import time


class ArtistHelper:

    def __init__(self, app):
        self.app = app

    def create_recording_artist(self, artist):
        wd = self.app.wd
        # navigate to the global search menu
        self.app.navigate.menu_global_search()
        # create artist in global search
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(artist.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='modal-body']//button[.='person']").click()
        # select type
        self.type()
        # find created artist
        self.app.navigate.menu_global_search()
        self.app.search.find_entity(query="ra_#1")
        # add notes
        self.add_notes(artist)

    def type(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/button").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/ul/li[2]").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(3)

    def add_notes(self, artist):
        wd = self.app.wd
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(artist.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()

