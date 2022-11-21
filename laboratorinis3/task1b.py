from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return (np.log(x) / (np.sin(2 * x) + 1.5)) + (x / 5)

# gaunama interpoliuojama funkcija
def calculate_interpolated_point(x, coefficients):
    n=len(coefficients)
    base = np.zeros(len(coefficients))
    for i in range(n):
        base[i] = x**i

    y = np.dot(base, coefficients)
    return y

# get f(x) points in start-stop range
def get_fx_points(begin, end, increment):
    x = []
    y = []
    current = begin

    while current <= end:
        x.append(current)
        y.append(f(current))
        current = current + increment

    return x, y


# get interpolated function points in start-stop range
def get_interpolated_points(begin, end, increment, coefficients):
    x = []
    y = []
    current = begin

    while current <= end:
        x.append(current)
        y.append(calculate_interpolated_point(current, coefficients))
        current = current + increment

    return x, y


if __name__ == "__main__":

    # duotas intervalas
    a = 2
    b = 10

    # laisvai pasirenkamas taškų skaičius
    n = 30

    x = []
    y = []

    # true = tolygūs, false = čiobyševo
    first = False

    #x taškų sudarymas
    if first:
        x = np.linspace(a, b, n, endpoint=True)
    else:
        for i in range(n):
            tempX = ((b - a) / 2) * np.cos((np.pi * (2 * i + 1)) / (2 * n)) + (b + a) / 2
            x.append(tempX)

    #y taškų sudarymas
    for i in range(n):
        y.append(f(x[i]))

    # randa funkcijos x reikšmes
    A = np.zeros((n, n))

    for i in range(n):

        for j in range(n):
            A[i, j] = x[i]**j

    # randa koeficientus
    coefficients = np.linalg.solve(A, y)
    print("Koeficientai:\n", coefficients)

    # randa funkcijos taškus
    x_fx, y_fx = get_fx_points(a, b, 0.01)

    # randa interpoliuotos funkcijos taškus
    x_interpolated, y_interpolated = get_interpolated_points(a, b, 0.01, coefficients)

    # piešia grafiką
    plt.title('f(x) = ln(x)/(sin(2x) + 1,5) + x/5')
    plt.plot(x_fx, y_fx, label='Funkcija f(x)')
    plt.plot(x_interpolated, y_interpolated, label='Interpoliuota funkcija f(x)', color="red", linestyle='dashed')
    plt.fill_between(x_fx, y_fx, y_interpolated, color="orange", label="Netiktis")
    plt.scatter(x, y, label='Funkcijos f(x) taškai')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(0.5)
    plt.show()