
# exercício 9
def T(n):
      if n == 1:
        return 1
      else:
        return n + T(n - 1)
      
# ex 11
def Rotina(L, j):
    if j == 1:
        return L
    
    i = L.index(max(L[:j]))
    
    L[i], L[j-1] = L[j-1], L[i]

    return Rotina(L, j-1)

L = [3, 7, 4, 2, 6]

Rotina(L, 5)
print(L)




# l = [3,7,4,2,6]
# ListaRotina(l, 5)

# print(l)
