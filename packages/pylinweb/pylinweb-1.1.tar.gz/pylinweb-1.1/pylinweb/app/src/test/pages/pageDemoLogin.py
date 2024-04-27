from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from allure import attach
import allure
from src.test.library.util_web import UTIL_WEB


class demoLogin:

    screenshot_counter = 0
    
    def __init__(self, context):
        self.context = context
       
    
    def click_Login(self):
        try:
            btnLogin = self.context.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']")
            btnLogin.click()
            demoLogin.screenshot_counter += 1
            screenshot_name = f"{demoLogin.screenshot_counter}_screenshot_clickLogin.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()

