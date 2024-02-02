principal = 0
interest = 0
term = 0

def get_payment(principal, interest, term):
    return principal * (interest / (1 - (1 + interest) ** (-term)))

print('Enter Principal: ')
principal = input()

print('Enter Interest: ')
interest = input()

print('Enter Term in Years: ')
term = input()

print(get_payment(int(principal), int(interest) / 100, int(term)))