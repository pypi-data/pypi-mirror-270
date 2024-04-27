from setuptools import setup, find_packages

setup(
    name='NetHyTech-STT',
    version='0.1',
    author='Anubhav Chaturvedi',
    author_email='chaturvedianubhav520@example.com',
    description='A package for speech-to-text using Selenium',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'webdriver_manager',
        'pyttsx3',
    ],
    entry_points={
        'console_scripts': [
            'my_package = my_package.main:main'
        ]
    },
)
