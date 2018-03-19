"""
Homework #10 for CPTR454.

Solving Quadradic Polynomials

Written By Ethan Beaver
"""


def newtonSqrt(D, prev=1):
    """Compute square roots using modified Newton's Method."""
    if D < 0:
        raise ValueError("THIS ALGORITHM DOESN'T HANDLE POLYNOMIALS WITH COMPLEX ROOTS")
    nextIteration = 0.5*(prev + D/prev)
    if abs(nextIteration - prev) < 0.000001:
        return nextIteration
    else:
        return newtonSqrt(D, nextIteration)


def quadraticSolver(a, b, c):
    """Solve quadratic polynomials using custom square root function."""
    try:
        if b > 0:
            return 2*c/(-b - newtonSqrt(b**2 - 4*a*c)), (-b - newtonSqrt(b**2 - 4*a*c))/(2*a)
        else:
            return (-b + newtonSqrt(b**2 - 4*a*c))/(2*a), 2*c/(-b + newtonSqrt(b**2 - 4*a*c))
    except ValueError as e:
        print("ERROR: Please enter coefficients that give a polynomial without complex roots")
        return None, None


def polynomialSolver():
    """Helper function for solving quadratic polynomials."""
    print("Enter coefficients for ax^2+bx+c=0")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    root1, root2 = quadraticSolver(a, b, c)
    print("Root 1: ", root1)
    print("Root 2: ", root2)


if __name__ == "__main__":
    polynomialSolver()
