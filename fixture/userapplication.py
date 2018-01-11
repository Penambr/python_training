from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.sessionusers import SessionHelperUsers
from fixture.users import UserHelper


class Userapplication:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.sessionusers = SessionHelperUsers(self)
        self.users = UserHelper(self)

    def open_webpage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()