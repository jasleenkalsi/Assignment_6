"""
Description: A class meant to manage Mortgage options.
Author: Jasleen kaur
Date: 03/31/2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION 

from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

class MortgageTests(TestCase):

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            Mortgage(-100000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 25)

    def test_invalid_rate(self):
        with self.assertRaises(ValueError):
            Mortgage(250000, "INVALID_RATE", PaymentFrequency.MONTHLY, 25)

    def test_invalid_frequency(self):
        with self.assertRaises(ValueError):
            Mortgage(250000, MortgageRate.FIXED_5, "INVALID_FREQUENCY", 25)

    def test_invalid_amortization(self):
        with self.assertRaises(ValueError):
            Mortgage(250000, MortgageRate.FIXED_5, PaymentFrequency.MONTHLY, 100)

    # The fifth test will be added once accessors for the attributes are defined.
