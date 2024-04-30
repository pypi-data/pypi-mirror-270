from setuptools import find_packages, setup

def load_requirements(filename: str):
    with open(filename, 'r') as file:
        return file.read().splitlines()


setup(
    name="language_model_toolkit",
    version="0.1",
    packages=find_packages(),
    description="A holisitic for interfacing with ollama and other llm hosts. Created mainly for private experimentation.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Steffen Probst",
    author_email="probststeffen15@t-online.de",
    url='https://github.com/AutomatedAlchemy/Language-Model-Toolkit',
    install_requires=load_requirements('requirements.txt')
)
