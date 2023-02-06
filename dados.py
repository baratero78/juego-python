import random ,os
num_a_eliminar=()
num_a_reincorporar=()
def lanzar_dados():
  dado1 = random.randint(1, 6)
  dado2 = random.randint(1, 6)
  return dado1 + dado2

def opciones_numeros(disponibles, eliminados, puntos):
    while True:
            os.system('cls' if os.name == 'nt' else 'clear') #codigo para limpiar pantalla
            print(f"Tienes {puntos} puntos disponibles")
            print(disponibles,"disponibles")
            print(eliminados,"eliminados")
            opcion = input("Ingresa 'e' para eliminar o 'r' para recuperar un número: ")
            if opcion == 'e':
                disponibles.sort()
                print(f"Números disponibles: {disponibles}")
                num_a_eliminar = int(input("Ingresa un número a eliminar: "))#plantearlo como una lista para poder eliminar de amas de uno
                if num_a_eliminar in disponibles:
                    if puntos - num_a_eliminar >= 0:
                        disponibles.remove(num_a_eliminar)
                        eliminados.append(num_a_eliminar)
                        puntos -= num_a_eliminar
                        if puntos == 0:
                            break
                    else:
                        print("No tienes suficientes puntos para eliminar ese número")
                else:
                    print("Ese número no está disponible")
            elif opcion == 'r':
                eliminados.sort()
                print(f"Números eliminados: {eliminados}")
                num_a_reincorporar = int(input("Ingresa el número a reincorporar: "))
                if num_a_reincorporar in eliminados:
                    eliminados.remove(num_a_reincorporar)
                    disponibles.append(num_a_reincorporar)
                    puntos += num_a_reincorporar
                    if puntos == 0:
                        break

def juego():
    disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    eliminados = []
    while disponibles:
        print(disponibles,"disponibles")
        print(eliminados,"eliminados")
        boton = input("Presiona x para lanzar los dados: ")
        if boton == "x":
            puntos = lanzar_dados()
            opciones_numeros(disponibles, eliminados, puntos)
            print(f"Números eliminados: {eliminados}")
        else:
            print("Botón inválido, vuelve a intentarlo")
    print("¡Felicidades, has eliminado todos los números!")

juego()