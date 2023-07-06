from setuptools import setup, find_packages

setup(
    name='lung-cancer',
    version='0.1',
    packages=find_packages('source'),
    package_dir={'': 'source'},
    install_requires=[
        'numpy',
        'pandas',
        'pydicom',
        'tqdm',
        'ultralytics',
        'seaborn',
        'tensorflow'
    ]
)