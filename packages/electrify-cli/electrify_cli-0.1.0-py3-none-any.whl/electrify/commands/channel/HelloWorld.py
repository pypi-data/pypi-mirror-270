# DownloadAttachments.py
import click
import asyncio

class HelloWorld:
    def __init__(self, user):
        self.user = user

    async def run(self):
        print(f'Hello, {self.user}!')

@click.command()
@click.option('--user', required=True)
def hello_world(user):
    task = HelloWorld(user)
    asyncio.run(task.run())
