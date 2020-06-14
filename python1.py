print("Colocando a inteligência no cálculo\n")
a=int(input("Digite o valor de A:"))
b=int(input("Digite o valor de B:"))
if b==0:
    print("Não é possível calcular a divisão, você deveria saber que divisão por zero é um problema para os computadors.")
else:
    c=a/b
    print("O resultado de {0:3.2f}/{1:3.2f}={2:3.2f}".format(a,b,c))