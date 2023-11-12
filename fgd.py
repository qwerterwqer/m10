import os
import random

import discord
from discord.ext import commands

import os
print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True+

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def mem(ctx):
    images = os.listdir("images")
    with open(f'images{random.choice(images)}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


#команда утка
@bot.command()
async def duck(ctx):
    duck = "произошли от кряквы. Селезни домашних уток весят 3—4 кг, утки — 2—3,5 кг. Средняя годовая яйценоскость до 250 яиц. Породы домашних уток подразделяются на мясные (пекинские, серые украинские, чёрные белогрудые), мясо-яичные (зеркальные, хаки-кемпбелл), яичные (индийские бегуны). Уток разводят во многих странах, в том числе в России."
    await ctx.send(duck)

             
bot.run("MTE2MzA1MTA1OTQ1NjAwNDE0OA.GwxbaC.WARjQ_iqIMKjYyvK9HvdSFJO6EdGJAXPAVjZ0Q")
