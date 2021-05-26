class TermNode:
    # exponent: int
    # coefficient: float
    # next: TermNode
    # __eq__(other: TermNode): bool
    # __ne__(other: TermNode): bool
    def __init__(self, coefficient, exponent, Next = None):
        self._coefficient = coefficient
        self._exponent = exponent
        self._next = Next

    def __eq__(self, other):
        return type(other) is type(self) and self._exponent == other._exponent and self._coefficient == other._coefficient

    def __ne__(self, other):
        return not(self == other)

class Polynomial:
    # _first_node: TermNode
    # __init__(exp, coef)
    # __add__(Polynomial): Polynomial
    # __mul__(Polynomial): Polynomial
    # differentiate(): Polynomial
    # integrate(): Polynomial  # (with 0 as the constant)
    # __str__: string  # in descending exponential order - clean up anything x^0 - coefficient to 2 decimal places
    # __eq__(other: Polynomial ): bool
    # __ne__(other: Polynomial ): bool

    def __init__(self, coefficient, exponent):
        self._first_node = TermNode(coefficient, exponent)

    def __add__(self, other):
        New_Poly = Polynomial(self._first_node._coefficient, self._first_node._exponent)
        current_TermNode_self = self._first_node._next
        current_TermNode_other = other._first_node

        while current_TermNode_self is not None:
            new_TermNode = TermNode(current_TermNode_self._coefficient, current_TermNode_self._exponent)
            New_Poly._DescendingExponentialorder(new_TermNode)
            current_TermNode_self = current_TermNode_self._next

        while current_TermNode_other is not None:
            new_TermNode = TermNode(current_TermNode_other._coefficient, current_TermNode_other._exponent)
            New_Poly._DescendingExponentialorder(new_TermNode)
            current_TermNode_other = current_TermNode_other._next
        return New_Poly

    def _DescendingExponentialorder(self, other_TN):
        if other_TN._exponent > self._first_node._exponent:  # performs swapping terms based on exponents
            other_TN._next = self._first_node
            self._first_node = other_TN
        elif other_TN._exponent == self._first_node._exponent: # adds coefficient if term exponents are same
            self._first_node._coefficient += other_TN._coefficient
        else:
            current_TermNode = self._first_node
            while current_TermNode._next is not None:
                if other_TN._exponent > current_TermNode._next._exponent:
                    other_TN._next = current_TermNode._next
                    current_TermNode._next = other_TN
                    break
                elif other_TN._exponent == current_TermNode._next._exponent:
                    current_TermNode._next._coefficient += other_TN._coefficient
                    break
                else:
                    current_TermNode = current_TermNode._next
            else:
                current_TermNode._next = other_TN

    def __mul__(self, other):
        current_TermNode_self = self._first_node
        New_Poly = None
        while current_TermNode_self is not None:
            current_TermNode_other = other._first_node
            while current_TermNode_other is not None:
                if New_Poly is None:
                    New_Poly = Polynomial(current_TermNode_self._coefficient * current_TermNode_other._coefficient, current_TermNode_self._exponent + current_TermNode_other._exponent)
                else:
                    new_TermNode = TermNode(current_TermNode_self._coefficient * current_TermNode_other._coefficient, current_TermNode_self._exponent + current_TermNode_other._exponent)
                    New_Poly._DescendingExponentialorder(new_TermNode)
                current_TermNode_other = current_TermNode_other._next
            current_TermNode_self = current_TermNode_self._next
        return New_Poly

    def integrate(self):
        New_Poly = Polynomial(self._first_node._coefficient/(self._first_node._exponent + 1), self._first_node._exponent+1)
        current_TermNode_self = self._first_node._next
        while current_TermNode_self is not None:
            if current_TermNode_self._exponent != -1:
                new_TermNode = TermNode(current_TermNode_self._coefficient/(current_TermNode_self._exponent + 1), current_TermNode_self._exponent+1)
                New_Poly._DescendingExponentialorder(new_TermNode)
            current_TermNode_self = current_TermNode_self._next
        return New_Poly

    def differentiate(self):
        New_Poly = Polynomial(self._first_node._coefficient * self._first_node._exponent, self._first_node._exponent - 1)
        current_TermNode_self = self._first_node._next
        while current_TermNode_self is not None:
            new_TermNode = TermNode(current_TermNode_self._coefficient * current_TermNode_self._exponent , current_TermNode_self._exponent-1)
            New_Poly._DescendingExponentialorder(new_TermNode)
            current_TermNode_self = current_TermNode_self._next
        return New_Poly

    def __str__(self):
        str_op = " "
        current_TermNode = self._first_node
        while current_TermNode is not None:
            if current_TermNode._coefficient != 0:
                str_op += "{:.2f}".format(current_TermNode._coefficient)
                # print(str_op)
                if current_TermNode._exponent != 0:
                    str_op += "x^"
                    str_op += str(current_TermNode._exponent)
                    # print(str_op)
                if current_TermNode._next is not None:
                    if current_TermNode._next._coefficient > 0:
                        str_op += " + "
                        # print(str_op)
            current_TermNode = current_TermNode._next
        return str_op

    def __eq__(self, other):
        current_TermNode_self = self._first_node
        current_TermNode_other = other._first_node
        while current_TermNode_self is not None and current_TermNode_other is not None:
            if current_TermNode_self != current_TermNode_other:
                return False
            current_TermNode_self = current_TermNode_self._next
            current_TermNode_other = current_TermNode_other._next
        return current_TermNode_self is None and current_TermNode_other is None

    def __ne__(self, other):
        return not(self == other)

poly2 = Polynomial(2, 3)  # makes the polynomial 2.00x^3
# print(poly2)
poly3 = Polynomial(3, 4)  # makes the polynomial 3.00x^4
# print(poly3)
print("Addition of polynomials", poly2, "and", poly3)
poly1 = poly2 + poly3  # makes poly1 = 3.00x^4 + 2.00x^3
print(poly1)
print("Multiplication of polynomials", poly2, "and", poly1)
poly6 = poly2 * poly1
print(poly6)
print("Multiplication of polynomials", poly1, "and", poly1)
poly7 = poly1 * poly1
print(poly7)
print("Multiplication of polynomials", poly1, "and", poly7)
poly0 = poly1 * poly7
print(poly0)
print("Integration of polynomial", poly0)
print(poly0.integrate())
print("Differentiation of polynomial", poly0)
print(poly0.differentiate())

poly_1 = Polynomial(1, 7)
poly_2 = Polynomial(2, 3)
poly_12 = poly_1 + poly_2
print("Compare:", poly_1, "equal to", poly_12)
print(poly_1 == poly_12)
print("Compare:", poly_1, "equal to", poly_1)
print(poly_1 == poly_1)
print("Compare:", poly_1, "not equal to", poly_2)
print(poly_1 != poly_2)

# prints out 3.0x^4 + 2.00x^3
# print(Polynomial.integrate(poly3))
# print(Polynomial.differentiate(poly3))
# poly3 = poly2 * poly1  # sets poly3 to 6.00x^7+4.00x^6
# poly4 = poly3.differentiate()  # sets poly4 to 42.00x^6+24.00x^5
# poly5 = poly1.integrate()  # sets poly5 to .60x^5+.50x^4