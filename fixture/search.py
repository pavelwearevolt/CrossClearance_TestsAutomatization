__author__ = 'pavelkosicin'


class SearchHelper:

    def __init__(self, app):
        self.app = app

    def search_query(self, query):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(query)

    def find_entity(self, query):
        wd = self.app.wd
        self.search_query(query)
        wd.find_element_by_link_text(query.title()).click()

