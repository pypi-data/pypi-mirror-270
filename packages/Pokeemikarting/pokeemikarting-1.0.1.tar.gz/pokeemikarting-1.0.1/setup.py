from setuptools import setup, find_packages

setup(
    name='Pokeemikarting',
    version='1.0.1',
    author='Emilio Jiminez',
    author_email='rochajimenezjoseemilio@gmail.com',
    description='Libreria para generar un Pokemon aleatorio',
    packages=['Pokeemikarting'],
    package_data={'Pokeemikarting': ['pokemon.csv']},
    install_requires=[
        'pandas'
    ]
)
