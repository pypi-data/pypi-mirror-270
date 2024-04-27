import os
import json
from selenium.webdriver import Chrome, Firefox, Edge
import configparser

class UTIL_WEB:


    @staticmethod
    def capture_screenshot(driver, filename, directory='screenshots'):
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, filename)
        driver.save_screenshot(filepath)

    @staticmethod
    def obtener_contraseña_desde_json(ruta_json):
        with open(ruta_json, 'r') as archivo_json:
            datos = json.load(archivo_json)
            return datos["credentials"]["password"]
        
    @staticmethod
    def obtener_confirmacion_desde_json(ruta_json):
        with open(ruta_json, 'r') as archivo_json:
            datos = json.load(archivo_json)
            return datos["credentials"]["confirm_password"]
        
    
    