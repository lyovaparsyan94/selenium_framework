import pytest

from helpers.helpers import get_webdriver


@pytest.fixture(scope='class')
def get_driver(request):
    driver = get_webdriver()
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()
