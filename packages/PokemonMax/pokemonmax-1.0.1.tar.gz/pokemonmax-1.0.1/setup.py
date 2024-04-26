from setuptools import setup, find_packages

setup(
    name='PokemonMax',
    version='1.0.1',
    author="Alexis",
    author_email="axelgoma11@gamil.com",
    description="Esta libreria contiene la facilidad de generar un pokemon aleatoria",
    packages=["pokemonmax"],
    package_data={"Pokemonmax":["pokemon.csv"]},
    install_requires=[
        "pandas"
    ]
)