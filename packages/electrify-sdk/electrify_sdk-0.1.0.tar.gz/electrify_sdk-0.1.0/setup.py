from setuptools import setup, find_packages

setup(
    name='electrify-sdk',
    version='0.1.0',
    author='Nularian',
    author_email='info@nularian.com',
    packages=find_packages(),
    install_requires=['python-dotenv', 'httpx', 'pydantic' ],
    description='SDK for electrify services',
)
