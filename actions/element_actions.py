from time import sleep

from selenium.common.exceptions import (
    ElementNotInteractableException,
    ElementClickInterceptedException
)

from actions.find_actions import FindActions


class ElementActions:

    @staticmethod
    def click(*, driver, locator, repeat=3, timeout=20):
        ok = False
        repeat_count = 0
        while not ok and repeat_count < repeat:
            try:
                repeat_count += 1
                element = FindActions().find_element(driver=driver, locator=locator, timeout=timeout)
                element.click()
                ok = True
            except (ElementNotInteractableException, ElementClickInterceptedException) as e:
                # firefox solution
                # TODO add logging
                sleep(0.3)

    @staticmethod
    def get_text(*, element=None, driver=None, locator=None, timeout=10):
        # If element is not provided you should provide driver and locator
        if not element:
            element = FindActions().find_element(driver=driver, locator=locator, timeout=timeout)
        return element.text

    @staticmethod
    def put_text(*, text, element=None, driver=None, locator=None, timeout=10):
        # If element is not provided you should provide driver and locator
        if not element:
            element = FindActions().find_element(driver=driver, locator=locator, timeout=timeout)
        element.send_keys(text)

    @staticmethod
    def get_attribute(*, attribute, element=None, driver=None, locator=None, timeout=10):
        # If element is not provided you should provide driver and locator
        if not element:
            element = FindActions().find_element(driver=driver, locator=locator, timeout=timeout)
        return element.get_attribute(attribute)

