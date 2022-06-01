import os

import hikari
import lightbulb


bot = lightbulb.BotApp(
    os.environ["TOKEN"],
    default_enabled_guilds=int(os.environ["DEFAULT_GUILD_ID"]),
    help_slash_command=True,
    intents=hikari.Intents.ALL,
)


@bot.command()
@lightbulb.option("text", "The thing to say.")
@lightbulb.command("echo", "Say something!")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_echo(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond(ctx.options.text)


def run() -> None:
    if os.name != "nt":
        import uvloop
        uvloop.install()

    bot.run()
