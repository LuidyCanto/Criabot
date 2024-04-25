import discord
from openai import AsyncOpenAI
from dotenv import load_dotenv
from discord.ext import commands
import os

# Carrega as variáveis de ambiente
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
aclient = AsyncOpenAI(api_key=OPENAI_API_KEY)

# Configura os intents do bot e a chave da API da OpenAI
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Função assíncrona para buscar o histórico do canal
async def buscar_historico_canal(canal, limit=5):
    messages_list = []
    async for message in canal.history(limit=limit):
        messages_list.append({
            "role": "user" if message.author.id != bot.user.id else "system",
            "content": message.content
        })
    messages_list.reverse()
    return messages_list

# Função assíncrona para perguntar ao GPT
async def ask_gpt(mensagens):
    response = await aclient.chat.completions.create(messages=mensagens,
    model="gpt-3.5-turbo-16k",
    temperature=0.9,
    max_tokens=1000)
    return response.choices[0].message.content

# Evento quando o bot fica online
@bot.event
async def on_ready():
    print(f"O {bot.user.name} ficou ligado!")
    await bot.change_presence(activity=discord.CustomActivity("Seu tutor de bioeconomia"))

# Manipulador de novas mensagens
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    async with message.channel.typing():
        mensagens = await buscar_historico_canal(message.channel)
        resposta = await ask_gpt(mensagens)
        await message.reply(resposta)

    await bot.process_commands(message)

# Inicia o bot
bot.run(DISCORD_BOT_TOKEN)



