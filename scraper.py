import requests
import pprint
from bs4 import BeautifulSoup

import os

import discord
from dotenv import load_dotenv


myid = '<@187284750736556035>'
URL = 'https://longap.com/product/longap-one/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
mydivs = soup.find_all("div", class_="elementor-element-d2e2377")

for x in mydivs:
    if(x.find('p').text == "Available for order soon."):

        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')

        client = discord.Client()
        @client.event
        async def on_ready():
            print(f'{client.user} has connected to Discord!')
            
        @client.event
        async def on_message(message):
                await message.channel.send("hej <@187284750736556035>")

        client.run(TOKEN)
#print(mydivs)
#results = soup.find(soup.findAll('div'),)


