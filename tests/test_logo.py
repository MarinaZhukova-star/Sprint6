 #Проверка логотипов

import allure
import pytest

from url import SCOOTER_ORDER_URL, YA_DZEN_URL
from pages.home_page import ScooterHomePage  


class TestsLogo:

    @allure.title('Нажать на логотип "Самокат"')
    def test_click_logo_scooter(self, firefox_driver):
        home_page = ScooterHomePage(firefox_driver)
        home_page.click_logo_scooter()
        assert home_page.get_current_url() == SCOOTER_ORDER_URL

    @allure.title('Кликнуть на логотип Яндекс')
    def test_click_logo_ya(self, firefox_driver):
        home_page = ScooterHomePage(firefox_driver)
        home_page.click_logo_ya()
        home_page.wait_url_contains(YA_DZEN_URL)
        assert home_page.get_current_url() == YA_DZEN_URL

        