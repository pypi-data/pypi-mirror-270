from setuptools import setup, find_packages

setup(
   name='dxrt',
   version="1.0.1",
   author="Gael Peña",
   author_email="gaelpeje1@gmaio.com",
   description="Libreria para generar un pokemom aleatorio",
   packages=["dxrt"],
   package_data={'dxrt' : ["pokemon.csv"]},
   install_requires=[
          'pandas'
          ]
)