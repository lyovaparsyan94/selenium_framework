from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class WaitActions:
    def __init__(self):
        self.conditions = {
            'visible': EC.visibility_of_element_located,
            'visible_any': EC.visibility_of_any_elements_located,
            'visible_all': EC.visibility_of_all_elements_located,
            'invisible': EC.invisibility_of_element_located,
            'presence': EC.presence_of_element_located
        }

    def wait_until(self, *, driver, locator, condition='visible', timeout=15):
        expected_condition = self.get_condition(condition=condition)
        element = None
        try:
            element = WebDriverWait(driver, timeout=timeout).until(
                expected_condition(locator=locator)
            )
        except TimeoutException as e:
            # TODO add logging
            print(f'TimeoutException, reason: {e}')
        return element

    def get_condition(self, *, condition):
        return self.conditions.get(condition)
