import allure
from locators.order_locators import NAME_INPUT, SURNAME_INPUT, ADDRESS_INPUT, METRO_STATION_INPUT, PHONE_INPUT, \
    BUTTON_NEXT, RENT_DATE_FIELD, RENT_PERIOD_DROPDOWN, RENT_TIME,  RENT_COMMENT_COURIER, \
    RENT_BUTTON_ORDER, BUTTON_YES, WINDOW_ORDER_PLACED
from pages.base_page import BasePage

class ScooterOrderPage(BasePage):

    @allure.step('Открыть браузер')
    def __init__(self, driver):
        super().__init__(driver)

#Заполнение экранной формы "Для кого самокат"
    @allure.step('Заполнить поле "Имя"')
    def name_input(self, name):
        self.input_text(NAME_INPUT, name)

    @allure.step('Заполнить поле "Фамилия"')
    def surname_input(self, surname):
        self.input_text(SURNAME_INPUT, surname)

    @allure.step('Заполнить поле "Адрес: куда привезти заказ"')
    def address_input(self, address):
        self.input_text(ADDRESS_INPUT, address)

    @allure.step('Заполнить поле "Станция метро"')
    def metro_station_input(self, metro_station):
        self.click_element(METRO_STATION_INPUT)
        self.click_element(metro_station)

    @allure.step('Заполнить поле "Телефон: на него позвонит курьер"')
    def phone_input(self, phone):
        self.input_text(PHONE_INPUT, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_button_next(self):
        self.click_element(BUTTON_NEXT)


#Заполнение экранной формы "Про аренду"
    @allure.step('Выбор даты "Когда привезти самокат"')
    def rent_date_field_input(self, delivery_date):
        self.click_element(RENT_DATE_FIELD)
        self.click_element(delivery_date)

    @allure.step('Выбрать "Срок аренды"')
    def rent_period_dropdawn_input(self, rent_period_dropdawn):
        self.click_element(RENT_PERIOD_DROPDOWN)
        self.click_element(rent_period_dropdawn)

    @allure.step('Выбрать дату доставки самоката')
    def set_rental_period(self, rent_period):
        self.click_to_element(RENT_TIME)
        self.click_to_element(rent_period)

    @allure.step('Выбрать "Цвет самоката"')
    def color_input(self, color):
        self.click_element(color)

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def comment_curier_input(self, comment_curier):
        self.input_text(RENT_COMMENT_COURIER, comment_curier)

    @allure.step('Нажать кнопку "Заказать"')
    def click_rent_button_order(self):
        self.click_element(RENT_BUTTON_ORDER)

    @allure.step('Нажать кнопку "Да"')
    def click_button_yes(self):
        self.click_element(BUTTON_YES)


#Проверка, что на странице есть текст "Заказ оформлен"
    @allure.step('Проверка, что на странице есть текст "Заказ оформлен"')
    def window_order_placed_text(self):
        return self.get_text_from_element(WINDOW_ORDER_PLACED)