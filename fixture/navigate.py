__author__ = 'Pavel Kosicin'


class NavigateHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("https://cross-edit-qa-frontend.herokuapp.com/")

    def menu_global_search(self):
        wd = self.app.wd
        wd.find_element_by_name("Global search").click()

    def menu_people(self):
        wd = self.app.wd
        wd.find_element_by_name("People").click()
