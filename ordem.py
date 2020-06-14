A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
if A<B<C:
    print("\nOrdem crescente {}, {}, {}".format(A, B, C))
    print("Ordem decrescente {}, {}, {}".format(C, B, A))
elif A<C<B:
    print("\nOrdem crescente {}, {}, {}".format(A, C, B))
    print("Ordem decrescente {}, {}, {}".format(B, C, A))
elif B<A<C:
    print("\nOrdem crescente {}, {}, {}".format(B, A, C))
    print("Ordem decrescente {}, {}, {}".format(C, A, B))
elif B<C<A:
    print("\nOrdem crescente {}, {}, {}".format(B, C, A))
    print("Ordem decrescente {}, {}, {}".format(A, C, B))
elif C<B<A:
    print("\nOrdem crescente {}, {}, {}".format(C, B, A))
    print("Ordem decrescente {}, {}, {}".format(A, B, C))
elif C<A<B:
    print("\nOrdem crescente {}, {}, {}".format(C, A, B))
    print("Ordem decrescente {}, {}, {}".format(B, A, C))