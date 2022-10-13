import numpy as np
A=np.matrix([[4, 12, 1, 7],
             [2, 6, 17, 2],
             [2, 1, 5, 1],
             [5, 11, 7, 0]]).astype(np.float_)
b = (np.matrix([171, 75, 30, 50])).transpose().astype(np.float_)
n = (np.shape(A))[0]
P = np.arange(0, n)
# tiesioginis etapas:
for i in range(0, n-1):
    a = max(abs(A[i:n, i]));
    iii = abs(A[i:n, i]).argmax()
    A[[i, i+iii], :] = A[[i+iii, i], :] #sukeiciamos eilutes
    P[[i, i+iii]] = P[[i+iii, i]] #sukeiciami eiluciu numeriai

    for j in range(i+1, n):
        r = A[j, i]/A[i, i]
        A[j, i:n+1] = A[j, i:n+1]-A[i, i:n+1]*r;
        A[j, i] = r;
    b = b[P]

print("y reiksmes")
# 1-as atvirkstinis etapas, sprendziama Ly=b, y->b
for i in range(1, n):
    b[i] = b[i] - A[i, 0:i]*b[0:i]
    print(b[i])
print("x reiksmes")
# 2-as atvirkstinis etapas , sprendziama Ux=b, x->b
for i in range(n-1, -1, -1):
    b[i] = (b[i] - A[i, i+1:n] * b[i+1:n]) / A[i, i]
    print(b[i])



#
# MAX = 100
#
#
# def luDecomposition(A, n):
#     L = [[0 for x in range(n)]
#              for y in range(n)]
#     U = [[0 for x in range(n)]
#              for y in range(n)]
#
#     # Decomposing matrix into Upper
#     # and Lower triangular matrix
#     for i in range(n):
#
#         # Upper Triangular
#         for k in range(i, n):
#
#             # Summation of L(i, j) * U(j, k)
#             sum = 0
#             for j in range(i):
#                 sum += (L[i][j] * U[j][k])
#
#             # Evaluating U(i, k)
#             U[i][k] = A[i][k] - sum
#
#         # Lower Triangular
#         for k in range(i, n):
#             if (i == k):
#                 L[i][i] = 1  # Diagonal as 1
#             else:
#
#                 # Summation of L(k, j) * U(j, i)
#                 sum = 0
#                 for j in range(i):
#                     sum += (L[k][j] * U[j][i])
#
#                 # Evaluating L(k, i)
#                 L[k][i] = int((A[k][i] - sum) /
#                                   U[i][i])
#
#     # setw is for displaying nicely
#     print("L\t\t\t\t\tU")
#
#     # Displaying the result :
#     for i in range(n):
#
#         # Lower
#         for j in range(n):
#             print(L[i][j], end="\t")
#         print("", end="\t")
#
#         # Upper
#         for j in range(n):
#             print(U[i][j], end="\t")
#         print("")
#
#     return L, U
#
#
# # Driver code
# A = [[4, 12, 1, 7], [2, 6, 17, 2], [2, 1, 5, 1], [5, 11, 7, 0]]
# b = [171, 75, 30, 50]
# nn = len(b)
# L, U = luDecomposition(A, nn)
#
# print("y reiksmes")
# # 1-as atvirkstinis etapas, sprendziama Ly=b, y->b
# for i in range(1,4) :
#     b[i]=b[i]-A[i,0:i]*b[0:i]
#     print(b[i])
# print("x reiksmes")
# # 2-as atvirkstinis etapas , sprendziama Ux=b, x->b
# for i in range (4-1,-1,-1) :
#     b[i]=(b[i]-A[i,i+1:4]*b[i+1:4])/A[i,i]
#     print(b[i])


