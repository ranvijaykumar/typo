import pathlib
from setuptools import setup

exec(open('typo/version.py').read())

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE/"README.md").read_text()

setup(
    name='typo',
    version=__version__,
    description='A python package to simulate typographical errors.',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/ranvijaykumar/typo',
    author='Ranvijay Kumar',
    license='MIT',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    packages=['typo', 'typo.keyboardlayouts']
)
