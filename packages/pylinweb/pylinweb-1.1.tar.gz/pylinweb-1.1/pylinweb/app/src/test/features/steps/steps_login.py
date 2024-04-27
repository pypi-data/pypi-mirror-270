from behave import *
from selenium.common.exceptions import NoSuchElementException
from src.test.pages.pageDemoLogin import demoLogin
from src.test.pages.pageDemoRegistro import demoRegistro
from src.test.pages.pageCertificado import demoCertificado

# Inicializar el driver de Selenium
#driver = None
pageLogin = None
pageRegistro = None
pageCertificado=None

@given('Usuario ingresa nuevamente a la web de OpenCart "{url}"')
def step_impl(context, url):
    global pageRegistro, pageCertificado
    context.pageRegistro = demoRegistro(context)
    context.pageCertificado = demoCertificado(context)

    context.pageRegistro.abrir_URL(url)
    context.pageCertificado.click_configAvanzada()
    context.pageCertificado.click_Acceder()
    

@when('Usuario da click en la opcion Login')
def step_impl(context):
    global pageRegistro
    context.pageRegistro = demoRegistro(context)
    context.pageRegistro.click_MyAccount()
    context.pageRegistro.click_Register()
      

@when('Usuario ingesa su correo "{correo}"')
def step_impl(context, correo):
    global pageRegistro
    context.pageRegistro = demoRegistro(context)
    context.pageRegistro.ingresaEmail(correo)
    


@when('Usuario ingresa su contraseña')
def step_impl(context):
    global pageRegistro
    context.pageRegistro = demoRegistro(context)
    ruta_json = "./src/test/resources/data/json/credentials.json"
    context.pageRegistro.ingresaClave(ruta_json)
    


@then('Se verifica el Login correcto')
def step_impl(context):
    global pageLogin
    #global driver, page
    context.pageLogin = demoLogin(context)
    context.pageLogin.click_Login()
    #page.cerrarNavegador()
