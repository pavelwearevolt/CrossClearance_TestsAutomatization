__author__ = 'Pavel Kosicin'
import time


class CollectiveHelper:

    def __init__(self, app):
        self.app = app

    def create_copyright_collective(self, collective):
        wd = self.app.wd
        # navigate menu global search
        self.app.navigate.menu_global_search()
        # create collective
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(collective.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='NTialWg8eHGF9sNIWyhYH']//button[.='company']").click()
        # select type
        self.type()
        # fill form on the CopyrightCollective modal window
        self.fill_form()
        # find created collective
        self.app.navigate.menu_global_search()
        self.app.search.find_entity(query="cc_#1")
        # add notes
        self.add_notes(collective)

    def type(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/button").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/ul/li[1]").click()
        time.sleep(2)

    def fill_form(self):
        wd = self.app.wd
        # fill form on the CopyrightCollective modal window
        wd.find_element_by_id("license_origin_select_search").click()
        wd.find_element_by_id("license_origin_select_search").clear()
        wd.find_element_by_id("license_origin_select_search").send_keys("canada")
        wd.find_element_by_xpath("//span[@class='tt-suggestions']/div/div[2]/div[2]/div/p").click()
        wd.find_element_by_id("media_type_select").click()
        wd.find_element_by_id("media_type_select_item_2").click()
        wd.find_element_by_id("media_type_select_item_3").click()
        wd.find_element_by_xpath("//div[@class='modal-footer']//button[.='Ok']").click()
        time.sleep(2)

    def add_notes(self, collective):
        wd = self.app.wd
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(collective.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()
        time.sleep(3)

