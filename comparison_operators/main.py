### comparison examples

# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

equalvals = 1 == 1
print(equalvals)

notequalvals = 1 != 5
print(notequalvals)

greaterthan = 1 > 5
print(greaterthan)

lessthan = 1 < 34
print(lessthan)

equalorlessthan = 1 <= 5
print(equalorlessthan)

lessthanorequal = 12 >= 5
print(lessthanorequal)

#### chaining comparisons
# and or not keywords examples

andexample = 1 < 5 and 5 < 10
print(andexample)

# easier way
first_val = 1 < 5
second_val = 5 < 10
andexample = first_val and second_val

first_val = 1 < 5
second_val = 5 < 10
andexample = first_val or second_val

orexample = 1 < 5 or 5 < 10
print(orexample)

# another way 
first_val = 1 < 5
second_val = 5 < 10
orexample = first_val or second_val

notexample = not 1 < 5
print(notexample)


#inverse using not keyword
first_val = 4
second_val = 10

#   !(first_val < second_val)
# prety much it negates the value
answer = not first_val < second_val
print(answer)