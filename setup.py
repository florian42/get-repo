import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

setup(
    name='git-get',
    version='0.1.0',
    description='Read the latest Real Python tutorials',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/realpython/reader',
    author='Real Python',
    author_email='info@realpython.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=['typer', 'git-url-parse'],
    entry_points={
        'console_scripts': [
            'git-get = git_get.cli:main',
        ],
    },
)
