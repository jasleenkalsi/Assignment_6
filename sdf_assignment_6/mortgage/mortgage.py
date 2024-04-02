"""
Description: A class meant to manage Mortgage options.
Author: Jasleen kaur
Date: 03/31/2024
Usage: Create an instance of the Mortgage class to manage mortgage records and 
calculate payments.
"""
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency, VALID_AMORTIZATION

class Mortgage:
    def __init__(self, loan_amount, mortgage_rate, payment_frequency, amortization_period):
        self.__loan_amount = None
        self.__rate = None
        self.__frequency = None
        self.__amortization_period = None
        
        self.loan_amount = loan_amount
        self.rate = mortgage_rate
        self.frequency = payment_frequency
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
        if value in MortgageRate:
            self.__rate = value
        else:
            raise ValueError("Rate provided is invalid.")

    @property
    def frequency(self):
        """Accessor for the frequency."""
        return self.__frequency

    @frequency.setter
    def frequency(self, value):
        """Mutator for the frequency."""
        if value in PaymentFrequency:
            self.__frequency = value
        else:
            raise ValueError("Frequency provided is invalid.")

    @property
    def amortization_period(self):
        """Accessor for the amortization period."""
        return self.__amortization_period

    @amortization_period.setter
    def amortization_period(self, value):
        """Mutator for the amortization period."""
        if value in VALID_AMORTIZATION:
            self.__amortization_period = value
        else:
            raise ValueError("Amortization provided is invalid.")

    def calculate_payment(self) -> float:
        """Calculate the mortgage payment amount."""
        if self.frequency == PaymentFrequency.MONTHLY:
            n = self.amortization_period * 12
            r = self.rate / 12
        elif self.frequency == PaymentFrequency.BI_WEEKLY:
            n = self.amortization_period * 26
            r = self.rate / 26
        elif self.frequency == PaymentFrequency.WEEKLY:
            n = self.amortization_period * 52
            r = self.rate / 52
        else:
            raise ValueError("Invalid payment frequency.")

        # Calculate mortgage payment using the formula
        mortgage_payment = (self.loan_amount * r) / (1 - ((1 + r) ** -n))

        return mortgage_payment

    def __str__(self) -> str:
        """Return string representation of Mortgage object."""
        return f"Mortgage Amount: ${self.loan_amount:.2f} Rate: {self.rate * 100:.2f}% Amortization: {self.amortization_period}"

    def __repr__(self) -> str:
        """Return raw string representation of Mortgage object."""
        return f"Mortgage({self.loan_amount}, {self.rate}, {self.frequency}, {self.amortization_period})"
