"""
age = 16 
account= 0 
if age >= 16: 
    print("Welcome to bank") 
    account += 10 

print(account)
"""

RED_ALERT= True 

income= 20000 

age= 26 

depositPercentage= 0.8 

 

offerLoan = ((not RED_ALERT) and (depositPercentage >=0.6) and (age >=22) and (income >18000) or (income/5000>=age)) 

print("Offer loan "+str(offerLoan))