from setuptools import setup, find_packages

setup(
    name='WSI-PeruDB',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'mysql-connector-python',
        'folium',
        'scikit-learn',
        'scikit-learn',
        'ipywidgets',
        'geopandas',
        'xlsxwriter'
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    author='Carol Romero',
    author_email='romeroroldancarol@gmail.com',
    description='This package allows users to access the Water Stable Isotope Database in Peru. It includes 464 stations over Peru, updated until 2023, and provides an interactive map for exploring the spatial distribution of all the stations. Additionally, it offers features for technical validation and display temporal series for each station and department across Peru',
    url='https://github.com/karoru23/WSI-PeruDB',
)
