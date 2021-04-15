import discord
from discord.ext import commands
import wikipedia
import googletrans
from googletrans import Translator

token = 'yourtoken'
bot = commands.Bot(command_prefix='?')

@bot.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason: str = 'Причина блокування не вказана.'):
    await member.ban(reason=reason, delete_message_days=0)
    await ctx.send(embed = discord.
 Embed(description = (f"**{member} заблокований**"),color=0xc582ff))
 
@bot.command()
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason: str = 'Причина вигнання не вказана.'):
    await member.kick(reason=reason)
    await ctx.send(embed = discord.
 Embed(description = (f"**{member} вигнаний**"),color=0xc582ff))

@bot.command()
async def user(ctx, Member: discord.Member = None ):
    if not Member:
        Member = ctx.author
    emb = discord.Embed(title='Інформація про користувача'.format(Member.name), description=f"Приєднався: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
    f"Нікнейм: {Member.name}\n\n"
    
   f"Нікнейм на сервері: {Member.nick}\n\n"
                                                                                      f"Статус: {Member.status}\n\n"
                                                                                      f"ID: {Member.id}\n\n"
                                                                                      f"Найвища роль: {Member.top_role}\n\n"
                                                                                      f"Аккаунт створений: {Member.created_at.strftime('%b %#d, %Y')}", 
                                                                                      color=0xc582ff, timestamp=ctx.message.created_at)
 
    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    await ctx.send(embed=emb)
 
@bot.command()
@commands.has_permissions( administrator = True )
async def delete(ctx, amount= None):
         await ctx.channel.purge(limit = int(amount) + 1)
         await ctx.send(embed= discord.Embed(description = (f'**Видалено {amount} повідомлення.**'), color=0xc582ff))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, команди не існує**', color=0xc582ff))
   

@bot.command()
@commands.has_permissions( administrator = True )
async def unban( ctx, *, member = None ):
    if member is None:
         await ctx.send(embed = discord.Embed(description = f'{ ctx.author.name }, вкажіть користувача', color = 0x4f4db3 ))
    else:
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban( user )
            await ctx.send(embed = discord.Embed(description = (f"**{member} розблокований**"),color=0xc582ff))

@bot.command()
async def wiki(ctx, *, text):
  try:    
    wikipedia.set_lang("uk")
    new_page = wikipedia.page(text)
    summ = wikipedia.summary(text)
    emb = discord.Embed(
        title= new_page.title,
        description= summ,
         color=0xc582ff
    )
    emb.set_author(name= 'Повна стаття', url= new_page.url, icon_url= 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
    await ctx.send(embed=emb)
  except Exception:
    return await ctx.send(embed = discord.Embed(description = (f"**Такої статті не існує**"),color=0xc582ff))

@bot.event
async def on_ready():
    game = discord.Game(r"?help")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def trans(ctx, lang: str, r: str, *, text):
  try:
    t = Translator()
    result = t.translate(text, src = lang, dest = r)
    await ctx.send(embed = discord.
  Embed(description = (f'**Переклад:** \n{result.text}'),color=0xc582ff))
  except Exception:
    return await ctx.send(embed = discord.Embed(description = (f"**Мова вказана не вірно**"),color=0xc582ff))   
    
bot.run(token)
