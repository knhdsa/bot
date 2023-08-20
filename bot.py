import discord
import random
from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

token = config.get("set1", "token")

p = "*"  # Prefix for your bot's commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=p, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} Bot command")

@bot.command()
async def สุ่มเลข(ctx):
    number = random.randint(1, 101)
    await ctx.send(f"Random Number: {number}")

@bot.command()
async def สวัสดี(ctx):
    await ctx.send(f"สวัสดีครับคุณ")

@bot.command()
async def rov(ctx):

    badlist = ["มาเล่น rov กันเพื่อน","มาเล่น rov กัน","มาเล่น rov ไหมเพื่อน"]
    badlist = random.choice(badlist)
    await ctx.send(f"{badlist}")

@bot.command()
async def ลุงตู่(ctx):
    badlist = ["https://tenor.com/view/ถูกใจสิ่งนี้-ประยุทธ-prayuth-yes-smile-gif-13943512",
               "https://mpics.mgronline.com/pics/Images/563000005307201.JPEG",
               "https://tenor.com/th/view/ลุงตู่-ตู่-สเปรย์-spray-tooh-gif-20705281"]

    badlist = random.choice(badlist)
    await ctx.send(badlist)

@bot.command()
async def ไอ้เลว(ctx):
    
    badlist = ['ไอ้คนเลวที่สุดในโลกที่เจอมาเลย','ไอ้คนเลว','ไอ้เลว','ไอ่เลวโง่ที่สุด']
    badlist = random.choice(badlist)
    await ctx.send(f"{badlist}")

'''
@bot.command()
async def test5(ctx):
    for i in range(5):
        i +=1   
        await ctx.send(f"test {i}")
'''

bot.run(token)