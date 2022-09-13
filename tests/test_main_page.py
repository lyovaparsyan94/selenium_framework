import pytest

from pages.main_page import MainPage


@pytest.mark.usefixtures('get_driver')
class TestMainPage:

    def setup(self):
        self.page = MainPage(driver=self.driver)
        self.page()

    @pytest.mark.hello
    def test_function_1(self):
        self.page.function()

    @pytest.mark.bye
    def test_function_2(self):
        self.page.function()

    @pytest.mark.hello
    def test_function_3(self):
        self.page.function()