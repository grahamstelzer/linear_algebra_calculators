# Goal: write a class that is able to parse polynomials and apply operations on them
# ex: a user needs to multiply x^2 + 1 * x^3 + 5x^2 + 7
# ex: a user needs to calculate the integral of x^3
#
# functionality should also print out relevant information that the user may need to use
# ex: online calculators may just give the result of an operation, this should give steps
#
# methodology: basically just parsing user input, storing as a list of coefficients
# ex: user enters: 1 + 3x^2 and asks to multiply by 1 + 2x, this is really just [1, 0, 3] * [1, 2]
# 
# notes: 
# - also allows degree specification
# - might need to build an integral class, but currently has a method for it


from fractions import Fraction

class Polynomial:
    def __init__(self, n, coeffs=None, expr=None):
        self.n = n
        if coeffs is not None:
            self.coeffs = coeffs
        elif expr is not None:
            self.coeffs = self.parse_expr(expr)
        else:
            self.coeffs = [0] * (n + 1)

    def parse_expr(self, expr):
        terms = expr.split('+')
# print(terms)
        coeffs = [0] * (self.n + 1) # generate a list of 0s
        for term in terms:
            term = term.strip() # remove leading/trailing whitespace
            if 'x^' in term:
                c, p = term.split('x^') # split the term into coefficient and power
                if c == '': # if coefficient not specified by user, assume 1
                    c = 1
# print(f"c: {c}, p: {p}")
                coeffs[int(p)] += int(c)
            elif 'x' in term:
                if term == 'x':
                    coeffs[1] += 1
                else:
                    c, _ = term.split('x')
                    coeffs[1] += int(c)
            else:
                coeffs[0] += int(term)
# print(f"Coefficient list: {coeffs}")
        return coeffs

    def __mul__(self, other):
        result_n = self.n + other.n
        result_coeffs = [0] * (result_n + 1)
        for i in range(self.n + 1):
            for j in range(other.n + 1):
                result_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(result_n, coeffs=result_coeffs)

    def __add__(self, other):
        max_n = max(self.n, other.n)
        self_coeffs = self.coeffs + [0] * (max_n - self.n)
        other_coeffs = other.coeffs + [0] * (max_n - other.n)
        result_coeffs = [a + b for a, b in zip(self_coeffs, other_coeffs)]
        return Polynomial(max_n, coeffs=result_coeffs)

    def __str__(self):
        terms = []
# print(f"coeffs: {self.coeffs}")
        for i, c in enumerate(self.coeffs):
            if c != 0:
                c = Fraction(c).limit_denominator()  # convert to fraction
                if c == 1:
                    if i == 0:
                        terms.append(str(c))
                    elif i == 1:
                        terms.append("x")
                    else:
                        terms.append(f"x^{i}")
                else:
                    if i == 0:
                        terms.append(str(c))
                    elif i == 1:
                        terms.append(f"({c})x")
                    else:
                        terms.append(f"({c})x^{i}")
        if not terms:
            return "0"
        else:
            return " + ".join(terms)
        
    def integral(self, a, b):
        result = 0
        # generate new coefficient list for the antiderivative by adding an extra space for the new coefficient:
        new_coeffs = [0] * (self.n + 2)
        for i, c in enumerate(self.coeffs):
            new_coeffs[i + 1] = c / (i + 1)
        self.coeffs = new_coeffs
# print(f"New coefficient list: {self.coeffs}")

    
        # print the new polynomial of the antiderivative:
        print(f"Antiderivative: {str(self)}")

        # calculate the result of the antiderivative at the upper bound:
        for i, c in enumerate(self.coeffs):
            result += c * b ** i

        # subtract the result of the antiderivative at the lower bound: 
        for i, c in enumerate(self.coeffs):
            result -= c * a ** i

        

        # print result as fraction:
        return Fraction(result).limit_denominator()
        # return result


# # test integral
# degree = int(input("Enter the degree of the polynomial: "))
# expr = input("Enter a polynomial (form should be {1,x,x^2...}): ")
# poly = Polynomial(n=degree, expr=expr)
# print(f"Created the polynomial {str(poly)}")

# # Perform integration
# a = int(input("Enter the lower bound of the interval: "))
# b = int(input("Enter the upper bound of the interval: "))
# result = poly.integral(a, b)
# print(f"Result of integration over [{a}, {b}]: {result}")


# # test multiplication or addition
# degree = int(input("Enter the degree of the polynomial: "))
# expr = input("Enter a polynomial (form should be {1,x,x^2...}): ")
# poly = Polynomial(n=degree, expr=expr)
# print(f"Created the polynomial {str(poly)}")

# # Perform multiplication or addition
# operation = input("Multiply or Add? ").strip().lower()
# if operation == "multiply":
#     expr2 = input("Enter another polynomial: ")
#     poly2 = Polynomial(n=degree, expr=expr2)
#     result = poly * poly2
#     print(f"Result of multiplication: {str(result)}")
# elif operation == "add":
#     expr2 = input("Enter another polynomial: ")
#     poly2 = Polynomial(n=degree, expr=expr2)
#     result = poly + poly2
#     print(f"Result of addition: {str(result)}")
# else:
#     print("Invalid operation. Please choose 'multiply' or 'add'.")
