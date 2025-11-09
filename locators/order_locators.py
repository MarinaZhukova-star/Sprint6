from selenium.webdriver.common.by import By
from data import create_metro_station, create_date, create_rent_period

#Кнопка "Заказать" вверху страницы
BUTTON_ORDER_TOP = (By.XPATH, './/button[@class="Button_Button__ra12g"]')
#Кнопка "Заказать" внизу страницы
BUTTON_ORDER_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text() = 'Заказать']")

#Форма заказа
#Поле ввода "Имя"
NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
#Поле ввода "Фамилия"
SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
#Поле ввода "Адрес: куда привезти заказ"
ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
#Поле ввода "Станция метро"
METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
#Список станций метро
METRO_STATION_LIST = [By.XPATH, f'//li[@data-value="{create_metro_station()}"]']
#Поле ввода "Телефон: на него позвонит курьер"
PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
#Кнопка "Далее"
BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

#Форма аренды
#Поле ввода "Когда привезти самокат"
RENT_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
#Выбор даты в календаре
RENT_CHOICE_DATE = (By.CSS_SELECTOR, f".react-datepicker__day--{create_date()}")
#Поле ввода "Срок аренды"
RENT_PERIOD_DROPDOWN = (By.XPATH, "//div[text()='* Срок аренды']")
#Выбор срока аренды
RENT_TIME = [By.XPATH, f"//div[@class='Dropdown-menu']/div[{create_rent_period()}]"]
#Чек-бокс "Черный жемчуг"
RENT_BLACK_SCOOTER = (By.ID, "black")
#Чек-бокс "Серая безысходность"
RENT_GREY_SCOOTER = (By.ID, "grey")
#Поле ввода "Комментарий для курьера"
RENT_COMMENT_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
#Кнопка "Заказать" на форме аренды
RENT_BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

#Форма "Хотите оформить заказ?"
#Ответ "Да"
BUTTON_YES = (By.XPATH, "//button[text() = 'Да']")
#Окно "Заказ оформлен" 
WINDOW_ORDER_PLACED = (By.XPATH, "//div[text()='Заказ оформлен']")
#Кнопка "Посмотреть статус"
BUTTON_VIEW_STATUS = (By.XPATH, "//button[contains(text(), 'Посмотреть статус')]")
