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
        with self.assertRaises(ValueError):
            mortgage = Mortgage(0, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 25)

    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
         mortgage = Mortgage(100000, MortgageRate, PaymentFrequency.MONTHLY, 25)

    def test_invalid_frequency(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, MortgageRate, PaymentFrequency.MONTHLY, 25)
    
    def test_invalid_amortization(self):
        with self.assertRaises(ValueError):
            mortgage = Mortgage(100000, MortgageRate.FIXED_1, PaymentFrequency.MONTHLY, 50)
            
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

if __name__ == '__main__':
    unittest.main()
