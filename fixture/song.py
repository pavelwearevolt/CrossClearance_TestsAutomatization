__author__ = 'pavelkosicin'
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class SongHelper:

    def __init__(self, app):
        self.app = app

    def create_song(self, name):
        wd = self.app.wd
        # create song
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='modal-body']//button[.='song']").click()

    def identifiers_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)

    def fill_song_form(self, data):
        wd = self.app.wd
        # add identifiers
        self.identifiers_field_value("song_iswc_identification_new", data.iswc)
        wd.find_element_by_id("song_iswc_identification_new_add").click()
        self.identifiers_field_value("song_asap_identification_new", data.asap)
        wd.find_element_by_id("song_asap_identification_new_add").click()
        self.identifiers_field_value("song_ascap_identification_new", data.ascap)
        wd.find_element_by_id("song_ascap_identification_new_add").click()
        self.identifiers_field_value("song_bmi_identification_new", data.bmi)
        wd.find_element_by_id("song_bmi_identification_new_add").click()
        self.identifiers_field_value("song_sesac_identification_new", data.sesac)
        wd.find_element_by_id("song_sesac_identification_new_add").click()
        # add note
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(data.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()

    def search_song(self, query):
        # navigate to the global search
        self.app.navigate.menu_global_search()
        self.app.search.find_entity(query)

    def check_cross_id(self):
        wd = self.app.wd
        # find cross id
        cross_id = wd.find_element_by_css_selector("div.list-group:nth-child(1)>span:nth-child(1)>li:nth-child(1)>" +\
                "div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>span:nth-child(1)").text
        # check for ambiguous symbols
        ambiguous_symbols = ['0', '1', 'I', 'i', 'L', 'l', 'O', 'o']
        for symbol in ambiguous_symbols:
            assert symbol not in cross_id[4:], "A restricted symbol found - \"%s\"" % symbol
        # check prefix of cross id
        assert cross_id.startswith('CCSN')

    def add_secondary_name(self, new_name):
        wd = self.app.wd
        wd.find_element_by_id("song_name_new_search").click()
        wd.find_element_by_id("song_name_new_search").clear()
        wd.find_element_by_id("song_name_new_search").send_keys(new_name)
        wd.find_element_by_id("song_name_new_create").click()

    def get_item_list(self, item_data):
        wd = self.app.wd
        check_list = []
        # list of names and identifiers, first items in list - names
        element = wd.find_elements_by_class_name("_3XcHlhYq6SKGkDZzMHxu2Q ")
        for item in element:
            if item.text == item_data:
                check_list.append(item.text)
            assert item_data in check_list, "no such data in fields"

    def change_data_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_id(field_name).click()
            wd.find_element_by_id(field_name).clear()
            wd.find_element_by_id(field_name).send_keys(text)
            wd.find_element_by_id(field_name + "_save").click()

    def check_cancel_button(self, field_name):
        wd = self.app.wd
        wd.find_element_by_id(field_name + "_cancel").click()

    def edit_data(self, data):
        wd = self.app.wd
        # edit song name
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[2]/div/div[2]/span/li[2]/div[2]/div/div[1]/a").click()
        self.check_cancel_button("song_name_edit")
        self.change_data_value("song_name_edit", data.name)
        # edit iswc
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div/div[2]/span/li/div[2]/div/div[1]/div/a").click()
        self.check_cancel_button("song_iswc_identification_edit")
        self.change_data_value("song_iswc_identification_edit", data.iswc)
        # edit asap
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[5]/div/div[2]/span/li/div[2]/div/div[1]/div/a").click()
        self.check_cancel_button("song_asap_identification_edit")
        self.change_data_value("song_asap_identification_edit", data.iswc)
        # edit ascap
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[6]/div/div[2]/span/li/div[2]/div/div[1]/div/a").click()
        self.check_cancel_button("song_ascap_identification_edit")
        self.change_data_value("song_ascap_identification_edit", data.iswc)
        # edit bmi
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[7]/div/div[2]/span/li/div[2]/div/div[1]/div/a").click()
        self.check_cancel_button("song_bmi_identification_edit")
        self.change_data_value("song_bmi_identification_edit", data.iswc)
        # edit sesac
        wd.find_element_by_xpath("//form[@class='form-horizontal']/div[8]/div/div[2]/span/li/div[2]/div/div[1]/div/a").click()
        self.check_cancel_button("song_sesac_identification_edit")
        self.change_data_value("song_sesac_identification_edit", data.iswc)
        # edit note
        #wd.find_element_by_xpath("//form[@class='form-horizontal']/div[4]/div/div[2]/span/li/div[2]/div/div[1]/div/a").click()
        #self.check_cancel_button("song_iswc_identification_edit")
        #self.change_data_value("song_iswc_identification_edit", data.iswc)




#    def delete_song(self):
#        wd = self.app.wd
#        wait = self.app.wait
#        wd.find_element_by_xpath("//div[@class='rubix-panel']//button[.='Delete Song']").click()
#        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='modal-footer']//button[.='Delete']"))).click()

