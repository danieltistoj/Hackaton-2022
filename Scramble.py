def existe(array,letra):

    for i in range(0,len(array)):
        if array[i] == letra:
            return True

    return False

def extraer_caracter(cadena):
    array = []
    for x in range(0,len(cadena)):
        if len(array)!=0:
            aux = cadena[x]
            if cadena[x].isupper():
                aux = cadena[x].swapcase()
            if existe(array,aux)!=True:
                array.append(aux)
        else:
            if cadena[x].isupper():
                aux = cadena[x].swapcase()
                array.append(aux)
            else:
                array.append(cadena[x])
    return array


def comparacion(array1,array2):
    if len(array1)!= len(array2):
        return False
    else:
        for i in range(0,len(array1)):
            contador = 0
            for j in range(0,len(array2)):
                if array1[i] == array2[j]:
                    contador+=1
            if contador == 0:
                return False
        return True


cadena1  = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

array1 = extraer_caracter(cadena1)
array2 = extraer_caracter(cadena2)
print(array1)
print(array2)
print(comparacion(array1,array2))
