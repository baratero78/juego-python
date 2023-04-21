import random
import os
from sumadisponibles import sumar_lista
from letrubi import es_letra

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2
def mostrar_dados(puntos):
    # Lista de representaciones gráficas de los puntos obtenidos en los dados
    dados_ascii = [
        # Dado con 1 punto
        ['+-------+',
         '|       |',
         '|  ●    |',
         '|       |',
         '+-------+'],
        # Dado con 2 puntos
        ['+-------+',
         '| ●     |',
         '|       |',
         '|     ● |',
         '+-------+'],
        # Dado con 3 puntos
        ['+-------+',
         '| ●     |',
         '|   ●   |',
         '|     ● |',
         '+-------+'],
        # Dado con 4 puntos
        ['+-------+',
         '| ●   ● |',
         '|       |',
         '| ●   ● |',
         '+-------+'],
        # Dado con 5 puntos
        ['+-------+',
         '| ●   ● |',
         '|   ●   |',
         '| ●   ● |',
         '+-------+'],
        # Dado con 6 puntos
        ['+-------+',
         '| ●   ● |',
         '| ●   ● |',
         '| ●   ● |',
         '+-------+']
    ]
    # Imprimir los dados de acuerdo a los puntos obtenidos
    for i in range(5):
        print("   ".join(dados_ascii[puntos[i]]))
def probabilidad_dados(resultado):
    total = 36
    favorable = 0
    for i in range(1,7):
        for j in range(1,7):
            if i + j > resultado:
                favorable += 1
    return favorable/total


def opciones_numeros(disponibles, eliminados, puntos):
    while puntos:
        os.system('cls' if os.name == 'nt' else 'clear') # Código para limpiar pantalla
        print(f"Tienes {puntos} puntos disponibles")
        print(f"Disponibles: {', '.join(map(str, sorted(disponibles)))}") # Presentar la lista de manera ordenada
        print(f"Eliminados: {', '.join(map(str, sorted(eliminados)))}") # Presentar la lista de manera ordenada
        resultado=sumar_lista(disponibles) # Calcula la nueva sumatoria de disponibles
        probabilidad = probabilidad_dados(resultado) # Calcula la probabilidad con la nueva sumatoria
        
        # Mostrar la probabilidad de fracaso con esferas "●"
        fracaso = int(probabilidad * 10) # Convierte la probabilidad a un número entero del 1 al 10
        esferas = "●" * fracaso # Crea una cadena de esferas "●" con la cantidad correspondiente al fracaso
        print(f"Probabilidad de fracaso: {esferas}")
        
        try:
            num = int(input("Ingresa el número que deseas eliminar o recuperar: "))
            if num in disponibles and num <= puntos:
                disponibles.remove(num)
                eliminados.append(num)
                puntos -= num
            elif num in eliminados:
                eliminados.remove(num)
                disponibles.append(num)
                puntos += num
            else:
                print("Número no válido")
        except ValueError:
            print("Por favor ingresa un número válido")
            
    return disponibles, eliminados, puntos



def juego():
    disponibles = [1,2,3,4,5,6,7,8,9]
    eliminados = []
    print("Bienvenido a la numerala, el objetivo del juego es eliminar todos los números disponibles,para hacerlo debe usar los puntos obtenidos en el lanzamiento de dados, recuerde que si la sumatoria de todos los números disponibles es menor que los puntos que obtuvo al tirar los dados el juego finalizara.")
    while disponibles:
        print(disponibles,"disponibles")
        print(eliminados,"eliminados")
        resultado=sumar_lista(disponibles)
        print(resultado,"sumatoria de disponibles")
        probabilidad = probabilidad_dados(resultado) # Calcula la probabilidad con la nueva sumatoria
        print(f"La probabilidad de que la suma de un lanzamiento de 2 dados de 6 caras sea mayor a {resultado} es {probabilidad}") # Muestra la probabilidad
        # Agregar opción para volver a la última decisión
        boton = input("Presiona ´x´ para lanzar los dados, presiona ´v´ para volver a la jugada anterior: ")
        if boton == "x":
            puntos = lanzar_dados()
            if sumar_lista(disponibles) < puntos:
                respuesta = input(f"¡Lo siento! Perdiste, obtuviste {puntos} puntos, ¿deseas jugar de nuevo? (s/n): ")
                if respuesta.lower() == "s":
                    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    eliminados = []
                    continue
                else:
                    break
            opciones_numeros(disponibles, eliminados, puntos)
            print(f"Números eliminados: {eliminados}")
        else:
            print("Botón inválido, vuelve a intentarlo")
    print("¡Felicidades, has eliminado todos los números!")

juego()
