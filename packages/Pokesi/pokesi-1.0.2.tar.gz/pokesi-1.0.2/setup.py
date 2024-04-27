from setuptools import setup, find_packages

setup(
    name='Pokesi',
    version='1.0.2',
    author='Bryan Salazar',
    author_email='bryan.nayrb.1071@gmail.com',
    description='Libreria que permite generar un Pokemon aleatorio',
    packages=['Pokesi'],
    package_data={'Pokesi': ['pokemon.csv']},
    install_requires=[
        'pandas'
    ]
)