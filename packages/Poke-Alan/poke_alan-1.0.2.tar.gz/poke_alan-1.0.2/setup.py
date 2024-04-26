from setuptools import setup, find_packages
setup(
    name='Poke-Alan',
    version='1.0.2',
    author="Alan Suarez",
    author_email="202224129_bautista@tesch.edu.mx",
    description="Libreria para generar un pokemon aleatorio",
    packages=['poke-base'],
    package_data={"poke-base": ["pokemon.csv"]},
    install_requires=[
        "pandas"
    ]
)