import click

from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """Ciaran's exciting demo project."""
    click.echo("Hello, world!")

if __name__ == "__main__":
    main()
