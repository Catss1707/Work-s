from time import sleep
def calculate():
    operacao = input("Digite a operacao desejada (soma,sub,mult,div): ")
    x = float(input("Insira o primeiro valor: "))
    y = float(input("Insira o segundo valor: "))

    import soma
    import sub
    import mult
    import div

    if operacao == 'soma':
        soma.soma(x,y)
    elif operacao == 'sub':
        sub.sub(x,y)
    elif operacao == 'mult':
        mult.mult(x,y)
    elif operacao == 'div':
        div.div(x,y)
    else:
        print('Operacao invalida!')
    again()

def again():
    calc_again = input('''
    Voce deseja calcular novamente?
    Digite S para sim  e N para nao.
    ''')
    if calc_again.upper()=='S':
        calculate()
    elif calc_again.upper()=='N':
        print('See you later :)')
        sleep(5)
    else:
        again()

calculate()