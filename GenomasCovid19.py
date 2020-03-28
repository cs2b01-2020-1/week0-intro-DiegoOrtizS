from time import time

tiempoInicial = time()

def CompararGenomasDeCoronavirus(archivo1, archivo2):
    cont  = 0

    archivoCopia1 = open(archivo1, "r")
    covidGenoma_a = str(archivoCopia1.read())
    archivoCopia1.close()

    archivoCopia2 = open(archivo2, "r")
    covidGenoma_b = str(archivoCopia2.read())
    archivoCopia2.close()

    covidGenoma_menor = min(len(covidGenoma_a), len(covidGenoma_b))
    
    i = 0
    while i < covidGenoma_menor:
        if covidGenoma_a[i] == covidGenoma_b[i]:
            cont = cont + 1
        i = i + 1
    cont  = 100*cont
    return cont

def Llenar(matriz, array):
    lista = [0]*len(array)

    print("Considerando las columnas como el conjunto de genomas de partida y las filas como el conjunto de genomas de llegada")
    print("Para calcular el porcentaje de similitud se ha multiplicado el número de similitudes por 100")
    print("y se ha dividido entre la longitud del genoma de llegada, redondeándolo a 2 decimales", "\n")
    print("               ", end = "")

    for i in range (len(archivos)):
        print("CovidGenoma",i+1, end = "    ")
        archivoCopia = open(array[i], "r")
        archivoCopia_ = str(archivoCopia.read())
        lista[i] = len(archivoCopia_)
        archivoCopia.close()
    print("")

    for i in range (len(archivos)):
        print("CovidGenoma",i+1, end = "       ")
        for j in range (len(archivos)):
            #Matriz triangular superior
            if j > i:
                matriz[i][j] = CompararGenomasDeCoronavirus(array[j],array[i])
                print(round(matriz[i][j]/lista[j],2), end = "            ")
            else:
                #Diagonal
                if i == j:
                    matriz[i][j] = "100  "
                #Matriz triangular inferior
                else:
                    matriz[i][j] = round(matriz[j][i]/(lista[j]), 2)
                print(matriz[i][j], end = "            ")
        print("")

#Main
archivos = ["AY274119.txt", "AY278488.2.txt", "MN908947.txt", "MN988668.txt", "MN988669.txt"]
matriz = [[0 for i in range(len(archivos))]for i in range(len(archivos))]
Llenar(matriz, archivos)
tiempoFinal   = time()
print("\nTiempo de ejecución: ", tiempoFinal - tiempoInicial)
