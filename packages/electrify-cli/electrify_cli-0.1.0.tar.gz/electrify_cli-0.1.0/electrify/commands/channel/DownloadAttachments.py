# DownloadAttachments.py
import click
import asyncio
#from electrify_sdk.ne_channel import ChannelConversations, MessageAttachments

class DownloadAttachments:
    def __init__(self, mode, inbox_id, mail_subject, output_directory):
        self.mode = mode
        self.inbox_id = inbox_id
        self.mail_subject = mail_subject
        self.output_directory = output_directory

    async def run(self):
        #conversations = ChannelConversations()
        #attachments = conversations.get_attachments(self.inbox_id, self.mail_subject)
        #downloader = MessageAttachments(self.output_directory)

        if self.mode == 'async':
            #await self.download_attachments_async(downloader, attachments)
            print('Downloaded async attachments!')
        else:
            #await self.download_attachments_sync(downloader, attachments)
            print('Downloaded sync attachments!')

    async def download_attachments_sync(self, downloader, attachments):
        for att in attachments:
            await downloader.download_file(att['data_url'])

    async def download_attachments_async(self, downloader, attachments):
        download_tasks = [downloader.download_file(att['data_url']) for att in attachments]
        await asyncio.gather(*download_tasks)

@click.command()
@click.option('--mode', type=click.Choice(['sync', 'async']), default='sync')
@click.option('--inbox_id', required=True)
@click.option('--mail_subject', required=True)
@click.option('--output_directory', required=True)
def download_attachments(mode, inbox_id, mail_subject, output_directory):
    task = DownloadAttachments(mode, inbox_id, mail_subject, output_directory)
    asyncio.run(task.run())
