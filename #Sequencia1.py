#Sequencia1

#Calcula a seguinte sequencia a partir da entrada do usuário: H = 1/1+3/2-5/3+7/4-...(+/-)(N*2-1)/N para N>=50


def calcular_H(n):
    resultado = 0
    for i in range(1,n+1):
        numerador = ((-1)**(i+1))*(2*i-1)
        denominador = i
        resultado = resultado + numerador/denominador
    return resultado


# Solicitar a entrada do usuário para N
n = int(input("Sabendo que N é um número inteiro positivo>=50, informe o valor de N: "))
if n<50:
    print("O valor de N não é aceito")
else:
    valor_H = calcular_H(n)
    print(f"O valor de H para N = {n} é {valor_H}")
    

