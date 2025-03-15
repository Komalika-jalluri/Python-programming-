no_of_days= int(input())
years=no_of_days//365
remaining_days=no_of_days%365
weeks=remaining_days//7
remaining_days=remaining_days%7
print("years:",years)
print("weeks:",weeks)
print("days:",remaining_days)
