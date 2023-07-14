# a = ['AGTB','GTXAB',"GTB"]
# def fn(i, j, k):
#   # i-th char of a, j-th char of b
  
#   if (i == len(a[0]) or j == len(a[1]) or k == len(a[2])):
#     return 0
  
#   if (a[0][i] == a[1][j] == a[2][k]):
#     return 1+fn(i+1, j+1, k+1)
  
#   return max(
#     fn(i+1, j),
#     fn(i, j+1),
#     fn(i,j,k+1)
#   )

# fn(0,0,0)

def test():
    return 1 , 2


L = [0,0]

L[0] , L[1] = test()
print(L)