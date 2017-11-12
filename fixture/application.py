__author__ = 'Pavel Kosicin'
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("https://cross-auth-staging.herokuapp.com/?redirect_uri=https%3A%2F%2Fcross-edit-staging-frontend.herokuapp.com%2F")

    def create(self, song):
        wd = self.wd
        # create song
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(song.name)
        wd.find_element_by_css_selector("button.btn.btn-green").click()
        wd.find_element_by_xpath("//div[@class='modal-body']//button[.='song']").click()
        # song modification
        wd.find_element_by_id("song_iswc_identification_new").click()
        wd.find_element_by_id("song_iswc_identification_new").clear()
        wd.find_element_by_id("song_iswc_identification_new").send_keys(song.iswc)
        wd.find_element_by_id("song_iswc_identification_new_add").click()
        wd.find_element_by_id("song_asap_identification_new").click()
        wd.find_element_by_id("song_asap_identification_new").clear()
        wd.find_element_by_id("song_asap_identification_new").send_keys(song.asap)
        wd.find_element_by_id("song_asap_identification_new_add").click()
        wd.find_element_by_id("song_ascap_identification_new").click()
        wd.find_element_by_id("song_ascap_identification_new").clear()
        wd.find_element_by_id("song_ascap_identification_new").send_keys(song.ascap)
        wd.find_element_by_id("song_ascap_identification_new_add").click()
        wd.find_element_by_id("song_bmi_identification_new").click()
        wd.find_element_by_id("song_bmi_identification_new").clear()
        wd.find_element_by_id("song_bmi_identification_new").send_keys(song.bmi)
        wd.find_element_by_id("song_bmi_identification_new_add").click()
        wd.find_element_by_id("song_sesac_identification_new").click()
        wd.find_element_by_id("song_sesac_identification_new").clear()
        wd.find_element_by_id("song_sesac_identification_new").send_keys(song.sesac)
        wd.find_element_by_id("song_sesac_identification_new_add").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").click()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").clear()
        wd.find_element_by_css_selector("textarea.form-control._3N_4MUdz6Is-muISLxDGRP").send_keys(song.note)
        wd.find_element_by_xpath("//div[@class='_30d-pYB2dYPjd0XNrEQjVs']//button[.='Send']").click()
        self.return_to_global_search()

    def return_to_global_search(self):
        wd = self.wd
        wd.find_element_by_link_text("Global search").click()

    def find(self, name):
        wd = self.wd
        # find created song
        wd.find_element_by_css_selector("input.form-control").click()
        wd.find_element_by_css_selector("input.form-control").clear()
        wd.find_element_by_css_selector("input.form-control").send_keys(name)
        # choose found song
        wd.find_element_by_link_text(name.title()).click()

    def destroy(self):
        self.wd.quit()
