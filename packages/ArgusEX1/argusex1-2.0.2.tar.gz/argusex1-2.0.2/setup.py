from setuptools import setup,find_packages

setup(
    name="ArgusEX1",
    version="2.0.2",
    author="JMEX",
    author_email="kvkgif95949@gmail.com",
    description="Libreria para generar un pokemin aleatoriamento",
    packages=[
        "ArgusEX1"
    ],
    package_data={"ArgusEX1": ["Poc.csv"]},
    install_requires=[
        "pandas"
    ]
)