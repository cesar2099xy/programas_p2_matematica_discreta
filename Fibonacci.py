# Lê um número inteiro e calcula seu número de Fibonacci
numero = int(input("Digite um número inteiro não nulo: "))

if numero <= 0:
    print("Número inválido. Por favor, insira um número positivo maior que zero.")
else:
    fib1, fib2 = 1, 1
    if numero == 1 or numero == 2:
        resultado = 1
    else:
        for i in range(3, numero + 1):
            resultado = fib1 + fib2
            fib1, fib2 = fib2, resultado
    print(f"O número de Fibonacci de F{numero} é {resultado}.")