from setuptools import setup, find_packages

setup(
    name='pratac',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pratac = pratac.__main__:main'
        ]
    }
)
