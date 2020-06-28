import discord
from discord.ext import commands
from pynput.keyboard import Key, Controller

keyboard = Controller()
# Change each key to what is set up for your game
keyA = 'a' # for single keys just type the key
keyB = 'b'
keyUp = Key.up # For special case keys info -> https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
keyDown = Key.down
keyLeft = Key.left
keyRight = Key.right
keySelect = 'o'
keyStart = 'p'


token = '' # Get bot token from https://discord.com/developers/applications | more info at README.md

prefix = '~' # Edit this to change prefix


# There should be no need to change anything below this point

bot = commands.Bot(command_prefix='~')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Awaiting Commands'))
    print("----------------------")
    print("Logged In As")
    print("Username: %s" % bot.user.name)
    print("ID: %s" % bot.user.id)
    print("----------------------")


@bot.listen()
async def on_message(message):
    if message.content.startswith(prefix + 'a'):
        channel = message.channel

        emoji = '\N{THUMBS UP SIGN}'
        # or '\U0001f44d' or '👍'
        await message.add_reaction(emoji)
        print("Button pressed [A]")
        keyboard.press(keyA)
        keyboard.release(keyA)


@bot.listen()
async def on_message(messageone):
    if messageone.content.startswith(prefix + '~b'):
        channel = messageone.channel

        emoji = '\N{THUMBS UP SIGN}'
        # or '\U0001f44d' or '👍'
        await messageone.add_reaction(emoji)
        print("Button pressed [B]")
        keyboard.press(keyB)
        keyboard.release(keyB)


@bot.listen()
async def on_message(message):
    if message.content.startswith(prefix + '~up'):
        channel = message.channel

        emoji = '\N{THUMBS UP SIGN}'
        # or '\U0001f44d' or '👍'
        await message.add_reaction(emoji)
        print("Button pressed [Up]")
        keyboard.press(keyUp)
        keyboard.release(keyUp)


@bot.listen()
async def on_message(message):
    if message.content.startswith(prefix + '~down'):
        channel = message.channel

        emoji = '\N{THUMBS UP SIGN}'
        # or '\U0001f44d' or '👍'
        await message.add_reaction(emoji)
        print("Button pressed [Down]")
        keyboard.press(keyDown)
        keyboard.release(keyDown)


@bot.listen()
async def on_message(message):
    if message.content.startswith(prefix + '~left'):
        channel = message.channel

        emoji = '\N{THUMBS UP SIGN}'
        # or '\U0001f44d' or '👍'
        await message.add_reaction(emoji)
        print("Button pressed [Left]")
        keyboard.press(keyLeft)
        keyboard.release(keyLeft)


@bot.listen()
async def on_message(message):
    if message.content.startswith(prefix + '~right'):
        channel = message.channel

        emoji = '\N{THUMBS UP SIGN}'
        # or '\U0001f44d' or '👍'
        await message.add_reaction(emoji)
        print("Button pressed [Right]")
        keyboard.press(keyRight)
        keyboard.release(keyRight)


@bot.listen()
async def on_message(message):
    if message.content.startswith(prefix + '~select'):
        channel = message.channel

        emoji = '\N{THUMBS UP SIGN}'
        # or '\U0001f44d' or '👍'
        await message.add_reaction(emoji)
        print("Button pressed [Select]")
        keyboard.press(keySelect)
        keyboard.release(keySelect)


@bot.listen()
async def on_message(message):
    if message.content.startswith(prefix + '~start'):
        channel = message.channel

        emoji = '\N{THUMBS UP SIGN}'
        # or '\U0001f44d' or '👍'
        await message.add_reaction(emoji)
        print("Button pressed [Start]")
        keyboard.press(keyStart)
        keyboard.release(keyStart)


bot.run(token)
