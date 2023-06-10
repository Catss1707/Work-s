i= int(input(('Digite a quantidade total de alunos: ')))
alunos=[]
for x in range(i):
    nome= input('Digite o nome do aluno: ')
    n1= int(input('Digite a primeira nota do aluno: '))
    n2= int(input('Digite a segunda nota do aluno: '))
    n3= int(input('Digite a terceira nota do aluno: '))
    obs= input('Escreva uma observação sobre o aluno: ')
    media= n1 + n2 + (n3*2) / 4
    
    alunos.append([nome,n1,n2,n3,media,obs])
    if media >= 5:
        print('O aluno {} que obteve as notas {},{} e {} com média final de {}, tem seu status como aprovado.'.format(nome,n1,n2,n3,media))
    elif media < 5:
        print('O aluno {} que obteve as notas {},{} e {} com média final de {}, tem seu status como reprovado.'.format(nome,n1,n2,n3,media))
    else:
        print('Caminho não escrito')
p= input('Digite o nome do aluno que queira localizar: ')
for aluno in alunos:
    if p in aluno:
        print(aluno)

    