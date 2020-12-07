#storing balance to be able to reset at the end of each iteration
balanceMin = balance

#defining monthly interest rate as 1/12 of annual interest rate
monthlyInterestRate = annualInterestRate / 12.0

#setting first patment to 0% interest rate for first check
payment = balance/12.0

#epsilon defined to control when the answer is close enough and degree of accuracy
epsilon = 0.01

#bounds for guess range and initial parameters after first guess with 0% intrest rate
lower = balance/12.0
upper = (balance*(1 + annualInterestRate)**12)/12.0

#loop to continously run until minimum payment is found
while True:

    #iterates through with current payment to calculate balanceMin at end of 12 months
    for month in range(0, 12):
        balanceMin -= payment
        balanceMin += monthlyInterestRate * balanceMin

    #case if balanceMin at the end of 12 months is less than our tolerance
    #breaks loop if within tolerance
    if abs(balanceMin) < epsilon:
        print("Lowest Payment: ", round(payment, 2))
        break

    #case if balanceMin at the end of 12 months is not less than our tolerance
    else:
        #adjusts payment guess depending on if balanceMin is high or low
        if balanceMin < 0:
            upper = payment
        else:
            lower = payment

        #adjusts payment guess
        payment = (lower + upper) / 2

        #resets to initial balance
        balanceMin = balance
