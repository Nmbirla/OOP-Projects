from unittest import TestCase
from Polynomial import Polynomial


class TestPolynomial(TestCase):
    def test_addition(self):
        print('Unit tests for __add__:')
        # Arrange
        Poly0 = Polynomial(-2, -3)
        Poly1 = Polynomial(5, 4)
        Expected_Addition_Poly_0_1 = Polynomial(-2, -3) + Polynomial(5, 4)
        Expected_Addition_Poly_0_0 = Polynomial(-4, -3)
        # Act
        Actual_Addition_Poly_0_1 = Polynomial.__add__(Poly0, Poly1)
        Actual_Addition_Poly_0_0 = Polynomial.__add__(Poly0, Poly0)
        # Assert
        self.assertEqual(Expected_Addition_Poly_0_1, Actual_Addition_Poly_0_1)
        self.assertEqual(Expected_Addition_Poly_0_0, Actual_Addition_Poly_0_0)

    def test_multiplication(self):
        print('Unit tests for __mul__:')
        # Arrange
        Poly3 = Polynomial(2, 3) + Polynomial(6, 7)
        Poly4 = Polynomial(5, 4) + Polynomial (2, 3)
        Poly5 = Polynomial(-2, -3)
        Expected_Multiplication_Poly_3_4 = Polynomial(30, 11) + Polynomial(12, 10) + Polynomial(10, 7) + Polynomial(4, 6)
        Expected_Multiplication_Poly_3_3 = Polynomial(36, 14) + Polynomial(24, 10) + Polynomial(4, 6)
        Expected_Multiplication_Poly_5_5 = Polynomial(4, -6)
        # Act
        Actual_Multiplication_Poly_3_4 = Polynomial.__mul__(Poly3, Poly4)
        Actual_Multiplication_Poly_3_3 = Polynomial.__mul__(Poly3, Poly3)
        Actual_Multiplication_Poly_5_5 = Polynomial.__mul__(Poly5, Poly5)
        # Assert
        self.assertEqual(Expected_Multiplication_Poly_3_4, Actual_Multiplication_Poly_3_4)
        self.assertEqual(Expected_Multiplication_Poly_3_3, Actual_Multiplication_Poly_3_3)
        self.assertEqual(Expected_Multiplication_Poly_5_5, Actual_Multiplication_Poly_5_5)


    def test_integrate(self):
        print('Unit tests for integrate():')
        # Arrange

        Poly0 = Polynomial(2, -3)
        Poly1 = Polynomial.__add__(Polynomial(1, 1), Polynomial(8, 3))

        Expected_Integration_Poly0 = Polynomial(-1, -2)
        Expected_Integration_Poly1 = Polynomial(0.50, 2) + Polynomial(2, 4)

        # Act
        Actual_Integration_Poly0 = Polynomial.integrate(Poly0)
        Actual_Integration_Poly1 = Polynomial.integrate(Poly1)

        # Assert
        self.assertEqual(Expected_Integration_Poly0, Actual_Integration_Poly0)
        self.assertEqual(Expected_Integration_Poly1, Actual_Integration_Poly1)

    def test_differentiate(self):
        print('Unit tests for differentiate():')
        # Arrange
        Poly_d0 = Polynomial(-2, -3)
        Poly_d1 = Polynomial.__add__(Polynomial(1, 1), Polynomial(8, 3))

        Expected_Differentiation_Poly_d0 = Polynomial(6, -4)
        Expected_Differentiation_Poly_d1 = Polynomial(24, 2) + Polynomial(1, 0)

        # Act
        Actual_Differentiation_Poly_d0 = Polynomial.differentiate(Poly_d0)
        Actual_Differentiation_Poly_d1 = Polynomial.differentiate(Poly_d1)

        # Assert
        self.assertEqual(Expected_Differentiation_Poly_d0, Actual_Differentiation_Poly_d0)
        self.assertEqual(Expected_Differentiation_Poly_d1, Actual_Differentiation_Poly_d1)

    def test_equal(self):
        print('Unit tests for __eq__ and __ne__:')
        # Arrange
        Poly_Eq0 = Polynomial(1, 2)
        Poly_Eq1 = Polynomial(1, 2) + Polynomial(2, 3)
        # Act
        #Assert
        self.assertTrue(Poly_Eq0 != Poly_Eq1)

        # Arrange
        Poly_Eq5 = Polynomial(-1, -2)
        Poly_Eq2 = Polynomial(-1, -2)
        # Act
        # Assert
        self.assertTrue(Poly_Eq5 == Poly_Eq2)

        # Arrange
        Poly_Eq0 = Polynomial(4, 5)
        Poly_Eq1 = Polynomial(1, 2)
        # Act

        # Assert
        self.assertTrue(Poly_Eq0 != Poly_Eq1)

        # Arrange
        Poly_Eq3 = Polynomial(-1, -2)
        Poly_Eq4 = Polynomial(1, 2)
        # Act
        # Assert
        self.assertTrue(Poly_Eq3 != Poly_Eq4)



