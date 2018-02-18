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
        # add identifiers
        self.identifiers_field_value("song_iswc_identification_new", data.iswc)
        self.identifiers_field_value("song_asap_identification_new", data.asap)
        self.identifiers_field_value("song_ascap_identification_new", data.ascap)
        self.identifiers_field_value("song_bmi_identification_new", data.bmi)
        self.identifiers_field_value("song_sesac_identification_new", data.sesac)

    def add_note(self, text):
        wd = self.app.wd
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(text.note)
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
        wd.find_element_by_id(self.app.locator.add_name(text)).click()
        wd.find_element_by_id(self.app.locator.add_name(text)).clear()
        wd.find_element_by_id(self.app.locator.add_name(text)).send_keys(new_name)
        wd.find_element_by_id(self.app.locator.add_name_create_button(text)).click()

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
        locator_path_name = "//form[@class='form-horizontal']/div[2]/div/div[2]/span/li[%s]/div[2]/div/div[1]/a"
        locator_path_identifier = "//form[@class='form-horizontal']/div[%s]/div/div[2]/span/li/div[2]/div[1]/div[1]/div/a"
        time.sleep(2)
        # edit song name
        wd.find_element_by_xpath(self.app.locator.edit_name(locator_path_name, div_number="2")).click()
        self.check_cancel_button("song_name_edit")
        wd.find_element_by_xpath(self.app.locator.edit_name(locator_path_name, div_number="2")).click()
        self.change_data_value("song_name_edit", new_data.name)
        # edit iswc
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="4")).click()
        self.check_cancel_button("song_iswc_identification_edit")
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="4")).click()
        self.change_data_value("song_iswc_identification_edit", new_data.iswc)
        # edit asap
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="5")).click()
        self.check_cancel_button("song_asap_identification_edit")
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="5")).click()
        self.change_data_value("song_asap_identification_edit", new_data.asap)
        # edit ascap
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="6")).click()
        self.check_cancel_button("song_ascap_identification_edit")
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="6")).click()
        self.change_data_value("song_ascap_identification_edit", new_data.ascap)
        # edit bmi
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="7")).click()
        self.check_cancel_button("song_bmi_identification_edit")
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="7")).click()
        self.change_data_value("song_bmi_identification_edit", new_data.bmi)
        # edit sesac
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="8")).click()
        self.check_cancel_button("song_sesac_identification_edit")
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="8")).click()
        self.change_data_value("song_sesac_identification_edit", new_data.sesac)
        # edit note

    def check_alert_info(self, alert_text):
        wd = self.app.wd
        element = wd.find_element_by_class_name("alert.alert-info").text
        assert element == alert_text, "Wrong alert text or tab is not empty"

    def add_entity_link(self, name, text):
        wd = self.app.wd
        wait = self.app.wait
        # метод для добавления сущности в песню (songwriter or publisher)
        wd.find_element_by_id(self.app.locator.add_entity_link(text)).click()
        wd.find_element_by_id(self.app.locator.add_entity_link(text)).clear()
        wd.find_element_by_id(self.app.locator.add_entity_link(text)).send_keys(name)
        wd.find_element_by_id(self.app.locator.add_entity_link_create_button(text)).click()
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, name)))

    def open_edit_entity_modal_window(self):
        # open edit songwriter modal window in the edit song page
        wd = self.app.wd
        wd.find_element_by_class_name("_3XcHlhYq6SKGkDZzMHxu2Q").click()

    def close_edit_entity_modal_window(self):
        # close edit songwriter modal window in the edit song page
        wd = self.app.wd
        wd.find_element_by_class_name("close").click()

    def check_songwriter_default_role(self, role_1, role_2):
        wd = self.app.wd
        role_list = []
        elements = wd.find_elements_by_class_name("Select-item-label")
        for element in elements:
            if element.text == role_1 or element.text == role_2:
                role_list.append(element.text)
        assert len(role_list) == 2

    def edit_songwriter_roles(self):
        wd = self.app.wd
        wd.find_element_by_class_name("Select-arrow").click()
        wd.find_element_by_id("writing_select_role_item_3").click()
        wd.find_element_by_id("writing_select_role_item_12").click()
        wd.find_element_by_id("writing_select_role_clear").click()
        wd.find_element_by_id("writing_select_role_item_1").click()
        wd.find_element_by_id("writing_select_role_item_2").click()

    def fill_identifiers_fields_in_edit_entity_modal_window(self, data, entity):
        self.identifiers_field_value(entity + "_ipicae_identification_new", data.ipicae)
        self.identifiers_field_value(entity + "_asap_identification_new", data.asap)

    def edit_entity_info_in_modal_window(self, new_data, entity_name, entity_identifier):
        wd = self.app.wd
        wait = self.app.wait
        # xpath
        locator_path_name = "//div[@class='form-group']/div/div/div[2]/li[%s]/div[2]/div[1]/a"
        locator_path_identifier = "//div[@class='form-group']/div[%s]/div/div[2]/span/li/div[2]/div/div[1]/div/a"

        wait.until(EC.presence_of_element_located((By.XPATH, self.app.locator.edit_identifier(locator_path_identifier,
                                                                                              div_number="2"))))
        wait.until(EC.presence_of_element_located((By.XPATH, self.app.locator.edit_identifier(locator_path_identifier,
                                                                                              div_number="3"))))
        # edit song name
        wd.find_element_by_xpath(self.app.locator.edit_name(locator_path_name, div_number="2")).click()
        self.check_cancel_button(entity_name + "_name_edit")
        wd.find_element_by_xpath(self.app.locator.edit_name(locator_path_name, div_number="2")).click()
        self.change_data_value(entity_name + "_name_edit", new_data.name)
        # edit ipicae
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="2")).click()
        self.check_cancel_button(entity_identifier + "_ipicae_identification_edit")
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="2")).click()
        self.change_data_value(entity_identifier + "_ipicae_identification_edit", new_data.ipicae)
        # edit asap
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="3")).click()
        self.check_cancel_button(entity_identifier + "_asap_identification_edit")
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="3")).click()
        self.change_data_value(entity_identifier + "_asap_identification_edit", new_data.asap)
        wd.find_element_by_class_name("btn.btn-success").click()

#    def delete_song(self):
#        wd = self.app.wd
#        wait = self.app.wait
#        wd.find_element_by_xpath("//div[@class='rubix-panel']//button[.='Delete Song']").click()
#        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='modal-footer']//button[.='Delete']"))).click()
