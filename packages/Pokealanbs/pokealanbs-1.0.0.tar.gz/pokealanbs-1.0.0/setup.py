from setuptools import setup, find_packages
setup(
    name='Pokealanbs',
    version='1.0.0',
    author="Alan Suarez",
    author_email="202224129_bautista@tesch.edu.mx",
    description="Libreria para generar un pokemon aleatorio",
    packages=['pokealan'],
    package_data={"pokealan": ["pokemon.csv"]},
    install_requires=[
        "pandas"
    ]
)