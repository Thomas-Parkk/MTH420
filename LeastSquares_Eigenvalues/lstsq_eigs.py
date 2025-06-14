# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name> Thomas Park
<Class> MTH 420
<Date> Saturday, June 14th 2025
"""

import numpy as np
from cmath import sqrt
from scipy import linalg as la
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    Q, R = la.qr (A, mode="economic")
    Q_Tb = Q. T@ b
    matrix_solved = la. solve_triangular (R, Q_Tb)
    return matrix_solved
    # raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    house = np. load( "housing .npy")

    years = house[:, 0]
    house_price_index = house[:, 1]

    A = np. column_stack((years,
np. ones (len (years))))
    b = house_price_index

    solution = least_squares (A, b)
    slope, intercept = solution

    plt.figure(figsize=(10, 6))
    plt.scatter(years, price_index, color='k', marker='*', label='Data Points')

    x_line = np.linspace(min(years), max(years), 100)
    y_line = slope * x_line + intercept

    plt.plot(x_line, y_line, label=f'Least Squares Fit: y = {slope:.4f}x + {intercept:.4f}', color='blue')
    plt.xlabel('Year since 2000')
    plt.ylabel('Housing Price Index')
    plt.title('Housing Price Index with Least Squares Fit')
    plt.legend(loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
            
    return slope, intercept
    # raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
housing_data = np.load("housing.npy")

years = housing_data[:, 0]
house_price_index = housing_data[:, 1]

x_ref = np.linspace(min(years), max(years), 1000)
degrees = [3, 6, 9, 12]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for i, degree in enumerate(degrees):
    A = np.vander(years, degree + 1)
    coeffs = la.lstsq(A, house_price_index)[0]
    poly = np.poly1d(coeffs)
    y_ref = poly(x_ref)

    axes[i].scatter(years, house_price_index, color='k', marker='*', label='Data Points')
    axes[i].plot(x_ref, y_ref, label=f'Degree {degree} Polynomial', color='blue')

    # For comparison using np.polyfit
    polyfit_coeffs = np.polyfit(years, house_price_index, degree)
    polyfit_poly = np.poly1d(polyfit_coeffs)
    y_polyfit = polyfit_poly(x_ref)
    axes[i].plot(x_ref, y_polyfit, label='np.polyfit result', linestyle='--', color='red')

    axes[i].set_title(f'Polynomial Fit (Degree {degree})')
    axes[i].set_xlabel('Year (0 = 2000)')
    axes[i].set_ylabel('House Price Index')
    axes[i].legend(loc='best')
    axes[i].grid(True, linestyle='--', alpha=0.7)

    print(f"Degree {degree} comparison:")
    print("Our coefficients:       ", coeffs)
    print("np.polyfit coefficients:", polyfit_coeffs)
    print("Max difference:         ", np.max(np.abs(coeffs - polyfit_coeffs)))
    print()

plt.tight_layout()
plt.show()

    # raise NotImplementedError("Problem 3 Incomplete")


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")

if __name__ == "__main__":
    least_squares(A, b)
    line_fit()
    polynomial_fit()