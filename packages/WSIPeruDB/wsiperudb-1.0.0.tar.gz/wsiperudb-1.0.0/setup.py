from setuptools import setup, find_packages

setup(
    name='WSIPeruDB',
    version='1.0.0',
    packages=find_packages(where='libname'),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'mysql-connector-python',
        'folium',
        'scikit-learn',
        'plotly_express',
        'ipywidgets',
        'geopandas',
        'xlsxwriter',
        'notebook==6.5.2'
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    author='Carol Romero',
    author_email='romeroroldancarol@gmail.com',
    description='Water Stable Isotope Database in Peru',
    long_description='This package allows users to access the Water Stable Isotope Database in Peru. It includes 464 stations over Peru, updated until 2023, and provides an interactive map for exploring the spatial distribution of all the stations. Additionally, it offers features for technical validation and display temporal series for each station and department across Peru',
    url='https://github.com/karoru23/WSI-PeruDB',
)
