def soma(a, b):
    print(a+b)
def subtrai(a, b):
    print(a - b)

def mutiplica(a, b):
    print(a * b)

def divide(a, b):
    print(a / b)

def calc(op, a, b):
    if op == '+':
        soma(a,b)
    elif op == '-':
        subtrai(a, b)
    elif op == '*':
        mutiplica(a,b)
    elif op == '/':
        divide(a,b)
    else:
        print('Operador inválido')
    
