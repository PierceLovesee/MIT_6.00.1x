# iterative loop to calculate the balance after each month for a year
for month in range(0, 12):

    # recaclulating the balance at the end of each month after
    # the min payment has been made
    balance = balance - balance * monthlyPaymentRate

    # calculating interest at the end of each month and adding to balance
    balance = balance + ((annualInterestRate / 12) * balance)

    # increment month count and continue looping
    month += 1

# displaying the balance at the end of month 12 to the user,
# rounded to 2 decimal places
print("Remaining balance: " + str(round(balance, 2)))
