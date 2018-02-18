__author__ = 'pavelkosicin'


class NavigateHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("https://cross-edit-staging-frontend.herokuapp.com/")

    def menu_global_search(self):
        wd = self.app.wd
        wd.find_element_by_name("Global search").click()

    def switch_to_tab(self, tab_name):
        wd = self.app.wd
        wd.find_element_by_link_text(tab_name).click()
