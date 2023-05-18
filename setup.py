from setuptools import find_packages, setup

__version__ = "1.0"

setup(
    name="Simulator",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "csv",
        "matplotlib",
        "scipy",
        "scikit-learn",
        "cmath",
    ],
)