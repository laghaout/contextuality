from setuptools import find_packages, setup

setup(
    name='contextuality',
    version='0.0.0',
    author='Amine Laghaout',
    description='Object-oriented framework for simulating contextuality',
    packages=find_packages(exclude=('test*',)),
    zip_safe=False,
    entry_points={
        'console_scripts': ['peres-mermin = contextuality.main:main', ]}
)
