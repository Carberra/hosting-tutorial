import os

import hikari
import lightbulb
import miru


class RpsView(miru.View):
    @miru.button(label="Rock", emoji="🪨", style=hikari.ButtonStyle.PRIMARY)
    async def btn_rock(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.edit_response("Paper!")
        self.stop()

    @miru.button(label="Paper", emoji="📰", style=hikari.ButtonStyle.PRIMARY)
    async def btn_paper(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.edit_response("Scissors!")
        self.stop()

    @miru.button(label="Scissors", emoji="✂️", style=hikari.ButtonStyle.PRIMARY)
    async def btn_scissors(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.edit_response("Rock!")
        self.stop()

    @miru.button(emoji="🛑", style=hikari.ButtonStyle.DANGER, row=2)
    async def btn_stop(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.edit_response("Stopped.")
        self.stop()

    async def on_timeout(self) -> None:
        await self.message.edit("Timed out!", components=[])


bot = lightbulb.BotApp(
    os.environ["TOKEN"],
    default_enabled_guilds=int(os.environ["DEFAULT_GUILD_ID"]),
    help_slash_command=True,
    intents=hikari.Intents.ALL,
)
miru.load(bot)


@bot.command()
@lightbulb.command("rps", "Rock Paper Scissors")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_rps(ctx: lightbulb.SlashContext) -> None:
    view = RpsView(timeout=60)
    response = await ctx.respond("Rock Paper Scissors!", components=view.build())
    view.start(await response.message())
    await view.wait()


def run() -> None:
    if os.name != "nt":
        import uvloop
        uvloop.install()

    bot.run()
