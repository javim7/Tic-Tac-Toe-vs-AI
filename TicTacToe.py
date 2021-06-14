__author__ = "Javier Mombiela"
__copyright__ = "Copyright 2021, Tic Tac Toe vs AI"
__credits__ = ["Tech with Tim"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Javier Mombiela"
__email__ = "rjmombiela@gmail.com"
__status__ = "Production"

#creando el tablero e iniciandolo con espacios vacios
tablero = [' ' for x in range (10)]

#funicon main: controla lo que pasa en el juego y interactua con el usuario
def main():
    print("\nBienvenido a Tic Tac Toe!\n")
    imprimir_tablero()

    #empezando el ciclo infinito que simule los turnos de los jugadoresz
    while not(esta_lleno(tablero)):
        #if para ver si la compu gano o no
        if not(es_ganador(tablero, 'O')):
            turno_jugador() #le toca al jugador
            imprimir_tablero()
        else: #significa que hay una linea completa de O's
            print("\nOooops, la computadora te ha ganado!\n") #imprimiendo mensaje de perder
            break

        #if para ver si el jugador gano
        if not(es_ganador(tablero, 'X')):
            turno_compu() #le toca a la computadora
            imprimir_tablero()
        else: #significa que hay una linea completa de O's
            print("\nExcelente, le has ganado a la computadora!\n") #imprimiendo mensaje de ganar
            break


    #if para ver si el tablero esta lleno o no
    if esta_lleno(tablero):
        print("\nHas empatado con la computadora!\n") #imprimir mensaje de empate

#funcion para poder insertar una letra en el tablero
def insertar_letra(letra, pos):

    # Parametros:
    #    letra (string): letra que se ingresara en el tablero.
    #    pos (int): posicion en la cual se ingresara la letra

    tablero[pos] = letra

#funcion para ver si el espacio esta libre o no
def espacio_libre(pos):

    # Parametros:
    #    pos (int): posicion en la cual se ingresara la letra

    #Retorna:
    #True or False: Dependiendo de si el espacio esta libre o no.

    return tablero[pos] == ' '

#funcion para poder imprimir el tablero
def imprimir_tablero():

    print('   |   |')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   |')

#funcion para ver quien es el ganador
def es_ganador(tab, letra):

    # Parametros:
    #    tablero (lista): es el tablero creado.
    #    letra (string): letra que ha ganado.

    #Retorna:
    #    True/False: Dependiendo si el jugador gana o no.

    return ((tab[7] == letra and tab[8] == letra and tab[9] == letra) or  # horizontal arriba
    (tab[4] == letra and tab[5] == letra and tab[6] == letra) or  # horizontal en medio
    (tab[1] == letra and tab[2] == letra and tab[3] == letra) or  # horizontal abajo
    (tab[7] == letra and tab[4] == letra and tab[1] == letra) or  # vertical izquierda
    (tab[8] == letra and tab[5] == letra and tab[2] == letra) or  # vertical en medio
    (tab[9] == letra and tab[6] == letra and tab[3] == letra) or  # vertical derecha
    (tab[7] == letra and tab[5] == letra and tab[3] == letra) or  # diagonal
    (tab[9] == letra and tab[5] == letra and tab[1] == letra))  # diagonal

#funcion para ver si el tablero esta lleno o no
def esta_lleno(tab):

    #Parametros:
    #    tablero (lista): el tablero creado.

    #Retorna:
    #    True/False: Dependiendo si el tablero esta lleno o no.

    #if para ver cuantos espacios vacios hay
    if tablero.count(' ') > 1:
        return True
    else:
        return False

#funcion para simular el turno del jugador
def turno_jugador():

    #while para hacer ciclo
    corrida = True
    while corrida:
        #guarcando en una variable el espacio en donde se ingresa la X
        movimiento = input("\nSeleccione un espacio par ingresar una 'X' (1-9): ")

        #try catch para asegurar que el input sea correcto
        try:
            movimiento = int(movimiento) #asegurando que el input sea un entero

            #if para asegurar que el numero este en un rango aceptable
            if movimiento > 0 or movimiento < 10:
                #if para ver si el espacio esta libre o no
                if espacio_libre(movimiento):
                    corrida = False #se termina el input porque es un valor acetable
                    insertar_letra("X", movimiento) #se inserta la letra X en el espacio escogido

                else: #else por si el espacio esta tomado
                    print("\nOoops, este espacio esta ocupado, escoge otro!")

            else: #else por si el numero esta fuera de rango
                print("\nPor favor ingrese un numero que este en el rango!\n")

        except:
            print("\nPor favor ingrese un numero entero!\n")


#funcion para simular el turno de la computadora
def turno_compu():
    pass

#llamando al main para que corra el programa
main()