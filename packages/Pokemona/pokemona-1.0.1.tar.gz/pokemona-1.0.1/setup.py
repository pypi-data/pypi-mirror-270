from setuptools import setup, find_packages

setup(
    name='Pokemona',
    version='1.0.1',
    author='Alexis Gonzales',
    author_email='axelgoma11@gmail.com',
    description='Libreria para generar un Pokemon aleatorio',
    packages=['Pokemona'],
    package_data={'Pokemona': ['pokemon.csv']},
    install_requires=[
        'pandas'
    ]
)
