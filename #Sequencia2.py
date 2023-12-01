#Sequencia1

#Calcula a seguinte sequencia a partir da entrada do usuário: S = 1/1-2/4+3/9-4/16+5/25-6/36...(+/-)N/N*N para N>=50


def calcular_S(n):
    resultado = 0
    for i in range(1,n+1):
        numerador = ((-1)**(i+1))*i
        denominador = i**2
        resultado = resultado + numerador/denominador
    return resultado

# Solicitar a entrada do usuário para N
n = int(input("Sabendo que N é um número inteiro positivo>=50, informe o valor de N: "))
if n<50:
    print("O valor de N não é aceito")
else:   
    valor_S = calcular_S(n)
    print(f"O valor de S para N = {n} é {valor_S}")


