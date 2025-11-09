#Блок "Вопросы о важном"

import allure
import pytest
from locators.faq_locators import COST_AND_PAY, ANSWER_COST_AND_PAY, MANY_SCOOTERS, ANSWER_MANY_SCOOTERS, \
    CALCULATION_RENTAL_TIME, ANSWER_RENTAL_TIME_CALCULATED, ORDER_SCOOTER_TODAY, ANSWER_ORDER_SCOOTER_TODAY, \
    EXTEND_OR_RETURN, ANSWER_EXTEND_OR_RETURN, CHARGING_DEVICE, ANSWER_CHARGING_DEVICE, \
    CANCEL_ORDER, TEXT_CANCEL_ORDER, ACROSS_MKAD, ANSWERACROSS_MKAD
from pages.home_page import ScooterHomePage

class TestScooterHomePage:

    @allure.title('Нажать на вопрос и проверить ответ')    
    @pytest.mark.parametrize('question, answer, answer_text',
                             [
        [COST_AND_PAY, ANSWER_COST_AND_PAY, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [MANY_SCOOTERS, ANSWER_MANY_SCOOTERS,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [CALCULATION_RENTAL_TIME, ANSWER_RENTAL_TIME_CALCULATED,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [ORDER_SCOOTER_TODAY, ANSWER_ORDER_SCOOTER_TODAY,
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [EXTEND_OR_RETURN, ANSWER_EXTEND_OR_RETURN,
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [CHARGING_DEVICE, ANSWER_CHARGING_DEVICE,
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [CANCEL_ORDER, TEXT_CANCEL_ORDER,
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [ACROSS_MKAD, ANSWERACROSS_MKAD, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
            ]
        )
    
    def test_click_question_and_check_answer(self, firefox_driver, question, answer, answer_text):
        home_page = ScooterHomePage(firefox_driver)
        home_page.scroll_important_questions()
        home_page.click_question(question)
        text_element = home_page.get_answer(answer)
        assert text_element == answer_text

