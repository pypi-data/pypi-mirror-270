from selenium.webdriver import Chrome, Firefox, Edge
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from behave import *
import os
import json
import configparser

@fixture
def navegador(context):
        config = configparser.ConfigParser()
        config.read('browser.properties')
        browser = config.get('General', 'browser')
        version = config.get('General','version')

        ruta_proyecto = os.getcwd()+"/src/test/resources/drivers/"+browser+"/"
        if browser.lower() == "chrome":
            ruta_proyecto = ruta_proyecto+version+"/chromedriver.exe"
            context.driver = Chrome(ruta_proyecto)
        elif browser.lower() == "firefox":
            ruta_proyecto = ruta_proyecto+version+"/geckodriver.exe"
            context.driver = webdriver.Firefox(ruta_proyecto)
        elif browser.lower() == "edge":
            ruta_proyecto = ruta_proyecto+version+"/msedgedriver.exe"
            context.driver = webdriver.Edge(ruta_proyecto)
        else:
            raise ValueError("Unsupported browser!")
        yield context.driver


def before_scenario(context, scenario):
    print("Inicializando el navegador...")
    use_fixture(navegador, context)

def after_scenario(context, scenario):
     context.driver.quit()

    