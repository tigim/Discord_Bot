from selenium import webdriver
from time import sleep
import os
import discord
import requests

my_token = os.environ['token']

def get_questions():
  browser = webdriver.Chrome(os.getcwd() + '/chromedriver')
  browser.get('https://leetcode.com/problems/two-sum/')
  browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
  sleep(5)
  problem_description = browser.find_element_by_class_name('question-content__JfgR')
  print(problem_description.text)
  
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$questions'):
    question = get_questions
    await message.channel.send(question)

client.run(my_token)

