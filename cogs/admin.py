from discord.ext import commands


class AdminCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def load_cog(self, ctx, *, cog: str):
        """Load a module
        Remember to use dot path. e.g: cogs.admin"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def unload_cog(self, ctx, *, cog: str):
        """Unload a module
        Remember to use dot path. e.g: cogs.admin"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str):
        """Reload a module
        Remember to use dot path. e.g: cogs.admin"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

def setup(bot):
    bot.add_cog(AdminCog(bot))
