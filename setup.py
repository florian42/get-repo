import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / 'README.md').read_text()

setup(
    name='get-repo',
    version='0.1.1',
    description='Small cli utility for cloning git repos in an orderly manner',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/florian42/get-repo',
    author='Florian Aumeier',
    author_email='hey@flo.fish',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=['typer==0.4.0', 'git-url-parse==1.2.2'],
    entry_points={
        'console_scripts': [
            'get-repo = get_repo.cli:main',
        ],
    },
)
