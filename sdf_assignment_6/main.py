"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: Jasleen Kaur
Date: 01 April 2024
"""
### REQUIREMENT 1: Incorporate Batch Processing Files
# Import necessary modules and classes
import os
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

# Define the file path
file_path = os.path.join("data", "pixell_river_mortgages.txt")

# Open and read the pixell_river_mortgages.txt file
with open(file_path, "r") as file:
    lines = file.readlines()

# Iterate through each line in the file
for line in lines:
    # Split the line by commas to get individual values
    values = line.strip().split(",")
    
    # Debug print statement to check values
    print("Values:", values)

    try:
        # Extract values from the list
        loan_amount = float(values[0])
        rate_value = values[1]
        frequency_value = values[2]
        amortization_period = int(values[3])  # Convert amortization period to integer

        # Create a Mortgage instance with the extracted values
        mortgage = Mortgage(loan_amount, MortgageRate[rate_value], PaymentFrequency[frequency_value], amortization_period)
        # Print the string representation of the mortgage instance
        print(str(mortgage))
        # Calculate and print the mortgage payment
        print("Calculated Payment: ${:.2f}".format(mortgage.calculate_payment()))
    except ValueError as e:
        # If ValueError is raised, print the error message and continue to the next line
        print("Error processing line:", e)
        continue



