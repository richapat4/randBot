import discord
import os
import pandas as pd
import random 

# Hello hokul is here

def readCsv(string):
    df = pd.read_csv("RandomFacTgeneratorNew.csv",encoding='utf-8')
    y = df[string].values.tolist()
    return y[random.randint(0, len(y) - 1)]


# def main():
#     readCsv('Science')

# if __name__ == "__main__":
#     main()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents =intents)

@client.event
async def on_ready():
    print ('Logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('fact'):
        b = message.content.lower()
        x = b.split(':')
        if len(x) == 1:
            await message.channel.send('on what topic? Please select from : history, science, math')
        elif x[1] == 'science':
            await message.channel.send(readCsv('Science'))
        elif x[1] == 'history':
            await message.channel.send(readCsv('History'))
        elif x[1] == 'math':
            await message.channel.send(readCsv('Math'))
        else:
            await message.channel.send('Topic not found, ensure that the command is of form fact:topic')
    # else:
    #     await message.channel.send('Would you like to hear an interesting fact? If yes please type fact:topic with topic of choice from : history, science, math')

client.run()





