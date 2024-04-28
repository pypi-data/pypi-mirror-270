from setuptools import setup, find_packages

setup(
    name="state_graph",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "pydantic",
        "networkx",
        "matplotlib",
        "beartype",
        "rich",
        "ipython",
    ],
)
