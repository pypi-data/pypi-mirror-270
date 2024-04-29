from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Engine for simulating relic in Warframe.'
LONG_DESCRIPTION = 'Engine that allows the full simluation of any relic in Warframe, shows each individual reward screen as well as the number of each "best drop," the order at which the best drop is chosen is customizable.'


setup(
    name='simulation-engine',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Jacob McBride',
    author_email='jake55111@gmail.com',
    packages=find_packages(),
    keywords=['warframe', 'fissures'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy~=1.26.4',
        'relic-engine~=0.2.8'
    ],
)
