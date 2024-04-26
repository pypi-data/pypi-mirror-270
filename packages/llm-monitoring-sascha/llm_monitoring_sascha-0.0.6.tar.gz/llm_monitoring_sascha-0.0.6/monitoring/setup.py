from setuptools import setup, find_packages

setup(
    name='plenoria',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pip install google-cloud-pubsub==2.21.1'
    ],
)
