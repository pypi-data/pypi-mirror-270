import os
import shutil
import subprocess
from .variables import version, repository_url, branch

def print_version():
    print(f'Version: {version}')

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
    # app_dir = os.path.join(current_dir, 'app')
    # os.chdir(app_dir)
    print('Ejecutando pruebas...')
    subprocess.run('behave --no-skipped', shell=True)

def generate_report_html():
    current_dir = os.getcwd()
    # app_dir = os.path.join(current_dir, 'app')
    # os.chdir(app_dir)
    print('Generando reporte...')
    subprocess.run('allure generate', shell=True)
    subprocess.run('allure open', shell=True)

def generate_report_word():
    current_dir = os.getcwd()
    # app_dir = os.path.join(current_dir, 'app', 'src', 'test', 'config')
    subprocess.run('python ./src/test/config/generate_word_web.py', shell=True)

def reset_files():
    folders = ["allure-report", "allure-results", "screenshots", "Evidencias"]
    current_dir = os.getcwd()

    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        try:
            shutil.rmtree(folder_path)
            print(f"La carpeta '{folder}' ha sido eliminada exitosamente.")
        except FileNotFoundError:
            print(f"La carpeta '{folder}' no existe.")

def clone_repository():
    print('Preparando repositorio...')
    if os.path.isdir('app'):
        if not os.path.isdir('app/.git'):
            print('El directorio "app" existe pero no es un repositorio git. Eliminándolo...')
            shutil.rmtree('app')
        else:
            print('El directorio "app" ya existe. Actualizando...')
            subprocess.run(f'git -C app pull origin {branch}', shell=True)

    if not os.path.isdir('app'):
        print('Clonando repositorio...')
        subprocess.run(f'git clone {repository_url} app', shell=True)

    print(f'Cambiando a la rama {branch}...')
    subprocess.run(f'git -C app checkout {branch}', shell=True)