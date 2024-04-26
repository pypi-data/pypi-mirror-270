from setuptools import setup, find_packages

setup(
    name='Pokemien',
    version='1.0.1',
    author='Angel Lopez',
    author_email='Lopez066p7@gmail.com',
    description='Libreria para generar un Pokemon aleatorio',
    packages=['Pokemien'],
    package_data={'Pokemien': ['pokemon.csv']},
    install_requires=[
        'pandas'
    ]
)
