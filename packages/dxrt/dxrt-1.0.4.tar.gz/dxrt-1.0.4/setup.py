from setuptools import setup, find_packages

setup(
   name='dxrt',
   version="1.0.4",
   author="Gael Peña",
   author_email="gaelpeje1@gmail.com",
   description="Libreria para generar un pokemon aleatorio",
   packages=find_packages(),
   package_data={'dxrt' : ["pokemon.csv"]},
   install_requires=[
          'pandas',
          ],
)