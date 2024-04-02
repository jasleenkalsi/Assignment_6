"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: Jasleen Kaur
Date: 01 April 2024
"""
import os
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, PaymentFrequency

### REQUIREMENT 1: Open and read the pixell_river_mortgages.txt file
file_path = os.path.join("data", "pixell_river_mortgages.txt")
with open(file_path, "r") as file:
    lines = file.readlines()

# Iterate through each line in the file
for line in lines:
    # Split the line by commas to get individual values
    values = line.strip().split(",")

    # Extract values from the list
    loan_amount = float(values[0])
    rate_value = values[1]
    frequency_value = values[2]
    amortization_period = int(values[3])

    # Create a Mortgage instance with the extracted values
    try:
        mortgage = Mortgage(loan_amount, MortgageRate[rate_value], PaymentFrequency[frequency_value], amortization_period)
        # Print the string representation of the mortgage instance
        print(str(mortgage))
        # Calculate and print the mortgage payment
        print("Calculated Payment: ${:.2f}".format(mortgage.calculate_payment()))
    except ValueError as e:
        # If ValueError is raised, print the error message
        print(e)

### REQUIREMENT
### ADD IMPORT STATEMENT FOR THE MORTGAGE CLASS



### REQUIREMENT
### ENCLOSE THE FOLLOWING 'WITH OPEN' BLOCK IN A 'TRY-EXCEPT' BLOCK WHICH 
### WILL CATCH A 'FILENOTFOUNDERROR' EXCEPTION
with open ("data\\pixell_river_mortgages.txt","r") as input:
    print("**************************************************")
    
    for data in input:
        items = data.split(",")
        
        try:
            amount = float(items[0])
            rate = items[1]
            amortization = int(items[2])
            frequency = items[3]

            ### REQUIREMENT:
            ### INSTANTIATE A MORTGAGE OBJECT USING THE VALUES
            ### FOR AMOUNT, RATE, FREQUENCY AND AMORTIZATION ABOVE.

            
            ### REQUIREMENT:
            ### PRINT THE MORTGAGE OBJECT

        except ValueError as e:
            # This except block will catch Explicit exceptions: 
            # Those raised by the programmer in the Mortgage class.
            print(f"Data: {data.strip()} caused Exception: {e}")
        
        except Exception as e:
            # This except block will catch Implicit exceptions:  
            # Those raised through normal execution.
            print(f"Data: {data.strip()} caused Exception: {e}")
        finally:
            print("**************************************************")
