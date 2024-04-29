from setuptools import setup, find_packages

setup(
    name="dcentralab_auto_infra",
    version="1.1.0",
    packages=find_packages(),
    install_requires=['selenium~=4.20.0',
                      'numpy==2.0.0rc1',
                      'allure-pytest==2.13.5',
                      'pytest==8.1.1',
                      'requests==2.31.0',
                      'webdriver-manager==4.0.1',
                      'json5~=0.9.25']
)
