import numpy as np
import sympy as sp
from decimal import Decimal


class Assess:
    @staticmethod
    def check_error(a, x, b, precision=15):
        result = np.dot(a, x)
        error = result - b
        shape = error.shape

        error_precise = [format(Decimal.from_float(err), '.' + str(precision)) for err in
                         np.array(error, dtype=np.float64).flatten()]
        error_precise = np.array(error_precise).reshape(shape)

        print("\n---------- Checking error ----------\n")
        print(f"x:\n{x}\n\na*x:\n{result}\n")
        print(f"b:\n{b}\n")
        print(f"error, which is (b - a*x):\n{error_precise}")

        return result, error

    @staticmethod
    def check_solution(a, b):
        print("\n---------- Checking solution with python libs ----------\n")
        try:
            x_numpy = np.linalg.solve(a, b)
            print(f"X with numpy.linalg.solve:\n{x_numpy}")
            print(f"f(x)={a.dot(x_numpy)}")
            print(f"b = {b}")
            print("Jeigu f(x) ir b sprendiniai neatitinka reiškia nekorektiškai apskaičiavo biblioteka.")
            return x_numpy
        except np.linalg.LinAlgError:
            print("Could not solve with numpy.linalg.solve - singular coefficient matrix.")
            return None


class Reflection:
    def __init__(self):
        self.debug = True

    def get_reflected_vector(self, vector, row_count):
        leading = vector[0, 0]
        sign = np.sign(leading)
        z_vector_squared = np.square(vector)
        multiplier = np.zeros((row_count, 1))

        multiplier[0, 0] = 1;

        return sign * np.sqrt(np.sum(z_vector_squared)) * multiplier

    def get_omega(self, vector, vector_reflected):
        sub = vector - vector_reflected

        return sub / np.linalg.norm(sub)

    def solve(self, matrix, free_members, eps=1e-4):
        equation_count = (np.shape(matrix))[0]
        free_member_count = (np.shape(free_members))[1]
        extended_matrix = np.hstack((matrix, free_members))

        print("Pradinė matrica: ", extended_matrix)

        # Tiesioginis etapas
        # (Ignoruojame atvejį, kai vedantysis 0, o kiti ne, kadangi informacijos apie tai
        # nebuvo suteikta teorinėje paskaitoje)
        for i in range(0, equation_count - 1):
            print(f"\n---------- Etapas {i}/{equation_count - 2} ----------\n")

            z_vector = extended_matrix[i:, i]
            print(f"Z vektorius: ", z_vector)

            # Patikriname atvejį, kai turime nulinį stulpelį (ar nereikia praleisti, kai po vedamo elemento yra visi nuliai?)
            if (np.sum(z_vector) == 0):
                # Jeigu turime, praleidžiame
                print("Praleidžiame, nes nulinis stulpelis...")
                continue

            z_vector_reflected = self.get_reflected_vector(z_vector, equation_count - i)
            print("Atspindėtas Z vektorius: ", z_vector_reflected)

            omega = self.get_omega(z_vector, z_vector_reflected)
            print("Omega: ", omega)

            Q = np.identity(equation_count - i) - 2 * omega * omega.transpose()
            print("Q: ", Q)

            extended_matrix[i:equation_count, :] = Q.dot(extended_matrix[i:equation_count, :])  # This seems wrong

            print(f"Etapas baigtas. Išplėstinė matrica:\n{extended_matrix}")

        # Atvirkštinis (Gauso) etapas
        x = np.zeros((equation_count, free_member_count))
        x_sym = sp.Matrix(x)
        used_syms = 0

        for i in range(equation_count - 1, -1, -1):
            values = (extended_matrix[i, equation_count:] - extended_matrix[i, i + 1:equation_count] * x_sym[
                                                                                                       i + 1:equation_count,
                                                                                                       :])

            for j in range(values.shape[1]):
                if (extended_matrix[i, i] < eps and abs(values[0, j]) < eps):
                    print(f"Skaičius X[{i}, {j}] gali būti betkoks. Pažymėsime kaip {'p' + str(used_syms)}")
                    x_sym[i, j] = sp.symbols('p' + str(used_syms))
                    used_syms += 1
                elif abs(extended_matrix[i, i]) < eps and abs(values[0, j]) > eps:
                    print(f"Nėra sprendinių")
                    return None, None
                else:
                    x_sym[i, j] = values[0, j] / extended_matrix[i, i]

        single_solution = used_syms <= 0

        return np.array(x_sym), single_solution


