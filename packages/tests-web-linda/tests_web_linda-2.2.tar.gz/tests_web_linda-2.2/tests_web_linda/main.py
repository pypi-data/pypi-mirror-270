# main.py
import argparse
import os
import shutil
import subprocess
from .version import __version__

def copy_app_directory():
    # Obtener la ruta absoluta de la carpeta 'app' dentro del paquete
    package_dir = os.path.dirname(os.path.abspath(__file__))
    app_dir = os.path.join(package_dir, 'app')
    
    # Copiar el directorio 'app' al directorio actual
    shutil.copytree(app_dir, './app')

def install_dependencies():
    # Obtener la ruta absoluta del directorio de trabajo actual
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, 'app')

    # Ejecutar npm install en el directorio 'app'
    subprocess.run(['npm', 'install'], cwd=app_dir)

def main():
    parser = argparse.ArgumentParser(description='Tests Web Linda')
    parser.add_argument('--setup', action='store_true', help='Copy app directory and install dependencies')
    parser.add_argument('--version', action='store_true', help='Show version')
    args = parser.parse_args()

    if args.setup:
        copy_app_directory()
        print('App directory copied successfully.')
        install_dependencies()
        print('Npm dependencies installed successfully.')
    elif args.version:
        print(f'Version: {__version__}')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

