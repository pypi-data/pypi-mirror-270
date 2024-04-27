import os
import shutil
import subprocess
from .version import __version__

def print_version():
    print(f'Version: {__version__}')

def copy_app_directory():
    package_dir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.join(package_dir, 'app')
    target_dir = './app'

    # Si la carpeta 'app' ya existe en el directorio actual, eliminarlo
    if os.path.exists(target_dir):
        print("El directorio 'app' ya existe. Procediendo a eliminarlo...")
        shutil.rmtree(target_dir)

    # Copiar la carpeta'app' al directorio actual
    print("Copiando el directorio 'app'...")
    shutil.copytree(app_dir, target_dir)
    print("Directorio 'app' copiado exitosamente.")

def install_dependencies():
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, 'app')

    os.chdir(app_dir)
    print('Instalando dependencias...')
    subprocess.run('npm install', shell=True)
    subprocess.run('npm install -g allure-commandline', shell=True)

    try:
        subprocess.run('allure --version', shell=True, check=True)
    except subprocess.CalledProcessError:
        print('Allure no está correctamente instalado. Cambiando la política de ejecución...')
        subprocess.run('Set-ExecutionPolicy RemoteSigned -Scope CurrentUser', shell=True)
        subprocess.run('allure --version', shell=True)

    print('Dependencias instaladas exitosamente.')

def execute_tests():
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, 'app')
    os.chdir(app_dir)
    print('Ejecutando pruebas...')
    subprocess.run('behave --no-skipped', shell=True)

def generate_report_html():
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, 'app')
    os.chdir(app_dir)
    print('Generando reporte...')
    subprocess.run('allure generate', shell=True)
    subprocess.run('allure open', shell=True)

def generate_report_word():
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, 'app', 'src', 'test', 'config')
    os.chdir(app_dir)
    subprocess.run('python generate_report_word.py', shell=True)

def reset_files():
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, 'app', 'src', 'test', 'config')
    os.chdir(app_dir)
    subprocess.run('python delete_folders.py', shell=True)



    