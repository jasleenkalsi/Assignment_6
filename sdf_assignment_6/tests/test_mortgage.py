"""
Description: A class used to test the Mortgage class.
Author: Jasleen kaur
Date: 03/31/2024
Usage: Use the tests encapsulated within this class to test the MortgagePayment class.
"""

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):
    def test_invalid_loan_amount(self):
        with self.assertRaises(ValueError):
            Mortgage(0, 'FIXED', 'MONTHLY', 25)
    
    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 'INVALID_RATE', 'MONTHLY', 25)
    
    def test_invalid_frequency(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 'FIXED', 'INVALID_FREQUENCY', 25)
    
    def test_invalid_amortization(self):
        with self.assertRaises(ValueError):
            Mortgage(100000, 'FIXED', 'MONTHLY', 50)
            
    def test_valid_inputs(self):
        mortgage = Mortgage(100000, 'FIXED', 'MONTHLY', 25)
        self.assertEqual(mortgage._Mortgage__loan_amount, 100000)
        self.assertEqual(mortgage._Mortgage__rate, MortgageRate.FIXED)
        self.assertEqual(mortgage._Mortgage__frequency, PaymentFrequency.MONTHLY)
        self.assertEqual(mortgage._Mortgage__amortization, 25)


    # The fifth test will be added once accessors for the attributes are defined.
