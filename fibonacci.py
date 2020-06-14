
print("\n            Cálculo da Sequência de Fibonacci\n\n")
n = int(input("Digite um número: "))

n1, n2 = 0, 1
count = 0

if n <= 0:
   print("Favor inserir um número positivo inteiro")
else:
   print("A sequência é:")
   while count < n:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count += 1