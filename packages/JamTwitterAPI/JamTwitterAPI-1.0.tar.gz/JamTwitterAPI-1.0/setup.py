from setuptools import setup, find_packages

setup(
    name='JamTwitterAPI',
    version='1.0',
    author='Jaammerr',
    author_email='jaammer.dev@gmail.com',
    description='Implementation of X/Twitter v1, v2, and GraphQL APIs',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
