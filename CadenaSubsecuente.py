text1 = input("Ingrese cadena 1: ")
text2 = input("Ingrese cadena 2: ")

array1 = list(text1)
array2 = list(text2)
L = [];
i=0;
while (i < len(array1)):
  if (array1[i] == array2[i]):
    L.append(array1[i])
  i = i + 1 ;
print("La cadena subsecuente es: ",L)

