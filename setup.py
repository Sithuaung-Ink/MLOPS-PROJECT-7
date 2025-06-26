from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT-7",
    version="0.1",
    author="Si Thu Aung",
    packages=find_packages(),
    install_requires = requirements,
)