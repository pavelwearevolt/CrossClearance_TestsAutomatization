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
            wd.find_element_by_id(field_name + "_add").click()

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

    def check_cross_id(self, locator_path, prefix):
        wd = self.app.wd
        # find cross id
        cross_id = wd.find_element_by_css_selector(locator_path).text
        # check for ambiguous symbols
        ambiguous_symbols = ['0', '1', 'I', 'i', 'L', 'l', 'O', 'o']
        for symbol in ambiguous_symbols:
            assert symbol not in cross_id[4:], "A restricted symbol found - \"%s\"" % symbol
        # check prefix of cross id
        assert cross_id.startswith(prefix)

    def add_secondary_name(self, new_name, text):
        wd = self.app.wd
        wd.find_element_by_id(self.add_name_locator(text)).click()
        wd.find_element_by_id(self.add_name_locator(text)).clear()
        wd.find_element_by_id(self.add_name_locator(text)).send_keys(new_name)
        wd.find_element_by_id(self.add_name_create_button_locator(text)).click()

    def get_item_list(self, item_data):
        wd = self.app.wd
        check_list = []
        # list of names and identifiers, first items in list - names
        elements = wd.find_elements_by_class_name("_3XcHlhYq6SKGkDZzMHxu2Q ")
        for element in elements:
            if element.text == item_data:
                check_list.append(element.text)
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

    def edit_song_info(self, new_data):
        wd = self.app.wd
        locator_path_name = "//form[@class='form-horizontal']/div[%s]/div/div[2]/span/li[2]/div[2]/div/div[1]/a"
        locator_path_identifier = "//form[@class='form-horizontal']/div[%s]/div/div[2]/span/li/div[2]/div[1]/div[1]/div/a"
        # edit song name
        wd.find_element_by_xpath(self.edit_name_locator(locator_path_name, div_number="2")).click()
        self.check_cancel_button("song_name_edit")
        wd.find_element_by_xpath(self.edit_name_locator(locator_path_name, div_number="2")).click()
        self.change_data_value("song_name_edit", new_data.name)
        # edit iswc
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="4")).click()
        self.check_cancel_button("song_iswc_identification_edit")
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="4")).click()
        self.change_data_value("song_iswc_identification_edit", new_data.iswc)
        # edit asap
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="5")).click()
        self.check_cancel_button("song_asap_identification_edit")
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="5")).click()
        self.change_data_value("song_asap_identification_edit", new_data.asap)
        # edit ascap
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="6")).click()
        self.check_cancel_button("song_ascap_identification_edit")
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="6")).click()
        self.change_data_value("song_ascap_identification_edit", new_data.ascap)
        # edit bmi
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="7")).click()
        self.check_cancel_button("song_bmi_identification_edit")
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="7")).click()
        self.change_data_value("song_bmi_identification_edit", new_data.bmi)
        # edit sesac
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="8")).click()
        self.check_cancel_button("song_sesac_identification_edit")
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="8")).click()
        self.change_data_value("song_sesac_identification_edit", new_data.sesac)
        # edit note

    def edit_identifier_locator(self, locator_path_identifier, div_number):
        # подстановка в %s нового знаения
        locator = locator_path_identifier
        return locator % (div_number)

    def edit_name_locator(self, locator_path_name, div_number):
        # подстановка в %s нового знаения
        locator = locator_path_name
        return locator % (div_number)

    def add_name_locator(self, text):
        # подстановка в %s нового знаения
        locator = "%s_name_new_search"
        return locator % (text)

    def add_name_create_button_locator(self, text):
        # подстановка в %s нового знаения
        locator = "%s_name_new_create"
        return locator % (text)

    def check_alert_info_tab_songwriter(self, alert_text):
        wd = self.app.wd
        element = wd.find_element_by_class_name("alert.alert-info").text
        assert element == alert_text, "Wrong alert text or songwriters tab is not empty"

    def add_songwriter(self, name):
        wd = self.app.wd
        # create songwriter
        wd.find_element_by_id("writing_new_search").click()
        wd.find_element_by_id("writing_new_search").clear()
        wd.find_element_by_id("writing_new_search").send_keys(name)
        wd.find_element_by_id("writing_new_create").click()

    def open_edit_songwriter_modal_window(self):
        # open edit songwriter modal window in the edit song page
        wd = self.app.wd
        wd.find_element_by_class_name("_3XcHlhYq6SKGkDZzMHxu2Q").click()

    def close_edit_songwriter_modal_window(self):
        # close edit songwriter modal window in the edit song page
        wd = self.app.wd
        wd.find_element_by_class_name("close").click()

    def check_songwriter_role(self, role_1, role_2):
        wd = self.app.wd
        role_list = []
        elements = wd.find_elements_by_class_name("Select-item-label")
        for element in elements:
            if element.text == role_1 or element.text == role_2:
                role_list.append(element.text)
        assert len(role_list) == 2

    def fill_identifiers_fields_in_edit_songwriter_modal_window(self, data):
        self.identifiers_field_value("songwriter_ipicae_identification_new", data.ipicae)
        self.identifiers_field_value("songwriter_asap_identification_new", data.asap)

    def edit_sonwriter_info_in_modal_window(self, new_data):
        wd = self.app.wd
        locator_path_name = "//div[@class='form-group']/div/div/div[2]/li[%s]/div[2]/div[1]/a"
        locator_path_identifier = "//div[@class='form-group']/div[%s]/div/div[2]/span/li/div[2]/div/div[1]/div/a"
        # edit song name
        wd.find_element_by_xpath(self.edit_name_locator(locator_path_name, div_number="2")).click()
        self.check_cancel_button("writing_name_edit")
        wd.find_element_by_xpath(self.edit_name_locator(locator_path_name, div_number="2")).click()
        self.change_data_value("writing_name_edit", new_data.name)
        # edit ipicae
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="2")).click()
        self.check_cancel_button("songwriter_ipicae_identification_edit")
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="2")).click()
        self.change_data_value("songwriter_ipicae_identification_edit", new_data.ipicae)
        # edit asap
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="3")).click()
        self.check_cancel_button("songwriter_asap_identification_edit")
        wd.find_element_by_xpath(self.edit_identifier_locator(locator_path_identifier, div_number="3")).click()
        self.change_data_value("songwriter_asap_identification_edit", new_data.asap)
        wd.find_element_by_class_name("btn.btn-success").click()






#    def delete_song(self):
#        wd = self.app.wd
#        wait = self.app.wait
#        wd.find_element_by_xpath("//div[@class='rubix-panel']//button[.='Delete Song']").click()
#        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='modal-footer']//button[.='Delete']"))).click()

