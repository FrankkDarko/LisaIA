import discord
from dotenv import load_dotenv
import openai
import os

# Load Token and api
load_dotenv()
token = os.environ['BOT_TOKEN']
openai.api_key = os.environ['OPENAI_API_KEY']

# connect to discord
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# current_conv

msg_system = "Une ia femme nommée Lisa qui adore apporté sont aide, es toujour joyeuse et ça arrive parfois d'ajouter une touche d'humour a tes réponse."

current_conv = [{"role": "system", "content": msg_system},
                {"role": "assistant", "content": "Bonjour je me présente je suis Lisa votre assitante personnel"},
                {"role": "user", "content": "Bonjour Lisa, tu es a mon service désormé"},
                ]


# Ask OpenAI / ChatGPT
def chatgpt_reply(conv):

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conv,
        max_tokens=350
    )

    return completion['choices'][0]['message']['content']


# Print Bot is start
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Verif User and reply to them
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.author.id == 200549635067084800:
        msg = message.content
        msg = str(msg)
        current_conv.append({"role": "user", "content": msg})
        reply = chatgpt_reply(current_conv)
        current_conv.append({"role": "assistant", "content": reply})
        await message.reply(reply, mention_author=True)


# Start the bot
def starter():
    client.run(token)


