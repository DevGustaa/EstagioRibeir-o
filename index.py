#TESTE Estágio Ribeirão Preto - 2024


#PERGUNTA NÚMERO 1
INDICE = 13;
SOMA = 0;           #Cada variável é colocada de acordo com a questão
K = 0;

while (K < INDICE) :    #As variáveis são postas como pedido, dentro de um "Enquanto", sendo lido "Enquanto K for menor que INDICE"
    K = K + 1;          #Este while irá ficar em loop até que K seja igual a 13
    SOMA = SOMA + K;    


print(SOMA)             #No fim, o resultado será 91.

#PERGUNTA NÚMERO 2
def fibo(n):            #criamos a uma função 
    a, b = 0, 1         #definimos que a=0 e b=0
    while a <= n:       #abrimos um while, dizendo que o loop acontecerá enquanto a for menor ou igual a n(NumeroDesejado)
        if a == n:      #se a for igual a n, será retornado true
            return True
        a, b = b, a + b #o valor de a significa o número anterior, já b o próximo número
    return False        #Se o valor de a passar de n, é retornado FALSE


NumeroDesejado = int(input("Digite um número: "))

if fibo(NumeroDesejado):
    print(f"{NumeroDesejado} pertence à sequência de Fibonacci.")
else:
    print(f"{NumeroDesejado} não pertence à sequência de Fibonacci.")

#PERGUNTA NÚMERO 3
#A) 1, 3, 5, 7, 9
#B) 2, 4, 8, 16, 32, 64, 128
#C) 0, 1, 4, 9, 16, 25, 36, 49
#D) 4, 16, 36, 64, 100
#E) 1, 1, 2, 3, 5, 8, 13 
#F) 2, 10, 12, 16, 17, 18, 19, 20


#PERGUNTA NÚMERO 4
#Teriamos o interruptor A,B,C e lampadas na sala 1, 2 e 3
#Eu acenderia A e B, indo em direção a sala 1
#Se a sala 1 estivesse apagada, seria 1C
#Voltaria para o interruptor, e apagaria a B, indo visitar a sala 2
#Se sala 2 estiver apagada, seria 1C, 2B e 3A, se estivesse acesa seria 1C, 2A e 3B
#Voltando para a primeira possibilidade, se a primeira sala estivesse acesa, 1C seria descartado, pois seria 1B ou 1A
#desligaria B e visitaria a sala 2, se a sala 2 estivesse acesa, 1B, 2A, 3C, se a sala 2 estivesse apagada, porém quente, seria 1A, 2B, 3C e se estivesse apagada e fria ,1A ,2C ,3B 


#PERGUNTA NÚMERO 5
    
def inveter(s):
    return s[::-1]
    
palavra = input("escreva algo: ")
resultado = inveter(palavra)
print(resultado)