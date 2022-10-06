#input 
import random
print("---------------------")
print("--ADIVINA EL NUMERO--")
print("---------------------")

g=random.randint(0,1000)
n=int(input("Digite un numero entre un numero 0 y 1000: "))
i=0
if n>=0 and n<=1000:
    while n!=g:
        i=i+1
    
        if n>g:
            print("INCORRECTO: Intente con un numero menor")
        else:
            print("INCORRECTO: Intente con un numero mayor")
        n=int(input("Digite un numero entre un numero 0 y 1000: "))
    print ("el numero es:"+str(n)+", lo logro en el intento "+ str(i))
    
else: 
    print ("NO CUMPLE CONDICIONES")

