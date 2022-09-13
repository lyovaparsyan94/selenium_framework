from pages.base_page import BasePage
from locators.main import MainePageLocators

from exceptions import PageIsNotLoaded


class MainPage(BasePage):

    def __init__(self, *, driver):
        super().__init__(driver=driver)
        self.locators = MainePageLocators()

    def __call__(self, *args, **kwargs):
        locator = self.locators.logo
        success = self.load(locator=locator)
        if not success:
            url = self.get_page_url()
            raise PageIsNotLoaded(url=url)

    def function(self):
        from time import sleep
        sleep(3)
