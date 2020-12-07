# initializing the minimum payment to $0 incase balance of $0 is given
payment = 0

# initialize stoarage balance variable inorder to not overwrite origonal balance
balanceMin = balance

# continuos loop while the balance is greater than $0 after 12 months
while balanceMin > 0:

    # incriment $10 to the minimum payment each attempt, starting with $10
    payment += 10

    #resetting the working balance to the origonal balance each attempt
    balanceMin = balance

    # loop to determine what the balance is at the end of month 12 for each attempt
    for month in range(0, 12):
        balanceMin = balanceMin - payment
        balanceMin = balanceMin + ((annualInterestRate / 12) * balanceMin)
        month += 1

# print the lowest possible $10 incinment payment to the user
print("Lowest Payment: " + str(payment))
