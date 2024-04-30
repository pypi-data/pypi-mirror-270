from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from allure import attach
import allure
from src.test.library.util_web import UTIL_WEB


class demoRegistro:

    screenshot_counter = 0
    
    def __init__(self, context):
        self.context = context
       
    def abrir_URL(self, url):
        self.context.driver.get(url)
        self.context.driver.implicitly_wait(10)
        self.context.driver.maximize_window()
        demoRegistro.screenshot_counter += 1  # Incrementar el contador de capturas
        screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_abreWeb.png"
        UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
        allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)

    def click_MyAccount(self):
        try:
            btn_my_account = self.context.driver.find_element(By.LINK_TEXT, "My Account")
            btn_my_account.click()
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_clickMyAccount.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()

    def click_Register(self):
        try:
            listLogin = self.context.driver.find_element(By.LINK_TEXT, "Login")
            listLogin.click()
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_clickLogin.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()


    def click_Continue(self):
        try:
            btnContinue = self.context.driver.find_element(By.LINK_TEXT, "Continue")
            btnContinue.click()
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_clickContinue.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()

    def ingresaNombre(self, nombre):
        try:
            txtFirstName = self.context.driver.find_element(By.ID, "input-firstname")
            txtFirstName.send_keys(nombre)
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_ingresoNombre.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()

    def ingresaApellido(self, apellido):
        try:
            txtLastname = self.context.driver.find_element(By.ID, "input-lastname")
            txtLastname.send_keys(apellido)
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_ingresoApellido.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()
    
    def ingresaEmail(self, correo):
        try:
            txtEmail = self.context.driver.find_element(By.ID, "input-email")
            txtEmail.send_keys(correo)
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_ingresoEmail.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()
    
    def ingresaTelefono(self, telefono):
        try:
            txtPhone = self.context.driver.find_element(By.ID, "input-telephone")
            txtPhone.send_keys(telefono)
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_ingresoTelefono.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()

    def ingresaClave(self, ruta_json):
        try:            
            password = UTIL_WEB.obtener_contraseña_desde_json(ruta_json)
            print("Contraseña obtenida del archivo JSON:", password)
            txtPass1 = self.context.driver.find_element(By.ID, "input-password")
            txtPass1.send_keys(password)  # Usamos la contraseña obtenida del JSON
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_ingresoClave.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()

    def ingresaConfirmación(self, ruta_json):
        try:            
            p_confirmar = UTIL_WEB.obtener_confirmacion_desde_json(ruta_json)
            print("Contraseña obtenida del archivo JSON:", p_confirmar)
            txtPass2 = self.context.driver.find_element(By.ID, "input-confirm")
            txtPass2.send_keys(p_confirmar)
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_ingresoConfirmacion.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()

    def click_Privacidad(self):
        try:
            checkBox = self.context.driver.find_element(By.NAME, "agree")
            checkBox.click()
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_clickPrivacidad.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()

    def click_Continuar(self):
        try:
            btnSumit = self.context.driver.find_element(By.CSS_SELECTOR, "input[class='btn btn-primary']")
            btnSumit.click()
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_clickSubmit.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()


    def verificarRegistro(self):
        try:
            label = self.context.driver.find_element(By.XPATH, "//*[@id='content']/p[1]")
            textoOutput = label.text
            textoEsperado = "Congratulations! Your new account has been successfully created!"
            assert textoOutput == textoEsperado
            demoRegistro.screenshot_counter += 1
            screenshot_name = f"{demoRegistro.screenshot_counter}_screenshot_verificacion.png"
            UTIL_WEB.capture_screenshot(self.context.driver, screenshot_name)
            allure.attach(self.context.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except AssertionError:
            print("La verificación falló: el texto obtenido no coincide con el texto esperado.")
            self.context.driver.close()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.driver.close()
        except Exception as e:
            print(f"Ocurrió un error inesperado: {str(e)}")
            self.context.driver.close()
