# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print('='*30)
print('CALCULO DE AUMENTO SALARIAL')
print('='*30)

salario = float(input("Digite o valor do salário: R$ "))

print('-'*40)
if salario <= 1250:
    novo_salario = salario + (salario * 0.15) # calculo alternativo: (salario * 15 /100)
    print(f"O salário de R${salario:.2f}, com o aumento de 15%, passará a ser de R${novo_salario:.2f}")
else:
    novo_salario = salario + (salario * 0.10) # calculo alternativo: (salario * 10 /100)
    print(f"O salário de R${salario:.2f}, com o aumento de 10%, passará a ser de R${novo_salario:.2f}")