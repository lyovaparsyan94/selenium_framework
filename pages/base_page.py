import os
from selenium.common.exceptions import WebDriverException

from actions.wait_actions import WaitActions


class BasePage:

    def __init__(self, driver, url=None):
        self.driver = driver
        self.base_url = url if url else os.environ['url']
        self.page = ''
        self.wait_action = WaitActions()

    def get_page_url(self):
        return f'{self.base_url}/{self.page}'

    def get_main_url(self):
        return self.base_url

    def load(self, *, locator):
        success = False
        try:
            url = self.get_page_url()
            self.driver.get(url)
            self.wait_action.wait_(driver=self.driver, locator=locator, condition='presence')
            success = True
        except WebDriverException as e:
            # TODO add logging
            print(f'WebDriverException, reason: {e}')
        return success
