
import random

print('En este "juego" tendras que responder a algunas preguntas sobre el medio anbiente y sobre las soluciones a este')

questions = ["¿De que color es el amarillo?","¿Cuanto es dos mas dos entre dos?"] # agregare las preguntas reales despues de una investigacion
answersList = ["pues azul ovio", "3"]
info = ["Esto pasa porque pues el amarillo es de color azul y asi", "La preguna dice, cuanto es 2 mas 2 entre 2. El resultado es 3 ya que por \n"
"jerarquia de operaciones la divicion se resuelve primeso asi que vasicamente es 2 entre dos que es 1 mas 2 que da 3."]

while True:

    answerIndex = random.randint(0,1)

    print(f"La pregunta es {questions[answerIndex]}")

    userAnswer = input("Respuesta: ")

    if userAnswer == answersList[answerIndex]:  # respuesta correcta

        print("¡Respuesta correcta!")
        
        userAnswer = input("¿Quisieras ver mas informacion? (Y/N): ").lower() # mas informacion?

        if userAnswer == "n":  #  no
            print("Proxima pregunta")
            continue

        elif userAnswer == "y":  # si
            print(info[answerIndex])
            continue

        else:
            continue

    elif userAnswer != answersList[answerIndex]:  # respuesta incorrecta
        print("Respuesta incorrecta")
        print(f"La respuesta correcta es {answersList[answerIndex]}")

        print(info[answerIndex])
