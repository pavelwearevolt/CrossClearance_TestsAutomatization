__author__ = 'Pavel Kosicin'


class SearchHelper:

    def __init__(self, app):
        self.app = app

    def global_search(self, name):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(name)
        wd.find_element_by_link_text(name.title()).click()

    def object_search(self, name):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(name)
        wd.find_element_by_link_text(name).click()
