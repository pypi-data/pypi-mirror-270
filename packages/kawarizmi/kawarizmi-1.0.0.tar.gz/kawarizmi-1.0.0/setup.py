from setuptools import setup, find_packages

setup(
    name='kawarizmi',
    version='1.0.0',

    packages=find_packages(),

    install_requires=[

        'ultralytics >= 8.1.42',
        'numpy >= 1.26.4',
        'opencv-python >= 4.9.0.80',
        'shapely >= 2.0.3'
    ],
    entry_points={
        'console_scripts': [
            'kawarizmi = kawarizmi:parking_space_counter',
        ],
    },
)
