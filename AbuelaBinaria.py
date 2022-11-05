
def sumaCorrecta(n,suma):
    if(n == suma):
        return True
    return False
def sumarUnos(bin):
    contador = 0
    for i in range(0,len(bin)):
        if bin[i] == "1":
            contador+=1
    return contador


N = int(input("Ingrese el valor N: "))
num1 = int(input("Ingrese el valor 1: "))
num2 = int(input("Ingrese el valor 2: "))
suma = num1 + num2
if sumaCorrecta(N,suma):
    bin1 = format(num1,"b")
    bin2 =format(num2,"b")
    print(bin1,bin2)
    cantidad1 = sumarUnos(bin1)
    cantidad2  = sumarUnos(bin2)
    total = cantidad1 + cantidad2
    print("La abuela le dara a sus nietos",total,"avellanas")
else:
    print("Los numeros no suman")
