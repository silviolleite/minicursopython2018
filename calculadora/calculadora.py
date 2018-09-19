def _soma(a, b):
    print(a+b)
def _subtrai(a, b):
    print(a - b)

def _mutiplica(a, b):
    print(a * b)

def _divide(a, b):
    print(a / b)

def calc(op, a, b):
    if op == '+':
        _soma(a,b)
    elif op == '-':
        _subtrai(a, b)
    elif op == '*':
        _mutiplica(a,b)
    elif op == '/':
        _divide(a,b)
    else:
        print('Operador inválido')
    
