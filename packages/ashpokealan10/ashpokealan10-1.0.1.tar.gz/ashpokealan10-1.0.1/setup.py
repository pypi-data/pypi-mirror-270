from setuptools import setup, find_packages

setup(
    name='ashpokealan10',
    version='1.0.1',
    author="alan27",
    author_email="alanurielsanchezhernandez9@gmail.com",
    description="Libreria para generar un pokemon aleatorio",
    packages=['ashpokealan10'],
    package_data={'ashpokealan10': ['pokemon.csv']},
    install_requires=[
        'pandas'
    ]

)