import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Here you can modify the bot's prefix and description and whether it sends help in direct messages or not.
# command_prefix can be changed to have pretty much any special character
client = Bot(description="Basic Bot by Ellimist#2651", command_prefix="!", pm_help = False)

# Dictionary of trigger words that the bot will act upon
triggerDict = {}

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Support Discord Server: https://discord.gg/FNNNgqb')
	print('Github Link: https://github.com/Habchy/BasicBot')
	print('--------')
	print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
	print('Created by Ellimist#2651')
	return await client.change_presence(game=discord.Game(name='EllimistBot'))

# This is a basic example of a call and response command. You tell it do "this" and it does it.
# @client.command()
# async def ping(*args):

# 	await client.say(":ping_pong: Pong!")
# 	await asyncio.sleep(3)
        # use the line below for warnings
        # await client.say(":warning: This bot was created by **Habchy#1665**, it seems that you have not modified it yet. Go edit the file and try it out!")

@client.command()
async def addTrigger(key, value):    # *args are used for untermined number of args
        """Adds a trigger to the triggerDict with the first message as key and the next as value"""
        await client.say("Add trigger")
        triggerDict[key] = value
        await client.say(':white_check_mark: Trigger: {}, response: {}'.format(key, value))
        print(triggerDict)

@client.command()
async def rmTrigger(key):
        """Removes from the triggerDict"""
        if key in triggerDict:
                del triggerDict[key]
                await client.say(':warning: Removed trigger: {}'.format(key))
                print(triggerDict)

@client.event
async def on_message(message):
        if message.author.id != client.user.id: # check to see if the message is sent by the user and not the bot
                # await client.send_message(message.channel, message.content)
                await client.process_commands(message) # added this to allow the command functions to work. on_message interupts commands or else
                for word in message.content.split():
                        if word in triggerDict:
                                await client.send_message(message.channel, triggerDict[word])
                                return                
	        
client.run('PUT YOUR BOT TOKEN HERE')

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
