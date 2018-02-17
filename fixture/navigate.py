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

    def tab_general_info(self):
        wd = self.app.wd
        wd.find_element_by_link_text("General Info").click()

    def tab_songwriters(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Songwriters").click()

    def tab_publishers(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Publishers").click()

    def tab_directives(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Directives").click()

    def tab_copyrigt_collective_info(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Copyright Collective Info").click()

    def tab_master_recordings(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Master Recordings").click()
