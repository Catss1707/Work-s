Nome = ['joão', 'Bruna', 'Rebeca','Liliane ','Adriano','Alisha','Anaís','Lucía','Noé','Michel']
n1 = [1,4,10,2,19,10,7,4,6,3]
n2 = [8,9,2,10,7,10,10,9,0,5]
n3 = [9,10,1,8,10,6,8,4,8,4]
media =[]
aprovados, reprovados, recu =0,0,0
for notas in range(10):
    media.append((n1[notas]+n2[notas]+(n3[notas]*2))/4)
    if media[notas] >= 7:
        print('O Aluno',Nome[notas], 'Foi Aprovado')
        aprovados +=1
    elif media[notas] <= 6 and media[notas]<=5:
        print('O Aluno', Nome[notas], "Está em Recuperação!")
        recu += 1
    else:
        print('O Aluno', Nome[notas], 'Foi Reprovado')
        reprovados +=1
print("Alunos Aprovados: ", reprovados)
print("Alunos Reprovados: ", aprovados)
print("Alunos em Recuperação: ", recu)