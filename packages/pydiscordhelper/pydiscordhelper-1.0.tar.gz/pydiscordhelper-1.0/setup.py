from setuptools import setup, find_packages

setup(
    name="pydiscordhelper",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
        'discord.py>=2.3.2'
    ]
)