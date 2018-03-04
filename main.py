import discord

from botdata import BotData
from botconf import Conf
from serverconfig import serv_conf

from Context import Context
from Bot import Bot

# Global constants/ environment variables

CONF_FILE = "paradox.conf"
BOT_DATA_FILE = "botdata.db"


# Initialise

conf = Conf(CONF_FILE)
botdata = BotData(BOT_DATA_FILE)

PREFIX = conf.get("PREFIX")

client = discord.Client()
bot = Bot(client=client,
          data=botdata,
          serv_conf=serv_conf,
          user_conf=None,
          bot_conf=conf,
          log_file="paralog.log")


# ----Discord event handling----


@client.event
async def on_ready():
    GAME = conf.getStr("GAME")
    if GAME == "":
        GAME = "in $servers$ servers!"
    GAME = await Context(client=client).para_format(GAME)
    await client.change_presence(status=discord.Status.online, game=discord.Game(name=GAME))
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("Logged into", len(client.servers), "servers")


"""
@client.event
async def on_member_join(member):
    server = member.server
    if not serv_conf["join"].get(botdata, server):
        return
    join_channel = serv_conf["join_ch"].get(botdata, server)
    join_message = serv_conf["join_msg"].get(botdata, server)
    if join_channel == 0:
        return
    channel = server.get_channel(join_channel)
    if not channel:
        return
    msg = await para_format(client, join_message, member=member)
    await client.send_message(channel, msg)


@client.event
async def on_member_remove(member):
    server = member.server
    if not serv_conf["leave"].get(botdata, server):
        return
    channel = serv_conf["leave_ch"].get(botdata, server)
    message = serv_conf["leave_msg"].get(botdata, server)
    if channel == 0:
        return
    channel = server.get_channel(channel)
    if not channel:
        return
    msg = await para_format(client, message, member=member)
    await client.send_message(channel, msg)


@client.event
async def on_server_join(server):
    pass
"""
# ----End Discord event handling----

# ----Event loops----
# ----End event loops----


# ----Everything is defined, start the client!----
client.run(conf.get("TOKEN"))
