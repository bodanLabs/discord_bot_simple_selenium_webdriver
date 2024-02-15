import asyncio
from discord.ext import commands, tasks
import discord
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

TOKEN = "BOT_TOKEN"

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!",intents=intents)

#on ready
@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity = discord.Activity(type=discord.ActivityType.watching, name = "News"))


@client.command()
async def news(ctx,*,keyword):
    print("looking...")
    options = Options()
    options.add_argument('--lang=en-GB')
    options.headless = True
    driver = webdriver.Chrome(options=options)
    kw = keyword.replace(" ","+")
    print(kw)

    driver.get(f'https://www.google.com/search?q={kw}&tbs=qdr:d,sbd:1&tbm=nws&tbas=0&source=lnt&sa=X&ved=2ahUKEwiX4fX4nIT3AhVn_rsIHdDHCEIQpwV6BAgBECU&biw=1365&bih=969')

    butt = driver.find_element(By.XPATH,value="/html/body/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button")
    butt.click()

    await asyncio.sleep(1)
    driver.save_screenshot("test.png")
    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(description=f"No News found for this keyword",color=15158332)
        await ctx.send(embed=embed)

    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[2]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        pass

    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[3]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[3]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        pass


    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[4]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[4]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        pass


    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[5]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[5]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        pass


    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[6]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[6]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        pass



    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[7]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[7]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        pass



    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[8]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[8]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        pass




    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[9]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[9]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        pass


    try:
        firstLink = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[10]/g-card/div/div/a").get_attribute("href")
        firstText = driver.find_element(By.XPATH,value="/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[10]/g-card/div/div/a").text
        split = firstText.split('\n')
        source = split[0]
        title = split[1]
        description = split[2]
        embed = discord.Embed(title=f"{title}", description=f"{description}\n`Source: {source}`",url=firstLink,color=1752220)
        await ctx.send(embed=embed)
    except:
        pass

client.run(TOKEN)
print(client.user.name)