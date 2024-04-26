from setuptools import setup, find_packages
setup(
    name="PokemonLmba",
    version="1.0.0",
    author="Litzy Barrera",
    author_email="202224128_barrera@tesch.edu.mx",
    description="Libreria para generar un pokemon aleatorio.",
    packages=["PokemonLmba"],
    package_data={"PokemonLmba": ["pokemon.csv"]},
    install_requires= [
        "pandas",
    ],
)