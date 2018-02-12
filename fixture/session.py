__author__ = 'pavelkosicin'
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.navigate.open_home_page()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(username)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//div[@class='sign-in-control-box']//button[.='Log In']").click()

    def logout(self):
        wd = self.app.wd
        wait = self.app.wait
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logout"))).click()
        wd.find_element_by_css_selector("button.btn.btn-success").click()
