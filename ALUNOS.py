def salvarAlunos(quantidade): 
    aluno=[]
    for i in range(quantidade):
        nome = input("nome")
        nota1 = int(input("Nota 1"))
        nota2 = int(input("Nota 2"))
        nota3 = int(input("Nota 3"))
        media = ((nota1+nota2+nota3*2)/4) 
        obs =   input("Obs") 
        aluno.append([nome,nota1,nota2,nota3,media,obs])
        
    return aluno

print(salvarAlunos(int(input("quantos alunos? "))))