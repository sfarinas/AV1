membros = int(input('Quantos membros tem na sua familia: '))
valor = 1
total = 0

while  valor <= membros:
    soma = int(input('Digite a idade do membro: '))
    
    total = soma + total

    print()
    #print('Total ', total)
    #print('membros ', membros)

    valor = valor + 1


    
media = total / membros

print('')
print('Quantidades de membros: ', membros)
print('')

print('O peso medio da familia é: ', media)