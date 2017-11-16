__author__ = 'Pavel Kosicin'


class SongwriterHelper:

    def __init__(self, app):
        self.app = app

    def create(self, songwriter):
        wd = self.app.wd
        # open tab songwriter
        wd.find_element_by_link_text("Songwriters").click()
        # create songwriter
        wd.find_element_by_id("writing_new_search").click()
        wd.find_element_by_id("writing_new_search").clear()
        wd.find_element_by_id("writing_new_search").send_keys(songwriter.name)
        wd.find_element_by_id("writing_new_create").click()
        wd.find_element_by_link_text(songwriter.name).click()
        # fill identifications
        wd.find_element_by_id("songwriter_ipicae_identification_new").click()
        wd.find_element_by_id("songwriter_ipicae_identification_new").clear()
        wd.find_element_by_id("songwriter_ipicae_identification_new").send_keys(songwriter.ipipcae)
        wd.find_element_by_id("songwriter_ipicae_identification_new_add").click()
        wd.find_element_by_id("songwriter_asap_identification_new").click()
        wd.find_element_by_id("songwriter_asap_identification_new").clear()
        wd.find_element_by_id("songwriter_asap_identification_new").send_keys(songwriter.asap)
        wd.find_element_by_id("songwriter_asap_identification_new_add").click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
        # find created songwriter, open songwriter edit page
        self.app.navigate.menu_people()
        self.find()
        # add notes
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(songwriter.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()

    def find(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys("sw_#1")
        wd.find_element_by_link_text("sw_#1").click()

