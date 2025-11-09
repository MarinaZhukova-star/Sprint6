import allure
from locators.faq_locators import IMPORTANT_QUESTIONS
from locators.logo_locators import LOGO_YA, LOGO_SCOOTER 
from locators.order_locators import BUTTON_ORDER_TOP, BUTTON_ORDER_BOTTOM
from pages.base_page import BasePage


class ScooterHomePage(BasePage):

#Браузер
    @allure.step('Открыть браузер Firefox')
    def __init__(self, driver):
        super().__init__(driver)

#Логотипы

    @allure.step('Кликнуть на логотип Самокат')
    def click_logo_scooter(self):
        self.click_element(LOGO_SCOOTER)

    @allure.step('Кликнуть на логотип Яндекс')
    def click_logo_ya(self):
        self.click_element(LOGO_YA)

#Кнопки "Заказать"

    @allure.step('Нажать кнопку "Заказать" вверху страницы')
    def click_button_order_top(self):
        self.click_element(BUTTON_ORDER_TOP)

    @allure.step('Переходим к кнопке "Заказать" внизу страницы')
    def scroll_button_order_bottom(self):
        self.scroll_to_element(BUTTON_ORDER_BOTTOM)

    @allure.step('Нажать кнопку "Заказать" внизу страницы')
    def click_button_order_bottom(self):
        self.click_element(BUTTON_ORDER_BOTTOM)

#Вопросы о важном        

    @allure.step('Скроллить страницу вниз до блока "Вопросы о важном"')
    def scroll_important_questions(self):
        self.scroll_to_element(IMPORTANT_QUESTIONS)

    @allure.step('Нажать на вопрос, чтобы развернуть ответ')
    def click_question(self, element):
        self.click_element(element)

    @allure.step('Получить текст ответа')
    def get_answer(self, element):
        return self.get_text_element(element)




