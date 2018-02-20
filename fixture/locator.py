__author__ = 'pavelkosicin'


class LocatorHelper:

    def __init__(self, app):
        self.app = app

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

    def choose_item_in_field_locator(self, field_locator, item):
        # fields in new deal modal window
        # "2" - Songwriters
        # "3" - Publisher
        # "4" - Licensed Territory
        # "5" - License origin
        # "6" - Media Types
        # локатор для выбора элементов в полях при заполнении формы создани new deal
        locator = "//div[@class='col-xs-12']/form[2]/div[%s]/div/div[2]/div/div[%s]"
        return locator % (field_locator, item)
