from setuptools import find_packages, setup

setup(
    name='kkba_mathUtils',
    packages=find_packages(include=['kkba_mathUtils']),
    version='1.0.0',
    description='My basic mathematics Python library',
    author='Kuate Brayan',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)