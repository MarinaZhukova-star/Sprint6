from selenium.webdriver.common.by import By

# Вопросы и важном
IMPORTANT_QUESTIONS = [By.XPATH, '//div[@class="Home_SubHeader__zwi_E" and text()="Вопросы о важном"]']

# Вопрос "Сколько это стоит? И как оплатить?"
COST_AND_PAY = [By.ID, 'accordion__heading-0']
# Ответ
ANSWER_COST_AND_PAY = [By.ID, 'accordion__panel-0']

# Вопрос "Хочу сразу несколько самокатов! Так можно?"
MANY_SCOOTERS = [By.ID, 'accordion__heading-1']
# Ответ
ANSWER_MANY_SCOOTERS = [By.ID, 'accordion__panel-1']

# Вопрос "Как рассчитывается время аренды?"
CALCULATION_RENTAL_TIME = [By.ID, 'accordion__heading-2']
# Ответ
ANSWER_RENTAL_TIME_CALCULATED = [By.ID, 'accordion__panel-2']

# Вопрос "Можно ли заказать самокат прямо на сегодня?"
ORDER_SCOOTER_TODAY = [By.ID, 'accordion__heading-3']
# Ответ
ANSWER_ORDER_SCOOTER_TODAY = [By.ID, 'accordion__panel-3']

# Вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
EXTEND_OR_RETURN = [By.ID, 'accordion__heading-4']
# Ответ
ANSWER_EXTEND_OR_RETURN = [By.ID, 'accordion__panel-4']

# Вопрос "Вы привозите зарядку вместе с самокатом?"
CHARGING_DEVICE = [By.ID, 'accordion__heading-5']
# Ответ
ANSWER_CHARGING_DEVICE = [By.ID, 'accordion__panel-5']

# Вопрос "Можно ли отменить заказ?"
CANCEL_ORDER = [By.ID, 'accordion__heading-6']
# Ответ
TEXT_CANCEL_ORDER = [By.ID, 'accordion__panel-6']

# Вопрос "Я жизу за МКАДом, привезёте?"
ACROSS_MKAD = [By.ID, 'accordion__heading-7']
# Ответ
ANSWERACROSS_MKAD = [By.ID, 'accordion__panel-7']