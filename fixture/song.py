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

    def check_fields_value_default(self, name):
        wd = self.app.wd
        default_value = []
        fields_value = wd.find_elements_by_class_name("list-group")
        for value in fields_value:
            default_value.append(value.text)
        while '' in default_value:
            default_value.remove('')
        assert len(default_value) == 2, "At creation the superfluous fields are filled"
        assert name in default_value, "Does not match the values that were entered when creating"

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

    def check_filled_fields_value(self, name, iswc, asap, ascap, bmi, sesac):
        wd = self.app.wd
        default_value = []
        fields_value = wd.find_elements_by_class_name("list-group")
        for value in fields_value:
            default_value.append(value.text)
        while '' in default_value:
            default_value.remove('')
        assert len(default_value) == 7, "Not all fields are filled in"
        assert name in default_value, "Does not match the value entered during filling"
        assert iswc in default_value, "Does not match the value entered during filling"
        assert asap in default_value, "Does not match the value entered during filling"
        assert ascap in default_value, "Does not match the value entered during filling"
        assert bmi in default_value, "Does not match the value entered during filling"
        assert sesac in default_value, "Does not match the value entered during filling"

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
        time.sleep(3)

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
        # div_number - sequence number of the song name, for example, if the song has only one name div_number - "1"
        # if the song has several names, if want choose second name - div_number - "2", the third - div_number - "3", ect.
        wd.find_element_by_xpath(self.app.locator.edit_name(locator_path_name, div_number="1")).click()
        self.check_cancel_button("song_name_edit")
        wd.find_element_by_xpath(self.app.locator.edit_name(locator_path_name, div_number="1")).click()
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

    def open_note_dropdown_menu(self, note_number):
        wd = self.app.wd
        # note_number - note's sequence number on the song editing page (for example first note)
        wd.find_element_by_xpath(self.app.locator.note_edit_button_locator(div_number=note_number)).click()

    def choose_item_in_note_dropdown_menu(self, note_number, item_number):
        wd = self.app.wd
        # note_number - note's sequence number on the song editing page (for example first note)
        # item_number - button edit or remove note
        # 1 - edit
        # 3 - remove
        wd.find_element_by_xpath(self.app.locator.item_in_note_dropdown_menu_locator(
            div_number=note_number, li_number=item_number)).click()

    def edit_note_text(self, text):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/textarea").click()
        wd.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/textarea").clear()
        wd.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/textarea").send_keys(text.note)

    def button_cancel_in_edit_note_modal_window(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[3]/button[2]").click()

    def button_edit_in_edit_note_modal_window(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[3]/button[1]").click()
        time.sleep(3)

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
        time.sleep(3)

    def open_edit_entity_modal_window(self):
        # open edit songwriter or publisher modal window in the edit song page
        # entity_number - number of songwriter or publisher
        # entity's sequence number on the song editing page (for example first songwriter)
        wd = self.app.wd
        wd.find_element_by_class_name("_3XcHlhYq6SKGkDZzMHxu2Q").click()

    def check_fields_value_default_in_entity_modal_window(self, name):
        wd = self.app.wd
        default_value = []
        # switch to the desired element
        modal_window = wd.find_element_by_class_name("modal-content")
        # Use a variable modal_window to specify which element is searched for elements
        fields_value = modal_window.find_elements_by_class_name("list-group")
        for value in fields_value:
            default_value.append(value.text)
        while '' in default_value:
            default_value.remove('')
        assert len(default_value) == 2, "At creation the superfluous fields are filled"
        assert name in default_value, "Does not match the values that were entered when creating"

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
        wait = self.app.wait
        locator_path_identifier = "//div[@class='form-group']/div[%s]/div/div[2]/span/li/div[2]/div/div[1]/div/a"
        self.identifiers_field_value(entity + "_ipicae_identification_new", data.ipicae)
        self.identifiers_field_value(entity + "_asap_identification_new", data.asap)
        wait.until(EC.presence_of_element_located((By.XPATH, self.app.locator.edit_identifier(locator_path_identifier,
                                                                                              div_number="2"))))
        wait.until(EC.presence_of_element_located((By.XPATH, self.app.locator.edit_identifier(locator_path_identifier,
                                                                                              div_number="3"))))

    def edit_entity_info_in_modal_window(self, new_data, entity_name, entity_identifier):
        wd = self.app.wd
        wait = self.app.wait
        # xpath
        locator_path_name = "//div[@class='form-group']/div/div/div[2]/li[%s]/div[2]/div[1]/a"
        locator_path_identifier = "//div[@class='form-group']/div[%s]/div/div[2]/span/li/div[2]/div/div[1]/div/a"
        # edit song name
        # div_number - sequence number of the entity (songwriter name or publisher name) name
        # for example, if the entity has only one name div_number - "1"
        # if the entity has several names, if want choose second name - div_number - "2", the third - div_number - "3", ect.
        wd.find_element_by_xpath(self.app.locator.edit_name(locator_path_name, div_number="1")).click()
        self.check_cancel_button(entity_name + "_name_edit")
        wd.find_element_by_xpath(self.app.locator.edit_name(locator_path_name, div_number="1")).click()
        self.change_data_value(entity_name + "_name_edit", new_data.name)
        # edit ipicae
        # div_number - number of the corresponding identifier field
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="2")).click()
        self.check_cancel_button(entity_identifier + "_ipicae_identification_edit")
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="2")).click()
        self.change_data_value(entity_identifier + "_ipicae_identification_edit", new_data.ipicae)
        # edit asap
        # div_number - number of the corresponding identifier field
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="3")).click()
        self.check_cancel_button(entity_identifier + "_asap_identification_edit")
        wd.find_element_by_xpath(self.app.locator.edit_identifier(locator_path_identifier, div_number="3")).click()
        self.change_data_value(entity_identifier + "_asap_identification_edit", new_data.asap)

    def check_filled_fields_in_entity_modal_window(self, name_value, ipicae_value, asap_value):
        wd = self.app.wd
        default_value = []
        # switch to the desired element
        modal_window = wd.find_element_by_class_name("modal-content")
        # Use a variable modal_window to specify which element is searched for elements
        fields_value = modal_window.find_elements_by_class_name("list-group")
        for value in fields_value:
            default_value.append(value.text)
        while '' in default_value:
            default_value.remove('')
        assert len(default_value) == 4, "At creation the superfluous fields are filled"
        assert name_value in default_value, "Does not match the values that were entered when creating"
        assert ipicae_value in default_value, "Does not match the values that were entered when creating"
        assert asap_value in default_value, "Does not match the values that were entered when creating"

    def open_dropdown_menu(self, entity_number):
        # drop-down menu to add share or deal
        wd = self.app.wd
        wd.find_element_by_xpath(self.app.locator.dropdown_menu_add_share_deal_locator(div_number=entity_number)).click()

    def open_modal_window(self, entity_number, function_number):
        # open modal window adding share or deal
        # entity_number - number of songwriter or publisher
        # entity's sequence number on the song editing page (for example first songwriter)
        # function_number - button share or button deal
        # TAB "SONGWRITERS"
        # 1 - share
        # 2 - deal
        # 4 - remove
        # TAB "PUBLISHERS"
        # 1 - deal
        # 3 - remove
        wd = self.app.wd
        wd.find_element_by_xpath(self.app.locator.choose_share_deal_locator(div_number=entity_number,
                                                                            li_number=function_number)).click()

    def close_modal_window_button_close(self):
        # close the window using the cross in the upper left corner
        wd = self.app.wd
        wd.find_element_by_class_name("close").click()

    def close_modal_window_button_cancel(self):
        # close the window using the button cancel
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[3]/span/button[1]").click()

    def fill_share_form(self, territory_field_id, territory, territory_locator, percentage_field_id, percentage):
        self.fill_territory_field(territory, territory_locator, territory_field_id)
        self.fill_percentage_field(percentage_field_id, percentage)
        self.save_button()
        time.sleep(3)

    def fill_territory_field(self, territory_field_id, territory, territory_locator):
        wd = self.app.wd
        wd.find_element_by_id(territory_field_id).click()
        wd.find_element_by_id(territory_field_id).clear()
        wd.find_element_by_id(territory_field_id).send_keys(territory)
        wd.find_element_by_class_name(territory_locator).click()

    def fill_percentage_field(self, percentage_field_id, percentage):
        wd = self.app.wd
        wd.find_element_by_id(percentage_field_id).click()
        wd.find_element_by_id(percentage_field_id).clear()
        wd.find_element_by_id(percentage_field_id).send_keys(percentage)

    def check_entity_in_new_deal_modal_window(self, entity_id, entity_name):
        wd = self.app.wd
        element = wd.find_element_by_xpath(self.app.locator.new_deal_entity_locator(entity_id)).text
        assert element == entity_name

    def fill_field_in_new_deal_directives_modal_window(self, field_id, field_value, field_locator):
        wd = self.app.wd
        items_list = []
        # выбрать какое поле будет заполнено
        wd.find_element_by_id(field_id).click()
        elements = wd.find_elements_by_class_name("Select-option")
        for element in elements:
            items_list.append(element.text)
        item_index = items_list.index(field_value)
        if item_index == 0:
            wd.find_element_by_xpath(self.app.locator.choose_item_in_field_media_type_locator(field_locator, item_index + 1)).click()
        else:
            wd.find_element_by_xpath(self.app.locator.choose_item_in_field_media_type_locator(field_locator, item_index + 1)).click()

    def save_button(self):
        wd = self.app.wd
        wd.find_element_by_class_name("btn.btn-success").click()

    def clear_field_in_new_deal_modal_window(self, field_id):
        wd = self.app.wd
        wd.find_element_by_id(field_id + "_clear").click()

    def open_share_dropdown_menu(self, songwriter_number):
        wd = self.app.wd
        wd.find_element_by_xpath(self.app.locator.share_button_locator(div_number=songwriter_number)).click()

    def choose_item_in_share_dropdown_menu(self, songwriter_number, item_number):
        wd = self.app.wd
        wd.find_element_by_xpath(self.app.locator.item_in_share_dropdown_menu_locator(
            div_number=songwriter_number, li_number=item_number)).click()

    def clear_share_territory_field(self):
        wd = self.app.wd
        wd.find_element_by_id("territory_cancel").click()
        assert wd.find_element_by_id("territory_search").get_attribute("placeholder") == "Start typing to search...", \
            "Wrong placeholder text or field does not cleared"

    def open_deal_dropdown_menu(self, entity_number):
        wd = self.app.wd
        # entity_number - number of songwriter or publisher
        # entity's sequence number on the song editing page (for example first songwriter)
        wd.find_element_by_xpath(self.app.locator.deal_edit_button_locator(div_number=entity_number)).click()

    def choose_item_in_deal_dropdown_menu(self, entity_number, item_number):
        wd = self.app.wd
        # entity_number - number of songwriter or publisher (can edit deal in tab "Songwriters" and tab "Publishers")
        # entity's sequence number on the song editing page (for example first songwriter)
        wd.find_element_by_xpath(self.app.locator.item_in_deal_dropdown_menu_locator(
            div_number=entity_number, li_number=item_number)).click()

    def remove_one_of_chosen_media_type(self, type_number):
        wd = self.app.wd
        # remove one of chosen media type
        # type_number - sequence number of chosen media types in field Media Types
        wd.find_element_by_xpath(self.app.locator.remove_media_type_button_locator(div_number=type_number)).click()

    def open_add_directives_modal_window(self, songwriter_number):
        # songwriter_number - sequence number of songwriter
        wd = self.app.wd
        wd.find_element_by_xpath(self.app.locator.add_directive_button_locator(div_number=songwriter_number)).click()

    def choose_media_types_directives(self, field_id, item_number):
        wd = self.app.wd
        wd.find_element_by_id(field_id).click()
        wd.find_element_by_id("media_type_select_item_" + item_number).click()

    def open_directive_actions_menu(self, songwriter_number, directive_number):
        wd = self.app.wd
        # songwriter_number - sequence number of songwriter
        # directive_number - sequence number of directive in current songwriter
        wd.find_element_by_xpath(self.app.locator.directives_action_button_locator(
            div_1_number=songwriter_number,
            div_2_number=directive_number
            )).click()

    def choose_item_in_action_menu(self, songwriter_number, directive_number, item_number):
        wd = self.app.wd
        # songwriter_number - sequence number of songwriter
        # directive_number - sequence number of directive in current songwriter
        # item_number - number of item in directive dropdown menu "actions"
        wd.find_element_by_xpath(self.app.locator.item_in_directive_action_menu_locator(
            div_1_number=songwriter_number,
            div_2_number=directive_number,
            li_number=item_number
            )).click()

    def clear_directive_field(self, field_name):
        wd = self.app.wd
        # field_name - name of the field in edit directive modal window:
        # care_of
        # licensee
        # payee
        # payment_recipient
        # license_origin_select
        wd.find_element_by_id(field_name + "_cancel").click()

    def close_directive_modal_window_button_cancel(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/div[2]/div[2]/button[1]").click()

    def create_new_entity_in_directive_modal_window(self, field_name, entity_name):
        wd = self.app.wd
        wd.find_element_by_id(field_name + "_search").click()
        wd.find_element_by_id(field_name + "_search").send_keys(entity_name)
        wd.find_element_by_id(field_name + "_create").click()

    def open_copyright_collective_modal_window(self, songwriter_number):
        wd = self.app.wd
        # choose songwriter for which will be added copyright collectives
        songwriter = wd.find_element_by_xpath(self.app.locator.choose_songwriter_copyright_collective_locator(
            div_number=songwriter_number
            ))
        songwriter.find_element_by_id("add-collective").click()

    def add_copyright_collective(self, collective_name, collective):
        wd = self.app.wd
        wd.find_element_by_id("undefined_search").click()
        # search collective by name
        wd.find_element_by_id("undefined_search").send_keys(collective_name)
        # choose collective from search result, choose collective in dropdown menu by "class_name"
        wd.find_element_by_class_name(collective).click()




#    def delete_song(self):
#        wd = self.app.wd
#        wait = self.app.wait
#        wd.find_element_by_xpath("//div[@class='rubix-panel']//button[.='Delete Song']").click()
#        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='modal-footer']//button[.='Delete']"))).click()
