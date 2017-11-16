__author__ = 'Pavel Kosicin'
import time

class ArtistHelper:

    def __init__(self, app):
        self.app = app

    def create(self, artist):
        wd = self.app.wd
        # create artist
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(artist.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='modal-body']//button[.='person']").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/button").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/ul/li[2]").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(3)
        self.app.navigate.menu_people()
        self.find(name="ra_#1")
        # add notes
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(artist.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()

    def find(self, name):
        wd = self.app.wd
        # find created recording artist
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(name)
        # choose found recording artist
        wd.find_element_by_link_text(name).click()