def do_task(reflection, matrix, free_members):
    x1, single_solution = reflection.solve(matrix, free_members)
    x1_lib = Assess.check_solution(matrix, free_members)
    if x1 is not None:
        print("Atsakymas: ", x1, single_solution)
        result1, error1 = Assess.check_error(matrix, x1, free_members)


reflection = Reflection()

# 8
matrixA = np.matrix([
    [4, 12, 1, 7],
    [2, 6, 17, 2],
    [2, 1, 5, 1],
    [5, 11, 7, 0]
]).astype(float)

free_membersA = (np.matrix([171, 75, 30, 50])).transpose().astype(float)

# 21
matrixB = np.matrix([
    [3, 7, 1, 3],
    [1, -6, 6, 8],
    [4, 4, -7, 1],
    [-1, 3, 8, 2]
]).astype(float)

free_membersB = (np.matrix([11, 3, 1, 1])).transpose().astype(float)

do_task(reflection, matrixA, free_membersA)
do_task(reflection, matrixB, free_membersB)
# import numpy as np
# from scipy.linalg import lu, lu_factor, lu_solve
# from time import time
# def AtspindzioMetodas(A, n):
#     flag = 0
#     # tiesioginis etapas(atspindziai):
#     for i in range(0, n - 1):
#         z = A1[i:n, i]
#         zp = np.zeros(np.shape(z))
#         zp[0] = np.linalg.norm(z)
#         omega = z - zp
#         omega = omega / np.linalg.norm(omega)
#         Q = np.identity(n - i) - 2 * omega * omega.transpose()
#         A1[i:n, :] = Q.dot(A1[i:n, :])
#         # atgalinis etapas:
#     x = np.zeros(shape=(n, nb))
#     for i in range(n - 1, -1, -1):  # range pradeda n-1 ir baigia 0 (trecias parametras yra zingsnis)
#         x[i, :] = (A1[i, n:n + nb] - A1[i, i + 1:n] * x[i + 1:n, :]) / A1[i, i]
#         A[i,:] = x[i,:]
#
#     return flag
#
# def BegalybesTikrinimas(A, n, flag):
#     flag=3
#     for i in range(n):
#         sum=0
#         for j in range(n):
#             sum=sum+A[i,j]
#             j=j+1
#             if(sum==A[i,j]and sum==0):
#                 flag=2
#     return flag
#
# def LygtiesPalyginimas(A,Rezultatai):
#     if (len(Rezultatai) == 0):
#         return ""
#     Ats = A.dot(Rezultatai)
#     return Ats
#
# def SpausdintiRezultatus(A,n,flag):
#     print("Rezultatai:")
#     rezultatai=np.empty([n,1],dtype=float)
#     if(flag==2):
#         print("Begalybesprendiniu")
#         return[]
#     elif(flag==3):
#         print("Nerasprendiniu")
#         return[]
#     else:
#         for i in range(n):
#             # print(A[i,n]/A[i,i],end="")
#             rezultatai[i,0]=A[i,n]/A[i,i]
#     print()
#     return rezultatai
#
# A=np.matrix([[3, 7, 1, 3],
#              [1, -6, 6, 8],
#              [4, 4, -7, 1],
#              [-1, 3, 8, 2]]).astype(np.float_)
# b = (np.matrix([11, 3, 1, 1])).transpose().astype(np.float_)
# # A = np.matrix([[4, 12, 1, 7],
# #              [2, 6, 17, 2],
# #              [2, 1, 5, 1],
# #              [5, 11, 7, 0]]).astype(np.float_)
# # b = (np.matrix([171, 75, 30, 50])).transpose().astype(np.float_)
# n = (np.shape(A))[0]
# nb = (np.shape(b))[1]
#
# A1 = np.hstack((A, b))
#
# flag = 0
#
# if(AtspindzioMetodas(A1,n)):
#     flag=BegalybesTikrinimas(A1,n,1)
#
# rezultatai=SpausdintiRezultatus(A1,n,flag)
# print("\nRezultatupasitikrinimasistatantipradinesalyga:")
# print(LygtiesPalyginimas(A,rezultatai))
#
#
#
# P, L, U = lu(A)
#
# #  Show the A = PLA
# np.allclose(L @ U, A)
# #  Do the factorization
# LU, p = lu_factor(A)
#
# #  Solve the system
# x1 = lu_solve((LU, p), b)
# print(x1)
# print("\nRezultatupasitikrinimaspasinaudojantpythonfunkcijom:")
# print(np.linalg.solve(x1,A,b))
