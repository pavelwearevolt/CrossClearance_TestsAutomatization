__author__ = 'Pavel Kosicin'


class NavigateHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("https://cross-auth-staging.herokuapp.com/?redirect_uri=https%3A%2F%2Fcross-edit-staging-frontend.herokuapp.com%2F")

    def return_to_global_search(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Global search").click()
