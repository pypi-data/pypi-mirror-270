# cli.py
import click
from .commands.channel.base import channel
from .commands.ticket.base import ticket

@click.group()
def cli():
    """Electrify CLI entry point."""
    pass

cli.add_command(channel)
cli.add_command(ticket)


if __name__ == '__main__':
    cli()
