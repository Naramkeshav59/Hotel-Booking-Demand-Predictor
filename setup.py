from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "mlops", 
    version = "0.1", 
    author = "keshav",
    author_email = "keshavn@umd.edu",
    description = "MLOPs project", 
    packages = find_packages(),
    install_requires = requirements,
    python_requires = ">=3.8"
)