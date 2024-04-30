from behave import *
from selenium.common.exceptions import NoSuchElementException
from src.test.pages.pageCertificado import demoCertificado
from src.test.pages.pageDemoRegistro import demoRegistro

# Inicializar el driver de Selenium
pageRegistro = None
pageCertificado = None
@given('Usuario ingresa a la web de OpenCart "{url}"')
def step_impl(context, url):
    global pageRegistro, pageCertificado
    context.pageRegistro = demoRegistro(context)
    context.pageCertificado = demoCertificado(context)

    context.pageRegistro.abrir_URL(url)
    context.pageCertificado.click_configAvanzada()
    context.pageCertificado.click_Acceder()

@given('Usuario da click en la opción Registro')
def step_impl(context):
    global pageRegistro
    context.pageRegistro = demoRegistro(context)
    context.pageRegistro.click_MyAccount()
    context.pageRegistro.click_Register()
    context.pageRegistro.click_Continue()

@given('Usuario llena los datos de Registro con "{nombre}", "{apellido}", "{correo}" y "{telefono}"')
def step_impl(context, nombre, apellido, correo, telefono):
    global pageRegistro
    context.pageRegistro = demoRegistro(context)
    context.pageRegistro.ingresaNombre(nombre)
    context.pageRegistro.ingresaApellido(apellido)
    context.pageRegistro.ingresaEmail(correo)
    context.pageRegistro.ingresaTelefono(telefono)

@given('Usuario ingresa sus claves')
def step_impl(context):
    global pageRegistro
    context.pageRegistro = demoRegistro(context)
    ruta_json = "./src/test/resources/data/json/credentials.json"
    context.pageRegistro.ingresaClave(ruta_json)
    context.pageRegistro.ingresaConfirmación(ruta_json)
    context.pageRegistro.click_Privacidad()

@then('Se verifica el registro correcto')
def step_impl(context):
    global pageRegistro
    context.pageRegistro = demoRegistro(context)
    context.pageRegistro.click_Continuar()
    context.pageRegistro.verificarRegistro()