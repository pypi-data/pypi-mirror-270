# base.py
import click

@click.group()
def channel():
    """Manage channel operations."""
    pass

# This setup allows you to import subcommands into this group.
# base.py continued
from .DownloadAttachments import download_attachments
channel.add_command(download_attachments)


from .HelloWorld import hello_world
channel.add_command(hello_world)
