from selenium.webdriver.common.by import By

from actions.wait_actions import WaitActions


class FindActions:

    def __init__(self):
        self.actions = {
            'single': 'find_element',
            'multiple': 'find_elements',
        }

    def find_element(self, *, driver, locator, action='single', timeout=15):
        element = None
        action = self.get_action(action=action)
        try:
            WaitActions().wait_until(driver=driver, locator=locator, timeout=timeout)
            element = getattr(driver, action)(*locator)
        except Exception as e:
            print(f'Unknown exception while finding element, reason: {e}')
        return element

    def find_element_from_element(self, *, parent, selector, by=By.CSS_SELECTOR, action='single'):
        element = None
        action = self.get_action(action=action)
        try:
            element = getattr(parent, action)(by=by, value=selector)
        except Exception as e:
            print(f'Unknown exception while finding element form element, reason: {e}')
        return element

    def check_element_existence(self, *, driver, locator, timeout=10):
        element = self.find_element(driver=driver, locator=locator, timeout=timeout)
        return bool(element)

    def get_action(self, *, action):
        return self.actions.get(action)
