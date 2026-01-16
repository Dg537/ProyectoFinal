import discord, os, random
from discord.ext import commands
import asyncio

intents = discord.Intents.default() # almacenamiento de los privilegios del bot
intents.message_content = True # Activar lectura de mensajes
bot = commands.Bot(command_prefix="/",intents=intents) # Creacion de bot y transferencia de los privilegios

questions = ["Al hacer composta estas ayudando al medio ambiente",
             "Los productos biodegradables no tienen defectos y solo tienen beneficios",
             "Comprar productos locales y de temporada es mucho mejor que en supermercados",
             "La energia nuclear es una de las formas de produccion de energia mas limpias y sustentables.",
             "Los carros electricos son la solucion perfecta contra el efecto invernadero",
             "El resiclaje una de las mejores medidas contra la contaminacion"]

answersList = [["verdadero","v","true","t"],["falso","f","false"],["verdadero","v","true","t"],["verdadero","v","true","t"],["falso","f","false"],["falso","f","false"]]
info = [

"¿Por qué la compostación contribuye a la reducción de la contaminación?\n"
"La compostación evita la disposición de residuos orgánicos que, de otro modo, podrían generar contaminación ambiental al ser quemados en vertederos o depósitos de basura. Además, el compost resultante es un fertilizante natural de alta calidad que puede sustituir a los fertilizantes químicos. Esta sustitución reduce la producción, distribución y uso de productos químicos, contribuyendo así a minimizar el impacto ambiental asociado a estos procesos.\n\n"
"Para mas informacion, puedes consultar la siguiente página: \nhttps://www.unep.org/es/noticias-y-reportajes/reportajes/compostar-puede-ayudarnos-reducir-nuestro-impacto-en-el-planeta\n"
"Para ver los beneficios de la composta, puedes consultar la siguiente página: https://residus.gencat.cat/es/ambits_dactuacio/valoritzacio_reciclatge/el_compost/beneficis_us_compost/index.html",

"Aunque los productos biodegradables son más ecológicos que los convencionales, no todo es tan sencillo; como ocurre con cualquier cosa, tienen tanto ventajas como desventajas.\n"
"Muchas personas piensan que estos productos no son tan efectivos como los tradicionales, pero esto no es cierto. La mayoría de los productos biodegradables tienen una calidad comparable a la de los productos normales. Por otro lado, existe la creencia de que los productos biodegradables son mejores porque se descomponen más rápido; sin embargo, para que esto ocurra, se requieren procesos especiales. Además, algunos de estos productos ni siquiera son compostables.\n\n"
"Para más información, puedes consultar la siguiente página: https://econserve.mx/mitos-y-realidades-de-los-desechables-biodegradables/",

"Adquirir productos locales representa una opción más favorable, ya que contribuye a la reducción de la contaminación generada por el transporte y el embalaje de mercancías. Además, estos productos suelen ser más económicos y saludables. Al optar por el consumo local, también se fomenta el desarrollo económico de la comunidad.\n\n"
"Para más información, puedes consultar la siguiente página: \nhttps://sdg2advocacyhub-org.translate.goog/latest/the-benefits-of-buying-local-and-seasonal/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc",

"Aunque pueda resultar sorprendente, la producción de energía nuclear es, de hecho, la segunda fuente de generación de energía más limpia. Esto se debe a que genera una cantidad mínima de contaminantes y requiere un consumo reducido de materia prima. Además, la construcción de una central nuclear demanda significativamente menos espacio en comparación con una planta convencional.\n\n"
"La energía nuclear ha sido objeto de críticas debido a los pocos accidentes ocurridos en estas instalaciones. Si bien estos incidentes pueden tener consecuencias devastadoras para el medio ambiente, su frecuencia es considerablemente menor en comparación con otros métodos de generación energética.\n\n"
"Como se puede observar, la energía nuclear es una opción segura y, además, altamente rentable, dado que el suministro de uranio es abundante y su consumo es mínimo.\n\n"
"Para más información, puedes consultar la siguiente página: https://www.almendron.com/tribuna/desmontando-los-10-mitos-sobre-la-energia-nuclear/",

"Los vehículos eléctricos suelen considerarse la solución ideal, ya que no emiten contaminantes derivados de la combustión de combustibles fósiles; sin embargo, esta percepción no es del todo precisa. Aunque no generan contaminación de esa manera, sí contribuyen a la contaminación por otros medios. Por ejemplo, al finalizar la vida útil de las baterías utilizadas en estos vehículos, estas no se reciclan adecuadamente, sino que suelen desecharse.\n\n"
"Para entenderlo mejor, la vida útil promedio de una batería es de aproximadamente cinco años, mucho menor que la duración promedio de un automóvil convencional. Esto ha incrementado la demanda de minerales como el níquel, el cobalto y el litio, cuya extracción requiere el uso de maquinaria minera de gran escala que, a su vez, consume combustibles fósiles. "
"Para más información, puedes consultar la siguiente página: https://www.gaceta.unam.mx/el-lado-oscuro-de-los-vehiculos-electricos/",

"El reciclaje es considerado una de las mejores formas para reducir la contaminación, ¿verdad? Sin embargo, la realidad es diferente. Aunque no lo creas, el reciclaje es una medida contra la contaminación que aporta muy poco. De hecho, en algunas ocasiones puede ser incluso perjudicial. Esto sucede porque la mayoría de las personas no sabe diferenciar correctamente entre materiales reciclables y no reciclables; como resultado, toneladas de productos altamente contaminantes, como el poliestireno y el unicel, terminan en los centros de reciclaje. "
"Sé lo que estás pensando, pero aunque todas las personas aprendieran a reciclar correctamente, el impacto real sería limitado.\n\n"
'Las "tres erres" han sido un concepto que, con el tiempo, ha envejecido la idea del reciclaje. De estas tres, el reciclaje es la última y debería ser la última opción, no la primera. La primera es reducir: esta es la que genera el mayor cambio, ya que implica producir menos desde el inicio. La segunda es reutilizar: darle un segundo uso a los objetos para prolongar su vida útil. Finalmente, reciclar: este es el último recurso y, aunque suele ser el único proceso que se aplica, muchas veces se hace con la errónea idea de que con ello se está ayudando significativamente al medio ambiente.\n'
"Para más información, puedes consultar las siguientes páginas:\n\n"
"https://www.xataka.com/ecologia-y-naturaleza/llevamos-decadas-reciclando-basura-que-producimos-expertos-dicen-que-no-ha-servido-para-nada-1\n"
"https://www.biobiochile.cl/noticias/sociedad/debate/2023/05/03/reciclar-no-es-virtuoso-esta-empeorando-las-cosas-investigador-explica-por-que-esta-sobrevalorado.shtml"]


