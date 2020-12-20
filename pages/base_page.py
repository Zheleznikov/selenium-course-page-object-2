from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


class BasePage:
    def __init__(self, browser, url, timeout=6):
        self.browser = browser
        self.url = url
        # self.user_language = user_language
        self.browser.implicitly_wait(timeout)

    def open(self):
        # открываем браузер
        self.browser.get(self.url)
        # print(self.user_language)

    def is_element_present(self, how, what):
        # проверяем есть ли элемент на старнице. Если такого элемента не находится, то подставляем кастомное
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_element_present2(self, how, what, n=0):
        try:
            self.browser.find_elements(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(how, what)
            )
        except TimeoutException:
            return True
        return False
