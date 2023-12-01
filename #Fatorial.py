#Calcula o Fatorial a partir da entrada de um número pelo usuário

fat =1
n = int(input("Informe um número: "))
for i in range(n,1,-1):
    fat = fat*i
print(fat)