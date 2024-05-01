# cli.py
import click
from lianpwn.template_gen import generate_template


@click.group()
def cli():
    pass


@cli.command()
def template():
    """Generate a template file"""
    generate_template()


if __name__ == "__main__":
    cli()
