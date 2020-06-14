print("Pesquisa sequencial")
n = int(input("Digite n: "))
l = list(range(2, n+1, 2)) #função list + tipo range (class range(start, stop, step))
print("lista gerada", l)
x = int(input("Digite um número: "))
while x != 0:
        if x in l:
                print("{0} está na lista".format(x))
        else:
            print("{0} não está na lista".format(x))
        x = int(input("Digite um número: "))
print("Fim do Programa!")