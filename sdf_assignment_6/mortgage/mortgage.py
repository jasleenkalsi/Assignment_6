"""
Description: A class meant to manage Mortgage options.
Author: Jasleen kaur
Date: 03/31/2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION


class Mortgage:
    def __init__(self, loan_amount, string_rate_value, string_frequency_value, amortization):
        # Validate Loan Amount
        if loan_amount <= 0:
            raise ValueError("Loan Amount must be positive.")
        self.__loan_amount = loan_amount

        # Validate Rate
        try:
            self.__rate = MortgageRate[string_rate_value]
        except KeyError:
            raise ValueError("Rate provided is invalid.")

        # Validate Frequency
        try:
            self.__frequency = PaymentFrequency[string_frequency_value]
        except KeyError:
            raise ValueError("Frequency provided is invalid.")

        # Validate Amortization
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid.")
        self.__amortization = amortization

class Mortgage:
    def __init__(self, loan_amount, mortgage_rate, payment_frequency, amortization_period):
        self.__loan_amount = None
        self.loan_amount = loan_amount  # Call the setter to evaluate and set the loan amount
        self.mortgage_rate = mortgage_rate
        self.payment_frequency = payment_frequency
        self.amortization_period = amortization_period

    @property
    def loan_amount(self):
        """Accessor for the loan amount."""
        return self.__loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        """Mutator for the loan amount."""
        if value > 0:
            self.__loan_amount = value
        else:
            raise ValueError("Loan Amount must be positive.")

    @property
    def rate(self):
        """Accessor for the rate."""
        return self.__rate

    @rate.setter
    def rate(self, value):
        """Mutator for the rate."""
        try:
            self.__rate = MortgageRate[value]
        except KeyError:
            raise ValueError("Rate provided is invalid.")