#GUILD_ID = discord.Object(id=1366819659944562804)

@bot.tree.command(name="minigame", description="Inicia el juego del medio ambiente")
async def minigame(interaction: discord.Interaction):
    
    index = 0
    aciertos = 0

    await interaction.response.send_message('¡Empezamos! Responde a las preguntas sobre el medio ambiente con verdadero o falso.')
    
    while True:
        #index = random.randint(0, len(questions) - 1)
        await interaction.channel.send(f"**Pregunta:** {questions[index]}")

        # Función para verificar que la respuesta sea del mismo usuario y canal
        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel

        try:
            # Esperar respuesta del usuario (tiempo límite 60 seg)
            msg = await bot.wait_for('message', check=check, timeout=60.0)
            
            if msg.content.lower() in answersList[index]:
                await interaction.channel.send("¡Respuesta correcta!")
                aciertos += 1
                
                await interaction.channel.send("¿Quisieras ver más información? **(Y/N)**")
                res_info = await bot.wait_for('message', check=check, timeout=30.0)
                
                if res_info.content.lower() == "y":
                    await interaction.channel.send(f"{info[index]}")
            
            else:
                await interaction.channel.send(f"Incorrecto. La respuesta era: **{answersList[index][0]}**")
                
                await interaction.channel.send("¿Quisieras ver más información? **(Y/N)**")
                res_info = await bot.wait_for('message', check=check, timeout=30.0)
                
                if res_info.content.lower() == "y":
                    await interaction.channel.send(f"{info[index]}")

            index += 1

            if index <= len(questions)-1:
                await interaction.channel.send("\n*¿Quieres seguir jugando? (Y/N)*")
                continuar = await bot.wait_for('message', check=check, timeout=60.0)
                if continuar.content.lower() not in ["si", "y", "yes"]:
                    await interaction.channel.send(f"Has hacertado un total de {aciertos} de {index} preguntas.")
                    await interaction.channel.send("Gracias por jugar. ¡Hasta pronto!")
                    break
            else:
                await interaction.channel.send("\n¡Felicidades! Has terminado el juego.")
                await interaction.channel.send(f"Has hacertado un total de {aciertos} de {index} preguntas.")
                break
            

        except asyncio.TimeoutError:
            await interaction.channel.send("Te quedaste dormido... El juego ha terminado.")
            break

@bot.event
async def on_ready():
    # Paso 1: Limpia los comandos del servidor (si registraste alguno ahí)
    # Reemplaza con tu ID real para limpiar la caché local
    mi_server = discord.Object(id=1366819659944562804)
    bot.tree.clear_commands(guild=mi_server)
    await bot.tree.sync(guild=mi_server)
    
    # Paso 2: Sincroniza de forma global
    await bot.tree.sync()
    
    print(f'Sincronización completada. Bot listo: {bot.user}')

bot.run('Token aqui')
