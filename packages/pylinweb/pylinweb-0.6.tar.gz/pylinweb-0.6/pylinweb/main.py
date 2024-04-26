# main.py
import argparse
from .functions import copy_app_directory, print_version, generate_report, install_dependencies, execute_tests

def main():
    parser = argparse.ArgumentParser(description='Testing utility for web applications.')
    
    # Define arguments
    parser.add_argument('--setup', action='store_true', help='Copy app directory and install dependencies')
    parser.add_argument('--version', action='store_true', help='Show version')
    parser.add_argument('--run-tests', action='store_true', help='Run tests')
    parser.add_argument('--report', action='store_true', help='Generate report')
    
    args = parser.parse_args()
    
    #Define actions and their corresponding functions
    actions = {
        'setup': lambda: (copy_app_directory(), install_dependencies()),
        'version': print_version,
        'run_tests': execute_tests,
        'report': generate_report
    }

    # Get the first truthy argument
    arg = next((arg for arg in vars(args) if getattr(args, arg)), None)

    if arg in actions:
        actions[arg]()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

