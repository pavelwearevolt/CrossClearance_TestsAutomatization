__author__ = 'Pavel Kosicin'
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from fixture.session import SessionHelper
from fixture.song import SongHelper
from fixture.navigate import NavigateHelper
from fixture.songwriter import SongwriterHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.wait = WebDriverWait(self.wd, 10)
        self.session = SessionHelper(self)
        self.song = SongHelper(self)
        self.navigate = NavigateHelper(self)
        self.songwriter = SongwriterHelper(self)

    def destroy(self):
        self.wd.quit()
