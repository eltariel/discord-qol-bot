import re
import discord
from yarl import URL


class QolClient(discord.Client):
    urlre = re.compile("(https?://)?(www\.)?twitter.com/[\w/#?&%=]*")

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        m = self.urlre.search(message.content)
        if m:
            twurl = m.group(0).lstrip("/")
            scheme = m.group(1)
            print(m.groups())
            if scheme is None:
                twurl = "https://" + twurl
            fxurl = URL(twurl).with_host("fxtwitter.com")
            print(f"{message.author}: {twurl} => {fxurl}")
            await message.reply(fxurl, mention_author=True)
