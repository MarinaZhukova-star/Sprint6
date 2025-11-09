from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    #Найти элемент
    def find_element(self, element):
        return self.driver.find_element(*element)

    #Нажать на элемент
    def click_element(self, element):
        self.driver.find_element(*element).click()

    #Пролистать до элемента
    def scroll_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*element))

    #Получить текст элемента
    def get_text_element(self, element):
        return self.driver.find_element(*element).text

    #Ввод текста
    def text_input(self, element, text):
        return self.driver.find_element(*element).send_keys(text)

    #Получить адрес страницы
    def get_current_url(self):
        return self.driver.current_url

    #Ожидание загрузки страницы
    def wait_url_contains(self, url):
        Wait(self.driver, 10).until(EC.url_contains(url))