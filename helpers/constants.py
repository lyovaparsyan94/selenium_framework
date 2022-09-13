from selenium.webdriver import (
    Chrome,
    Firefox,
    Safari
)

from selenium.webdriver import (
    ChromeOptions,
    FirefoxOptions
)

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

DRIVERS_MAPPER = {
    'chrome': {
        'webdriver': Chrome,
        'manager': ChromeDriverManager,
        'options': ChromeOptions,
        'service': ChromeService,
    },
    'firefox': {
        'webdriver': Firefox,
        'manager': GeckoDriverManager,
        'options': FirefoxOptions,
        'service': FirefoxService,
    },
    'safari': {
        'webdriver': Safari,
    }
}

