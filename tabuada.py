while True:
    n = int(input("Digite um número: "))

    print()
    print("Tabuada com for")
    for i in range(1,11):
        print("{} x {} = {}".format(n, i, n*i))

    print()
    print("Tabuada com while")

    j = 1
    while j <= 10:
        print("{} x {} = {}".format(n, j, n*j))
        j = j + 1

    control = input("Y - continua | N - Encerra: ")
    if control.upper() != 'Y':
        break;
    
