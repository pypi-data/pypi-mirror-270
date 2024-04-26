from setuptools import setup, find_packages

setup(
    name='Pokebomari',
    version='1.0.1',
    author='Maria Cortez',
    author_email='202224172@tesch.edu.mx',
    description='Libreria para generar un Pokemon aleatorio',
    packages=['Pokebomari'],
    package_data={'Pokebomari': ['pokemon.csv']},
    install_requires=[
        'pandas'
    ]
)
