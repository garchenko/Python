# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('='*20)
print('MAIOR E MENOR NÚMERO')
print('='*20)

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# logica para descobrir o menor
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3

# logica para descobrir o maior
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n3:
    maior = n2
else:
    maior = n3
    
print('-'*30)
print(f'O menor número é {menor}.')
print(f'O maior número é {maior}.')

# existe uma função pronta para descobrir o maior e o menor número, que é a função max() e min().