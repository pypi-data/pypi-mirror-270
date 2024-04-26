from setuptools import setup,find_packages

setup(
    name="Espinosa",
    version="3.0.6",
    author="JMEX",
    author_email="kvkgif95949@gmail.com",
    description="Libreria para generar un pokemin aleatoriamento",
    packages=["Espinosa"],
    package_data={"Espinosa": ["Pokem.csv"]},
    install_requires=[
        "pandas"
    ]
)
