#Sequencia3

#Calcula a seguinte sequencia a partir da entrada do usuário: P = 2/pot(1,3)+3/pot(3,3)+5/pot(5,3)+7/pot(7,3)+11/pot(9,3)+......onde n é o número de termos da sequencia, sendo um número inteiro e positivo >= 5

def calcular_P(n):
    resultado = 0
    for i in range(1,n+1):
        c=0
        for z in range(1,i+1):
            if i%z==0:
                c=c+1
        if c<3: #divide por ele mesmo e por 1 para ser primo
            numerador = i
            denominador = (2*i-1)**3
            resultado = resultado + numerador/denominador
    return resultado


# Solicitar a entrada do usuário para N
n = int(input("Sabendo que N é um número inteiro positivo>=50, informe o valor de N: "))
if n<50:
    print("O valor de N não é aceito")
else:
    valor_P = calcular_P(n)
    print(f"O valor de P para N = {n} é {valor_P}")


