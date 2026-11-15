# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=-'*12)
print('ANALISADOR DE TRIANGULOS')
print('=-'*12)


r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

print('-'*40)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')