from setuptools import setup, find_packages

setup(
    name='Pokemila',
    version='1.0.1',
    author='Maria Martinez',
    author_email='quinaprinces@gmail.com',
    description='Libreria para generar un Pokemon aleatorio',
    packages=['Pokemila'],
    package_data={'Pokemila': ['pokemon.csv']},
    install_requires=[
        'pandas'
    ]
)