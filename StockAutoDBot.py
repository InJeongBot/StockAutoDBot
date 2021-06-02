import discord
from discord.ext import commands
from discord.utils import get
import time

TOKEN = 'ODQ5MzIwNDkxMDM0NDc2NTc0.YLZdWA.p-WmM6WWo-ROl4A3JekAnjPpmm4'

bot = commands.Bot(command_prefix = '`')
client = discord.Client()

administrator_id = 270403684389748736

# Event 디스코드 시작
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game('주식 변동'))
    print('Logging')
    print(bot.user.name)
    print('TOKEN =', TOKEN)
    print('Successly access')

@bot.command()
async def 주식자동변동(ctx, t_time):
    if ctx.message.author.id == administrator_id:
        all_channels = ctx.guild.text_channels
        for ch in all_channels:
            if ch.topic == '#인정주식':
                await ctx.send(f'주식 자동변동 시간이 {t_time}초로 설정되었습니다.')
                while True:
                    t = time.time()
                    time.sleep(int(t_time))
                    while True:
                        if time.time() >= t + int(t_time):
                            await ch.send('주식변동')
                            await ch.send('주식정보')
                            break

bot.run(TOKEN)