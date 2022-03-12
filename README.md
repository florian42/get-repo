# git-get
> A small cli utility for cloning git repositories in an orderly manner.

`git-get` clones git repositories into `$HOME/source/{host}/{owner}/{repository-name}``

## Installation

OS X & Linux & Windows:

```sh
pip install git-get
```

## Usage example

```sh
git-get https://github.com/florian42/git-get.git
```

## Development setup

- Install Python 3.x
- Install [Poetry](https://python-poetry.org/docs/)

```sh
poetry install
poetry run pre-commit install
poetry run pre-commit run --all-files
```

## Release History

* 0.1.0
    * Initial Release

## Meta

Florian Aumeier – hey@flo.fish

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/florian42/git-get](https://github.com/florian42)

## Contributing

1. Fork it (<https://github.com/florian42/git-get/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
