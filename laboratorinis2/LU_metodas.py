from turtle import pos
import numpy as np
import sympy as sp
from decimal import Decimal


class Assess:
    @staticmethod
    def check_error(a, x, b, precision=12):
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


class LUDecomposition:
    def solve(self, a, b, eps=1e-12):
        U = a

        # number of equations
        n = a.shape[0]

        L = np.identity(n)

        # number of vectors b
        m = b.shape[1]

        # number of symbolic variables used in solution
        used_syms = 0

        # boolean: whether the equation system has one or infinite solutions
        is_one_solution = True

        positions = np.arange(0, n)

        print("\nFORWARD STEP")

        for i in range(0, n - 1):
            print(f"\n---------- Stage {i}/{n - 2} ----------\n")
            # if the leading element is 0, Gaussian method does not apply
            if U[i, i] == 0:
                print(f"Leading element at [{i}, {i}] is 0, looking to switch equations.")
                max_column_index = np.argmax(abs(U[i:, i]))

                # switch rows, so that leading element is not 0
                if max_column_index + i != i:
                    print(f"Switching rows {i} and {max_column_index + i}.")

                    U[[i, i + max_column_index], :] = U[[i + max_column_index, i], :]
                    positions[[i, i + max_column_index]] = positions[[i + max_column_index, i]]

                    print(f"Augmented matrix after rearrangement\n {U}")
                else:
                    print(f"Could not find a replacement for the leading element, skipping current iteration.")
                    continue

            for j in range(i + 1, n):
                val = U[j, i] / U[i, i]
                U[j, i:] = U[j, i:] - U[i, i:] * U[j, i] / U[i, i]
                L[j, i] = val

            print(f"Stage complete. \nU matrix:\n{U}")
            print(f"L matrix:\n{L}")

        print("\nBACKWARD STEP")

        # Ly=b, y->b
        b = b[positions, :]

        for i in range(1, n):
            b[i] = b[i] - L[i, 0:i] * b[0:i]

        # Ux=b, x->b
        x = np.zeros((n, m))
        x_sym = sp.Matrix(x)

        mfull = np.hstack((a, b))

        for i in range(n - 1, -1, -1):
            print(f"\n---------- Stage {n - 1 - i}/{n - 1} ----------\n")
            vals = (mfull[i, n:] - mfull[i, i + 1:n] * x_sym[i + 1:n, :])
            for j in range(vals.shape[1]):
                if mfull[i, i] < eps and abs(vals[0, j]) < eps:
                    print(f"Variable X[{i}, {j}] may be any number. Denoted as {'p' + str(used_syms)}")
                    x_sym[i, j] = sp.symbols('p' + str(used_syms))
                    used_syms += 1
                elif abs(U[i, i]) < eps and abs(vals[0, j]) > eps:
                    print("Nėra sprendinių")
                    return None, None
                else:
                    x_sym[i, j] = vals[0, j] / mfull[i, i]

            print(f"Stage complete. X matrix:\n{np.array(x_sym)}")

        if used_syms > 0:
            is_one_solution = False

        return np.array(x_sym), is_one_solution


def do_task(lu, matrix, free_members):
    matrix_copy = matrix.copy()
    members_copy = free_members.copy()

    x1, single_solution = lu.solve(matrix, free_members)

    if x1 is not None:
        print("Atsakymas: ", x1, single_solution)
        result1, error1 = Assess.check_error(matrix_copy, x1, members_copy)

    x1_lib = Assess.check_solution(matrix_copy, members_copy)


lu = LUDecomposition()

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

do_task(lu, matrixA, free_membersA)
do_task(lu, matrixB, free_membersB)
