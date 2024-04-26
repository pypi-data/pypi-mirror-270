from setuptools import setup, find_packages

setup(
    name='poke_frm_donpolloloco',
    version='1.0.1',
    author= "FernandoRoldan",
    author_email="roldanf661@gmail.com",
    description="LIBRERIA QUE GENRA UN POKEMON DE DONPOLLOLO, ES DECIR UN POKEMON ALEATORIO",
    packages=["POKE_DONPOLLO"],
    package_data= {'POKE_DONPOLLO': ['pokemon.csv']},
    install_requires = ['pandas']
)