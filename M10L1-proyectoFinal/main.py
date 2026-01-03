import discord, os, random
from discord.ext import commands

intents = discord.Intents.default() # almacenamiento de los privilegios del bot
intents.message_content = True # Activar lectura de mensajes
bot = commands.Bot(command_prefix="/",intents=intents) # Creacion de bot y transferencia de los privilegios


@bot.event
async def on_ready():
    print(f'Conectado al sistema como: {bot.user}')


@bot.command()
async def minigame(ctx):
    await ctx.send('En este "juego" tendras que responder a algunas preguntas sobre el medio anbiente y sobre las soluciones a este')

    questions = ["¿De que color es el amarillo?","¿Cuanto es dos, mas dos entre dos?"] # agregare las preguntas reales despues de una investigacion
    selectedQuestion = random.choices(questions)
    userAnswer = None # se le agregara valor proximamente

    await ctx.send(selectedQuestion)
    await ctx.send("Respuesta: ")

    # codigo por aqui
    
    if userAnswer == selectedQuestion:

        await ctx.send("¡Respuesta correcta! ¿Te gustaria ver mas informacion sobre el tema?")

        # codigo para guardar la respuesta del usuario    

        if userAnswer == "si" or "y":
            None

    else:
        await ctx.send("¡Respuesta incorrecta!")
