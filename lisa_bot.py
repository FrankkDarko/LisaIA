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

current_conv = [{"role": "system", "content": os.getenv("PROMPT_SYS")},
                {"role": "assistant", "content": os.getenv("PROMTP_1_ASSISTANT")},
                {"role": "user", "content": os.getenv("PROMTP_1_USER")},
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
    my_id = int(os.getenv("DISCORD_ID"))

    if message.author == client.user:
        return

    if message.author.id == my_id:
        msg = message.content
        msg = str(msg)
        current_conv.append({"role": "user", "content": msg})
        reply = chatgpt_reply(current_conv)
        current_conv.append({"role": "assistant", "content": reply})
        await message.reply(reply, mention_author=True)




