# base.py
import click

@click.group()
def ticket():
    """Manage ticket operations."""
    pass

from .HelloWorld import hello_world
ticket.add_command(hello_world)
