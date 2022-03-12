import typer

from .parser import InvalidGitUrl, parse

app = typer.Typer(
    name='git-get',
    add_completion=False,
    help='Helps you clone git repos in an organized way.',
)


@app.command()
def get(url: str) -> None:
    """Clones a git repository"""
    try:
        print(parse(url))
    except InvalidGitUrl as exception:
        print(exception)


def main() -> None:
    app()
