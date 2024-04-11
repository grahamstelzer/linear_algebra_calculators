import Polynomial as poly

# create inner_product class that will use coefficient list form Polynomial:

class Inner_Product:
    def __init__(self, vector_space, inner_product_space):


# test with 2 polynomials:
print("Enter the degree of the first polynomial: ")
degree1 = int(input())
print("Enter the first polynomial (form should be {1,x,x^2...}): ")
expr1 = input()

poly1 = poly.Polynomial(n=degree1, expr=expr1)
print(f"Created the polynomial {str(poly1)}")


print ("Enter the degree of the second polynomial: ")
degree2 = int(input())
print("Enter the second polynomial (form should be {1,x,x^2...}): ")
expr2 = input()

poly2 = poly.Polynomial(n=degree2, expr=expr2)
print(f"Created the polynomial {str(poly2)}")


# Perform inner product
inner_product = Inner_Product(poly1, poly2)
print(inner_product)