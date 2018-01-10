__author__ = 'Pavel Kosicin'
import time

class LabelHelper:

    def __init__(self, app):
        self.app = app

    def create_from_menu_global_search(self, label):
        wd = self.app.wd
        # navigate menu global search
        self.app.navigate.menu_global_search()
        # create label
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(label.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='NTialWg8eHGF9sNIWyhYH']//button[.='company']").click()
        # select type
        self.type()
        # find created songwriter
        self.app.navigate.menu_global_search()
        self.app.search.find_entity(query="rl_#1")
        # fill fields on the publisher edit page
        self.fill_fields_pulisher_edit_page(label)
        # add notes
        self.add_notes(label)

    def create_from_menu_companies(self, label):
        wd = self.app.wd
        # navigate menu companies
        self.app.navigate.menu_companies()
        # create publisher
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(label.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        # select person type
        self.type()
        # find created songwriter
        self.app.navigate.menu_global_search()
        self.app.search.find_entity(query="rl_#2")
        # fill fields on the songwriter edit page
        self.fill_fields_pulisher_edit_page(label)
        # add notes
        self.add_notes(label)

    def fill_fields_pulisher_edit_page(self, label):
        wd = self.app.wd
        # fill asap
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[1]/div/div[1]/input").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[1]/div/div[1]/input").clear()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[1]/div/div[1]/input").send_keys(label.asap)
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div[1]/div/div[1]/div").click()

    def add_notes(self, label):
        wd = self.app.wd
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(label.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()
        time.sleep(3)

    def type(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/button").click()
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[3]/div/div[1]/div/ul/li[3]").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(3)

