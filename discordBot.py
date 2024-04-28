import interactions
from interactions import (slash_command, SlashContext, listen, slash_option, OptionType,
                          StringSelectMenu, component_callback, ComponentContext, Embed, File,
                          Button, ButtonStyle, Timestamp, Intents)

from scripts.python.update import update
from utils.wlanCon import get_wlan_info
from os import path
from config.config import Config
from time import sleep
import subprocess


configData = Config("config/config.yaml")

useDiscordBot = configData.get_value("discord", "useDiscordBot")
token = configData.get_value("discord", "discordBotToken")

source_channel_id = configData.get_value("discord", "sourceChannelId")
destination_channel_id = configData.get_value("discord", "destinationChannelId")
status_channel_id = configData.get_value("discord", "statusChannelId")
status_channel = None
bot = None
sleep(60)

if useDiscordBot:
    bot = interactions.Client(token=token, intents=Intents.GUILDS | Intents.ALL)
else:
    print("Disabled Discord Bot")

@listen()
async def on_ready():
    global status_channel
    status_channel = bot.get_channel(status_channel_id)
    print(f"Discord Bot: Logged in as {bot.user}")
    print("Connected to the following guild:\n")
    for guild in bot.guilds:
        print(f"\t{guild.name} (id: {guild.id})")
    await status_channel.send(embed=embed_template("online", "Bot got started!", bot.user))


@listen()
async def on_message_create(ctx):
    if int(ctx.message.channel.id) != source_channel_id:
        return

    if ctx.message.content == "refresh":
        await ctx.message.delete()
        await refresh_image(ctx)


@slash_command(name="ping", description="Ping command.")
async def ping(ctx: SlashContext):
    await ctx.send(f"Pong! ({bot.latency*1000}ms)")


@slash_command(name="usage", description="Shows the usage of the bot.")
async def usage(ctx: SlashContext) -> None:
    refresh_button = Button(
        style=ButtonStyle.PRIMARY,
        label="Refresh",
        custom_id="refresh_button"
    )

    embed = Embed(title="Usage", color=0x7289DA)
    embed.add_field(
        name="Refresh Button",
        value="Click the button to refresh the image."
    )

    await ctx.channel.send(embed=embed, components=refresh_button)
    await ctx.send("Setuped usage!", ephemeral=True)

@slash_command(name="settings", description="Manage the Settings")
async def settings(ctx: SlashContext):
    await ctx.send("Settings command.", ephemeral=True)

@slash_command(name="setup", description="Setup the discord bot.")
async def setup(ctx: SlashContext):
    await ctx.send("Settings command.", ephemeral=True)


@slash_command(name="exec", description="Executes a terminal command and returns the output")
@slash_option(
    name="command",
    description="Is the command which will be executed",
    required=True,
    opt_type=OptionType.STRING
)
async def info(ctx: SlashContext, command: str):
    result = subprocess.check_output([command], stderr=subprocess.STDOUT).decode('utf-8')
    await ctx.send(embed=embed_template("info", f"Terminal\n {result}", ctx.author_id))



@slash_command(name="info", description="Gets the info of the bot.")
async def info(ctx: SlashContext):
    await ctx.send(embed=embed_template("info", f"Info\n {get_wlan_info()}", bot.user))


@settings.subcommand(sub_cmd_name="edit", sub_cmd_description="Edit the Settings")
async def edit_settings(ctx: SlashContext):
    # Categorys
    components = StringSelectMenu(
        # todo load with config yaml data
        ["General", "Discord", "Home Assistant"],
        placeholder="Choose the category which you wanna edit",
        min_values=1,
        max_values=1,
        custom_id="category_select",
    )
    await ctx.send("What is your favourite food?", components=components)


@component_callback("category_select")
async def my_callback(ctx: ComponentContext):
    await ctx.edit(f"Your favourite food is {ctx.values[0]}", ephemeral=True)


@slash_command(name="clear", description="Clear messages in the channel")
@slash_option(
    name="amount",
    description="Clears the amount of messages",
    required=True,
    min_value=1,
    opt_type=OptionType.INTEGER
)
async def clear(ctx: SlashContext, amount: int):
    await ctx.channel.purge(deletion_limit=amount)
    await ctx.send(f"Cleared {amount} messages!", ephemeral=True)


async def embed_template(status, info_message, user_sent):
    colors = {
        'error': 0xFF0000,
        'success': 0x57F287,
        'info': 0x7289DA
    }

    color = colors.get(status, 0x7289DA)

    embed = Embed(
        title=f"{status.capitalize()}!",
        description=info_message,
        color=color
    )

    if status == "success":
        destination_channel = bot.get_channel(destination_channel_id)
        embed.add_field(
            name="Destination Channel",
            value=destination_channel.mention
        )

    embed.add_field(name="Sent From User:", value=user_sent.mention)
    embed.timestamp = Timestamp.now()
    return embed


async def refresh_image(ctx):
    author = ctx.author if isinstance(ctx, ComponentContext) else ctx.message.author

    destination_channel = bot.get_channel(destination_channel_id)
    
    image_path = configData.get_value("general", "imagePath") + "/" + update()

    try:
        # check if image file exists
        if path.exists(image_path):
            await status_channel.send(embed=embed_template("success", "Successfully sent the image.", author))
            print('Image sent to the destination channel')
        else:
            raise FileNotFoundError
            await destination_channel.send(file=File(image_path))

        if isinstance(ctx, ComponentContext):
            return await ctx.send(f"Image was sent into {destination_channel.mention}.", ephemeral=True)
    except FileNotFoundError:
        print('Image file not found')
        await status_channel.send(embed=embed_template("error", "File not found", ctx.author))
        if isinstance(ctx, ComponentContext):
            return await ctx.send("Image file not found.", ephemeral=True)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        await status_channel.send(embed=embed_template("error", str(e), ctx.author))
        if isinstance(ctx, ComponentContext):
            return await ctx.send(f"An unexpected error occured. Try again.", ephemeral=True)


@component_callback("refresh_button")
async def refresh_button(ctx: ComponentContext):
    await ctx.defer(ephemeral=True)
    await refresh_image(ctx)


def start_bot(bot, restart_time=5):
    try:
        bot.start()
    except Exception as e:
        print(f"Connection Error: {e}")
        print(f"Restarting Discord bot in {restart_time}!")
        sleep(restart_time)
        start_bot(bot=bot, restart_time=restart_time)

if __name__ == "__main__":
    start_bot(bot=bot, restart_time=5)
        