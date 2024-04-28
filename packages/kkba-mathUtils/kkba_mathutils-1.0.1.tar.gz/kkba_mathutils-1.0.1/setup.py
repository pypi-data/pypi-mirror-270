from setuptools import find_packages, setup


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='kkba_mathUtils',
    packages=find_packages(include=['kkba_mathUtils']),
    version='1.0.1',
    description='My basic mathematics Python library',
    author='Kuate Brayan',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown'
)