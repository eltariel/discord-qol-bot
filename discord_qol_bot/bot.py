import click

from .qol_client import QolClient


@click.command()
@click.option("--token", "-t", required=True, help="Discord bot token")
def bot(token):
    intents = discord.Intents.default()
    intents.message_content = True

    client = QolClient(intents=intents)
    client.run(token)
