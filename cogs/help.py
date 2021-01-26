import functions
import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.check(functions.beta_tester)
    async def help(self, ctx, menu=None):
        if menu == "utility":
            embed = discord.Embed(
                colour= discord.Colour.orange(),
                title = "🛠️ Utility commands",
                description = "`stats`, `bio`, `pfp`, `banner`, `profile`, `junior`, `date`, `nickname`, `latest`, `oldest`, `latestfeed`, `oldestfeed`, `cheers`, `comments`, `pictures`"
            )
        elif menu == "other":
            embed = discord.Embed(
                colour= discord.Colour.orange(),
                title = "📖 Other commands",
                description = "`doc`, `invite`"
            )   
        elif menu == "random":
            embed = discord.Embed(
                colour= discord.Colour.orange(),
                title = "<:RRQuestion:803587583187746847> \"Random\" commands",
                description = "`randombio`"
            )
        else:
            embed = discord.Embed(
                colour= discord.Colour.orange(),
                title = "RecNetBotV2 Command List"
            )

            embed.add_field(name="🛠️ Utility", value="`.help utility`")
            embed.add_field(name="<:RRQuestion:803587583187746847> \"Random\"", value="`.help random`")
            embed.add_field(name="📖 Other", value="`.help other`")
        
       
        functions.embed_footer(ctx, embed)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))