__author__ = 'pavelkosicin'


class LocatorHelper:

    def __init__(self, app):
        self.app = app

    def note_edit_button_locator(self, div_number):
        locator = "//form[@class='form-horizontal']/div[10]/div/div/div[2]/div[%s]/div/button"
        return locator % (div_number)

    def item_in_note_dropdown_menu_locator(self, div_number, li_number):
        locator = "//form[@class='form-horizontal']/div[10]/div/div/div[2]/div[%s]/div/ul/li[%s]/a"
        return locator % (div_number, li_number)

    def edit_identifier(self, locator_path_identifier, div_number):
        # подстановка в %s нового знаения
        locator = locator_path_identifier
        return locator % (div_number)

    def edit_name(self, locator_path_name, div_number):
        # подстановка в %s нового знаения
        locator = locator_path_name
        return locator % (div_number)

    def add_name(self, text):
        # подстановка в %s нового знаения
        locator = "%s_name_new_search"
        return locator % (text)

    def add_name_create_button(self, text):
        # подстановка в %s нового знаения
        locator = "%s_name_new_create"
        return locator % (text)

    def add_entity_link(self, text):
        # подстановка в %s нового знаения
        # локатор для методов добавления в песню сущностей (songwriter, publisher)
        locator = "%s_new_search"
        return locator % (text)

    def add_entity_link_create_button(self, text):
        # подстановка в %s нового знаения
        locator = "%s_new_create"
        return locator % (text)

    def new_deal_entity_locator(self, entity_id):
        locator = "//*[@id='%s']/div[1]"
        return locator % (entity_id)

    def choose_item_in_field_media_type_locator(self, field_locator, item):
        # fields in new deal modal window
        # "2" - Songwriters
        # "3" - Publisher
        # "4" - Licensed Territory
        # "5" - License origin
        # "6" - Media Types
        # локатор для выбора элементов в полях при заполнении формы создани new deal
        locator = "//div[@class='col-xs-12']/form[2]/div[%s]/div/div[2]/div/div[%s]"
        return locator % (field_locator, item)

    def dropdown_menu_add_share_deal_locator(self, div_number):
        locator = "//div[@class='col-sm-12']/div[2]/span/div[%s]/div/div/table/tbody/tr/td[2]/h3/div/button"
        return locator % (div_number)

    def choose_share_deal_locator(self, div_number, li_number):
        locator = "//div[@class='col-sm-12']/div[2]/span/div[%s]/div/div/table/tbody/tr/td[2]/h3/div/ul/li[%s]/a"
        return locator % (div_number, li_number)

    def share_button_locator(self, div_number):
        locator = "//div[@class='col-sm-12']/div[2]/span/div[%s]/div/div/div/span/div/div/div[2]/div/button"
        return locator % (div_number)

    def share_button_color_locator(self, color):
        locator = "dropdown-toggle.btn-%s.btn.btn-inline"
        return locator % (color)

    def item_in_share_dropdown_menu_locator(self, div_number, li_number):
        locator = "//div[@class='col-sm-12']/div[2]/span/div[%s]/div/div/div/span/div/div/div[2]/div/ul/li[%s]/a"
        return locator % (div_number, li_number)

    def deal_edit_button_locator(self, div_number):
        locator = "//div[@class='col-sm-12']/div[2]/span/div[%s]/div/div/div/div/div/table/tbody/tr/td[6]/div[2]/button"
        return locator % (div_number)

    def item_in_deal_dropdown_menu_locator(self, div_number, li_number):
        locator = "//div[@class='col-sm-12']/div[2]/span/div[%s]/div/div/div/div/div/table/tbody/tr/td[6]/div[2]/ul/li[%s]/a"
        return locator % (div_number, li_number)

    def remove_media_type_button_locator(self, div_number):
        locator = "//div[@id='media_type_select']/div[%s]/span[2]"
        return locator % (div_number)

    def add_directive_button_locator(self, div_number):
        locator = "//form[@class='form-horizontal']/div[2]/div[%s]/div[2]/div/div[1]/h4/button"
        return locator % (div_number)

    def directives_action_button_locator(self, div_1_number, div_2_number):
        locator = "//form[@class='form-horizontal']/div[2]/div[%s]/div[2]/div/div[2]/span/div[%s]/div/div/div/div[2]" +\
                "/div/div/div[2]/div/div/button"
        return locator % (div_1_number, div_2_number)

    def item_in_directive_action_menu_locator(self, div_1_number, div_2_number, li_number):
        locator = "//form[@class='form-horizontal']/div[2]/div[%s]/div[2]/div/div[2]/span/div[%s]/div/div/div/div[2]" +\
                "/div/div/div[2]/div/div/ul/li[%s]/a"
        return locator % (div_1_number, div_2_number, li_number)

    def choose_songwriter_copyright_collective_locator(self, div_number):
        locator = "//form[@class='form-horizontal']/div[2]/div[%s]"
        return locator % (div_number)

    def cc_action_button_locator(self, div_number):
        locator = "//form[@class='form-horizontal']/div[2]/div[%s]/div[2]/span/div/div/div/div/div/div[2]/div[1]/div[2]" +\
                  "/div/div/button"
        return locator % (div_number)

    def item_in_cc_action_menu_locator(self, div_number, li_number):
        locator = "//form[@class='form-horizontal']/div[2]/div[%s]/div[2]/span/div/div/div/div/div/div[2]/div[1]/div[2]" +\
                 "/div/div/ul/li[%s]/a"
        return locator % (div_number, li_number)

