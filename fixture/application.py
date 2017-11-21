__author__ = 'Pavel Kosicin'
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from fixture.session import SessionHelper
from fixture.song import SongHelper
from fixture.navigate import NavigateHelper
from fixture.songwriter import SongwriterHelper
from fixture.artist import ArtistHelper
from fixture.recording import RecordingHelper
from fixture.search import SearchHelper
from fixture.publisher import PublisherHelper
from fixture.label import LabelHelper
from fixture.collective import CollectiveHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.wait = WebDriverWait(self.wd, 10)
        self.session = SessionHelper(self)
        self.song = SongHelper(self)
        self.navigate = NavigateHelper(self)
        self.songwriter = SongwriterHelper(self)
        self.artist = ArtistHelper(self)
        self.recording = RecordingHelper(self)
        self.search = SearchHelper(self)
        self.publisher = PublisherHelper(self)
        self.label = LabelHelper(self)
        self.collective = CollectiveHelper(self)

    def destroy(self):
        self.wd.quit()
