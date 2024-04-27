from setuptools import setup, find_packages
from setuptools.command.install import install

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pylinweb',
    version='1.0',
    description='A simple functional test library using Python and Selenium',
    author='Linda Lopez',
    packages=find_packages(),
    include_package_data=True, #Esto hace que setuptools lea el archivo MANIFEST.in
    package_data={
        'pylinweb': ['app/*'],
    },
    install_requires=[
        "allure-behave==2.13.4",
        "allure-python-commons==2.13.4",
        "behave==1.2.6",
        "behave-html-formatter==0.9.10",
        "behave2cucumber==1.0.3",
        "docxcompose==1.4.0",
        "docxtpl==0.16.8",
        "playwright==1.42.0",
        "psutil==5.9.2",
        "PyPDF2==3.0.1",
        "python-docx==1.1.0",
        "pycparser==2.21",
        "screeninfo==0.8",
        "selenium==4.1.3",
        "webdriver-manager==4.0.1",
        "webdrivermanager==0.10.0",
        "keyboard==0.13.5"
    ],
    entry_points={
        'console_scripts': [
            'pylinweb=pylinweb.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ],
    keywords=['selenium', 'testing', 'web', 'chrome'],
    long_description=long_description,
    long_description_content_type="text/markdown",
)