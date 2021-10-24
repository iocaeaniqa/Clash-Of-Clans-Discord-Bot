# Sends the list of servers that have the bot

import os

import discord

from Script.Clients.discord_client import Clash_info


async def servers_list(ctx):
    guilds = {}
    for guild in Clash_info.guilds:
        users = 0
        bots = 0
        for member in guild.members:
            if member.bot:
                bots += 1
            else:
                users += 1
        guilds[guild] = {"users": users, "bots": bots}
    ones = 0
    file = open("tmp.txt", "w")
    for guild in sorted(guilds.items(), key=lambda item: item[1]["users"], reverse=True):
        ones += 1
        text = f"\n{ones}) {guild[1]['users'] + guild[1]['bots']} members ({guild[1]['users']} users, {guild[1]['bots']} bots) ; creator : {guild[0].owner.name} ; server : {guild[0].name}"
        file.write(text)
    file.close()
    await ctx.channel.send(file=discord.File("tmp.txt"))
    os.remove("tmp.txt")
    return
