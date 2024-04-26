# main.py
import argparse
import os
import shutil
import subprocess
from .version import __version__

def copy_app_directory():
    package_dir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.join(package_dir, 'app')
    target_dir = './app'

    # Si el directorio 'app' ya existe, eliminarlo
    if os.path.exists(target_dir):
        print("El directorio 'app' ya existe. Procediendo a eliminarlo...")
        shutil.rmtree(target_dir)

    # Copiar el directorio 'app' al directorio actual
    print("Copiando el directorio 'app'...")
    shutil.copytree(app_dir, target_dir)
    print("Directorio 'app' copiado exitosamente.")

def install_dependencies():

    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, 'app')

    os.chdir(app_dir)
    subprocess.run('npm install', shell=True)

def execute_tests():
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, 'app')

    os.chdir(app_dir)

    subprocess.run('behave', shell=True)

def main():
    parser = argparse.ArgumentParser(description='Testing utility for web applications.')
    parser.add_argument('--setup', action='store_true', help='Copy app directory and install dependencies')
    parser.add_argument('--version', action='store_true', help='Show version')
    parser.add_argument('--run-tests', action='store_true', help='Run tests')
    args = parser.parse_args()

    if args.setup:
        copy_app_directory()
        print('App directory copied successfully.')
        install_dependencies()
        print('Npm dependencies installed successfully.')
    elif args.version:
        print(f'Version: {__version__}')
    elif args.run_tests:
        execute_tests()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

