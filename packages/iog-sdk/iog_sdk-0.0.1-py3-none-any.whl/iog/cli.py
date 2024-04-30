import sys

import click


@click.command()
def main(args=None):
    """Console script for IOG SDK."""
    click.echo("IOG SDK in development")
    click.echo("https://developers.io.net/docs")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
