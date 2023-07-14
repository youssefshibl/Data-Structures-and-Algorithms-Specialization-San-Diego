#  //=============================\\
# || data structures & algorithms ||
# \\=============================//
#
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
# ⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀
# ⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀
# ⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀
# ⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
# ⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
# ⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
# ⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀⠀⠀⠀⠀⢀⣤⣤⣤⡀⠀⠀⢸⣿⣿⣿⣷⣦⠀⠀⠀
# ⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
# ⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁
#
# ┌──────────────────────────────────────────────┐
# │ 1 Algorithmic Toolbox                        │
# │ 6 week                                       │
# │ 3 Maximum Value of an Arithmetic Expression  │
# └──────────────────────────────────────────────┘


# Uses python3
def calc(one , op , two):
    if(op == "+"):
        return one + two
    elif(op == "-"):
        return one - two
    elif(op == "*"):
        return one * two
    else:
        assert False
   


M = []
P = []
m = []
def MinAndMax(i , j) :
    global M,m,P
    min_ = float("inf")
    max_ = float("-inf")
    for k in range(i , j):
        a = calc(M[i-1][k-1], P[k-1], M[k ][ j-1])
        b = calc(m[i-1][k-1], P[k-1], M[k ][ j-1])
        c = calc(M[i-1][k-1], P[k-1], m[k ][ j-1])
        d = calc(m[i-1][k-1], P[k-1], m[k ][ j-1])
        min_ = min(a, b ,c ,d,min_)
        max_ = max(a ,b ,c ,d,max_)
    return min_, max_

def parentheses(digites , operators):
    global M ,m ,P
    P = operators
    d = len(digites)
    o = d -1 
    M =  [[float("inf")] * (d) for _ in range(d)]
    m =  [[float("-inf")] * (d) for _ in range(d)]

    for i in range(0,d):
        M[i][i] = digites[i]
        m[i][i] = digites[i]
    for s in range(1 ,d):
        for i in range(1 , d-s+1) :
            j = i +s 
            m[i-1][j-1], M[i-1][j-1] = MinAndMax(i,j)
    return M[0][d-1]        




str_1 = str(input())
digits = []
operators =[]
for i in range(0,len(str_1)):
    if(i%2 == 0):
        digits.append(int(str_1[i]))
    else:
        operators.append(str_1[i])
    
print(parentheses(digits,operators))
