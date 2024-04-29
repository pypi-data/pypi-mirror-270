from setuptools import setup

setup(
    name = 'csv_reconciler_savarb',
    version = '0.0.1',
    packages = ['csv_reconciler'],
    author = 'Abiodun Dabiri',
    email = 'savarb@gmail.com',
    description = 'A simple CSV reconciler',
    home_page = 'https://github.com/abbeydabiri/csv_reconciler',
    issues = 'https://github.com/abbeydabiri/csv_reconciler/issues',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points = {
        'console_scripts': [
            'csv_reconciler = csv_reconciler.__main__:main'
        ]
    })