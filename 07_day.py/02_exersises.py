A = {2, 4, 6, 8, 10, 12}
B = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
C = A.union(B)
print(C)
print(A.intersection(B))
print(A.isdisjoint(B))
AB = A.union(B)
BA = B.union(A)
print(AB,BA)
print(A.symmetric_difference(B))
del A,B