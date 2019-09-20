from setuptools import setup, find_packages

setup(
    name='azt',
    version='0.0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pyfiglet',
    ],
    entry_points='''
        [console_scripts]
        azt=azt:cli
    ''',
)
