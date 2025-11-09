import allure
import pytest
from data import create_name, create_surname, create_address, create_random_phone, create_comment_courier
from locators.order_locators import METRO_STATION_LIST, RENT_CHOICE_DATE, RENT_TIME, RENT_BLACK_SCOOTER, RENT_GREY_SCOOTER
from pages.home_page import ScooterHomePage
from pages.order_page import ScooterOrderPage


class TestScooterOrderPage:

#Тест-кейс с нажатием кнопки "Заказать" вверху страницы
    @allure.title('Заказать самокат через кнопку "Заказать" вверху страницы')
    @pytest.mark.parametrize('name, surname, address, metro_station, phone, delivery_date, rent_period_dropdawn, color, comment_curier',
        [[create_name(), create_surname(), create_address(), METRO_STATION_LIST, create_random_phone(), RENT_CHOICE_DATE, RENT_TIME, RENT_BLACK_SCOOTER, create_comment_courier()]]
    )
    
    def test_button_order_top(self, firefox_driver, name, surname, address, metro_station, phone, delivery_date, rent_period_dropdawn, color, comment_curier):
        home_page = ScooterHomePage(firefox_driver)
        home_page.click_button_order_top()

#Заполнение экранной формы "Для кого самокат"
        order_page = ScooterOrderPage(firefox_driver)
        order_page.name_input(name)
        order_page.surname_input(surname)
        order_page.address_input(address) 
        order_page.metro_station_input(metro_station) 
        order_page.phone_input(phone)
        order_page.click_button_next()

#Заполнение экранной формы "Про аренду"
        order_page.rent_date_field_input(delivery_date)
        order_page.rent_period_dropdawn_input(rent_period_dropdawn)
        order_page.color_input(color)
        order_page.comment_curier_input(comment_curier)
        order_page.click_rent_button_order()
        order_page.click_button_yes()

#Проверка, что на странице есть текст "Заказ оформлен"
        text = order_page.window_order_placed_text()
        assert "Заказ оформлен" in text


#Тест-кейс с нажатием кнопки "Заказать" внизу страницы
    @allure.title('Заказать самокат через кнопку "Заказать" внизу страницы')
    @pytest.mark.parametrize('name, surname, address, metro_station, phone, delivery_date, rent_period_dropdawn, color, comment_curier',
        [[create_name(), create_surname(), create_address(), METRO_STATION_LIST, create_random_phone(), RENT_CHOICE_DATE, RENT_TIME, RENT_GREY_SCOOTER, create_comment_courier()]]
    )

    def test_buttom_order_bottom(self, firefox_driver, name, surname, address, metro_station, phone, delivery_date, rent_period_dropdawn, color, comment_curier):
        home_page = ScooterHomePage(firefox_driver)
        home_page.scroll_button_order_bottom()
        home_page.click_button_order_bottom()
        scooter_order_page = ScooterOrderPage(firefox_driver)

       #Заполнение экранной формы "Для кого самокат"
        order_page = ScooterOrderPage(firefox_driver)
        order_page.name_input(name)
        order_page.surname_input(surname)
        order_page.address_input(address) 
        order_page.metro_station_input(metro_station) 
        order_page.phone_input(phone)
        order_page.click_button_next()

        #Заполнение экранной формы "Про аренду"
        order_page.rent_date_field_input(delivery_date)
        order_page.rent_period_dropdawn_input(rent_period_dropdawn)
        order_page.color_input(color)
        order_page.comment_curier_input(comment_curier)
        order_page.click_rent_button_order()
        order_page.click_button_yes()

#Проверка, что на странице есть текст "Заказ оформлен"
        text = scooter_order_page.window_order_placed_text()
        assert "Заказ оформлен" in text