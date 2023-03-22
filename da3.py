import random ,os
num_a_eliminar=()
num_a_reincorporar=()
from sumadisponibles import sumar_lista
from letrubi import es_letra
def lanzar_dados():
  dado1 = random.randint(1, 6)
  dado2 = random.randint(1, 6)
  return dado1 + dado2  
  
import os

def opciones_numeros(disponibles, eliminados, puntos):
    while puntos > 0:
        os.system('cls' if os.name == 'nt' else 'clear') # Código para limpiar pantalla
        print(f"Tienes {puntos} puntos disponibles")
        print(f"Disponibles: {', '.join(map(str, sorted(disponibles)))}") # Presentar la lista de manera ordenada
        print(f"Eliminados: {', '.join(map(str, sorted(eliminados)))}") # Presentar la lista de manera ordenada
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
    print("Bienvenido a la numerala, el objetivo del juego es eliminar todos los números, recuerde que si la sumatoria de todos los números disponibles es menor que los puntos que obtuvo al tirar los dados el juego finalizara.")
    while disponibles:
        print(disponibles,"disponibles")
        print(eliminados,"eliminados")
        resultado=sumar_lista(disponibles)
        print(resultado,"sumatoria de disponibles")
        boton = input("Presiona x para lanzar los dados: ")
        if boton == "x":
            puntos = lanzar_dados()
            if sumar_lista(disponibles) < puntos:   #aca
                respuesta = input(f"¡Lo siento! Perdiste,obtuviste {puntos} puntos,¿deseas jugar de nuevo? (s/n): ")
                if respuesta.lower() == "s":
                    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    eliminados = []
                    continue
                else:
                    break   #hasta aca
            opciones_numeros(disponibles, eliminados, puntos)
            print(f"Números eliminados: {eliminados}")
            #if sumar_lista(disponibles) < puntos:   #aca
                #respuesta = input("¡Lo siento! Perdiste, ¿deseas jugar de nuevo? (s/n): ")
                #if respuesta.lower() == "s":
                    #disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    #eliminados = []
                    #continue
                #else:
                    #break   #hasta aca
        else:
            print("Botón inválido, vuelve a intentarlo")
    print("¡Felicidades, has eliminado todos los números!")

juego()