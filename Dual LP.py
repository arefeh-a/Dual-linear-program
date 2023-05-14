import numpy as np

minmax = input("please enter type of optimization MIN or MAX upper case: ")

A_rows = int(input("please enter number of a's rows :"))
A_cols = int(input("please enter number of a's cols :"))

C_list = [0.0 for i in range(A_cols)]
for i in range(A_cols):
    print("please enter the c ", i, "th element")
    C_list[i] = float(input())

A_list = [[0.0 for j in range(A_cols)]for i in range(A_rows)]
for i in range(A_rows):
    for j in range(A_cols):
        print("please enter the ", i, " th row , ", j , "th column :")
        A_list [i][j] = float(input())

print("note: for entering sign of variables pleas enter one of <=0, =0 FREE")
sign_of_X = [0.0 for i in range(A_cols)]
for i in range(A_cols):
    print("please enter the sign of ", i, "th variable")
    sign_of_X[i] = input()

B_list = [0.0 for i in range(A_rows)]
for i in range(A_rows):
    print("please enter the b ", i, "th element")
    B_list[i] = float(input())
    
Limitation = [0.0 for i in range(A_rows)]
print("note: for entering limitation pleas enter one of <=, = >=")
for i in range(A_rows):
    print("please enter the ", i, "th limitation")
    Limitation[i] = input()

A = np.asarray(A_list)
b = np.asarray(B_list)
c = np.asarray(C_list)

Dual_c = b
Dual_b = c
Dual_A = np.transpose(A)

if minmax == 'MIN':
    Dual_minmax = 'MAX'
elif minmax == 'MAX':
    Dual_minmax = 'MIN'
else: 
   print("ERROR! PLEASE ENTER A VALID MIN OR MAX")

Dual_limitation = [None for i in range(A_cols)]
if minmax == 'MIN':
    for i in range(A_cols):
        if sign_of_X[i] == '>=0':
            Dual_limitation[i] = '<='
        elif sign_of_X[i] == 'FREE':
            Dual_limitation[i] = '='
        elif sign_of_X[i] == '<=0':
            Dual_limitation[i] = '>='
        else:
            print("ERROR! PLEASE ENTER A VALID SIGN")
else:
    for i in range(A_cols):
        if sign_of_X[i] == '>=0':
            Dual_limitation[i] = '>='
        elif sign_of_X[i] == 'FREE':
            Dual_limitation[i] = '='
        elif sign_of_X[i] == '<=0':
            Dual_limitation[i] = '<='
        else:
            print("ERROR! PLEASE ENTER A VALID SIGN")
            
Dual_sign = [None for i in range(A_rows)]
if minmax == 'MIN':
    for i in range(A_rows):
        if Limitation[i] == '>=':
            Dual_sign[i] = '>=0'
        elif Limitation[i] == '<=':
            Dual_sign[i] = '<=0'
        elif Limitation[i] == '=':
            Dual_sign[i] = 'FREE'
        else:
            print("ERROR! PLEASE ENTER A VALID LIMITATION")    
else:
    for i in range(A_rows):
        if Limitation[i] == '>=':
            Dual_sign[i] = '<=0'
        elif Limitation[i] == '<=':
            Dual_sign[i] = '>=0'
        elif Limitation[i] == '=':
            Dual_sign[i] = 'FREE'
        else:
            print("ERROR! PLEASE ENTER A VALID LIMITATION")
            
print(Dual_minmax)      
print("c:\n", Dual_c)
print("A:\n", Dual_A)
print("limitations:\n", Dual_limitation)
print("b:\n", Dual_b)
print("signs:\n", Dual_sign)
