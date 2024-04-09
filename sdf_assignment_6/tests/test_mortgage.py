"""
Description: A class used to test the Mortgage class.
Author: Jasleen kaur
Date: 03/31/2024
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""
import unittest
from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    def test_invalid_loan_amount(self):

        #Act
        with self.assertRaises(ValueError):
            mortgage = Mortgage(0, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 25)

    def test_invalid_rate(self):
        #Act
        with self.assertRaises(ValueError):
         mortgage = Mortgage( 100000, MortgageRate, PaymentFrequency.MONTHLY, 25)


    def test_invalid_frequency(self):

        #Act
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, MortgageRate, PaymentFrequency.MONTHLY, 25)

    
    def test_invalid_amortization(self):

        #Act
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 50)
           
       #Arrange     
    def test_valid_inputs(self):
        mortgage = Mortgage(100000, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 25)
        self.assertEqual(mortgage.loan_amount, 100000)
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_1)
        self.assertEqual(mortgage.frequency, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage.amortization_period, 25)

class TestMortgageLoanAmount(TestCase):
    def test_negative_loan_amount(self):
        """Test modifying the loan amount to a negative value."""
        mortgage = Mortgage(100000, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 25)
        with self.assertRaises(ValueError):
            mortgage.loan_amount = -5000

    def test_zero_loan_amount(self):
        """Test modifying the loan amount to zero."""
        mortgage = Mortgage(100000, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 25)
        with self.assertRaises(ValueError):
            mortgage.loan_amount = 0

    def test_positive_loan_amount(self):
        """Test modifying the loan amount to a positive value."""
        mortgage = Mortgage(100000, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 25)
        mortgage.loan_amount = 150000
        self.assertEqual(mortgage.loan_amount, 150000)

class TestMortgageRate(TestCase):
    def test_valid_rate(self):
        """Test modifying the Rate to a valid MortgageRate enum value."""
        mortgage = Mortgage(100000,MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 25)
        self.assertEqual(mortgage.rate, MortgageRate.FIXED_1)

    def test_invalid_rate(self):
        """Test modifying the Rate to a value that is not a MortgageRate enum type."""
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, 'INVALID_RATE', PaymentFrequency.MONTHLY, 25)

class TestMortgageFrequency(TestCase):
    def test_valid_frequency(self):
        """Test modifying the Frequency to a valid PaymentFrequency enum value."""
        mortgage = Mortgage(100000,MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 25)
        self.assertEqual(mortgage.frequency, PaymentFrequency.MONTHLY)

    def test_invalid_frequency(self):
        """Test modifying the Frequency to a value that is not a PaymentFrequency enum type."""
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, MortgageRate.FIXED_1, 'INVALID_FREQUENCY', 25)

class TestMortgageAmortization(TestCase):
    def test_valid_amortization(self):
        """Test modifying the Amortization to a valid value."""
        mortgage = Mortgage(100000, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 25)
        self.assertEqual(mortgage.amortization_period, 25)

    def test_invalid_amortization(self):
        """Test modifying the Amortization to an invalid value."""
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 40)

class TestCalculatePayment(TestCase):

  class TestCalculatePayment(TestCase):

    def test_calculate_payment_monthly(self):
        # Test with example values
        mortgage = Mortgage(100000, MortgageRate.FIXED_5, 30, PaymentFrequency.MONTHLY)
        expected_payment = 449.66
        calculated_payment = mortgage.calculate_payment()
        self.assertAlmostEqual(calculated_payment, expected_payment, places=2)

    def test_calculate_payment_weekly(self):
        # Test with different frequency (weekly)
        mortgage = Mortgage(150000, MortgageRate.FIXED_1, 20, PaymentFrequency.WEEKLY)
        expected_payment = 220.01
        calculated_payment = mortgage.calculate_payment()
        self.assertAlmostEqual(calculated_payment, expected_payment, places=2)

    def test_calculate_payment_biweekly(self):
        # Test with different frequency (bi-weekly)
        mortgage = Mortgage(200000, MortgageRate.VARIABLE_3, 25, PaymentFrequency.BI_WEEKLY)
        expected_payment = 433.79
        calculated_payment = mortgage.calculate_payment()
        self.assertAlmostEqual(calculated_payment, expected_payment, places=2)

    def test_calculate_payment_high_interest(self):
        # Test with higher interest rate
        mortgage = Mortgage(120000, MortgageRate.FIXED_2, 15, PaymentFrequency.MONTHLY)
        expected_payment = 1158.72
        calculated_payment = mortgage.calculate_payment()
        self.assertAlmostEqual(calculated_payment, expected_payment, places=2)

    def test_calculate_payment_high_loan_amount(self):
        # Test with higher loan amount
        mortgage = Mortgage(300000, MortgageRate.FIXED_1, 30, PaymentFrequency.MONTHLY)
        expected_payment = 1349.82
        calculated_payment = mortgage.calculate_payment()
        self.assertAlmostEqual(calculated_payment, expected_payment, places=2)

class TestMortgageStringRepresentation(TestCase):
    def test_string_representation_monthly(self):
        mortgage = Mortgage(150000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 30)
        expected_string = "Principal: $150,000.00\nInterest Rate: 5.19%\nTerm: 30 years\nFrequency: MONTHLY\n"
        self.assertEqual(str(mortgage), expected_string)

    def test_string_representation_biweekly(self):
        mortgage = Mortgage(200000, MortgageRate.VARIABLE_3, PaymentFrequency.BI_WEEKLY , 25)
        expected_string = "Principal: $200,000.00\nInterest Rate: 6.69%\nTerm: 25 years\nFrequency: BI_WEEKLY\n"
        self.assertEqual(str(mortgage), expected_string)

    def test_string_representation_weekly(self):
        mortgage = Mortgage(250000, MortgageRate.FIXED_1, PaymentFrequency.WEEKLY , 20)
        expected_string = "Principal: $250,000.00\nInterest Rate: 5.99%\nTerm: 20 years\nFrequency: WEEKLY\n"
        self.assertEqual(str(mortgage), expected_string)

class TestMortgageRepr(TestCase):
    def test_repr(self):
        mortgage = Mortgage(150000.1234, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY , 30)
        expected_repr = "Mortgage(principal=150000.12, rate=0.0599, term_years=30, frequency=PaymentFrequency.MONTHLY)"
        self.assertEqual(repr(mortgage), expected_repr)

   
if __name__ == '__main__':
    unittest.main()

 

