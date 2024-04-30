from setuptools import setup, find_packages

setup(
    name='jsonLiteLLM',
    version='1.0.0',
    author='Maher AMARA',
    packages=find_packages(),
    install_requires=[
        'litellm',
        'regex',
        'jsonschema'
    ],
    python_requires='>=3.7',
)