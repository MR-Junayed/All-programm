#set
set_A={1, 3, 4, 5}
print(set_A)
set_B={3, 6, 5, 8}
print(set_B)
set_C={10, 6, 14, 8}
print(set_C)
#adding
set_A.add(9)
set_B.add(9)
set_C.add(9)
print(set_A)
print(set_B)
print(set_C)
#removing
set_A.remove(9)
set_B.remove(9)
set_C.remove(9)
print(set_A,set_B,set_C)
#set  operation_union(AUBUC)
union_A_B_C=set_A.union(set_B).union(set_C)
print(union_A_B_C)
#set operation_intersection(A^B^C)
intersection_A_B_C=set_A.union(set_B).union(set_C)
print(intersection_A_B_C)