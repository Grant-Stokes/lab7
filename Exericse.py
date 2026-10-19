# Exercise 1
#Defining a function
def calculate_tax(price,rate):
    return price * rate

#calling a function

tax1=calculate_tax(100,0.07)
tax2=calculate_tax(250,0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")    

#Exercise 2
#Defining a function with an if statement
def apply_a_discount(price,tier):
    if tier == 'gold':
        return price *0.85
    elif tier == 'silver':
        return price *0.90
    elif tier == 'bronze':
        return price *0.95
    else:
        return price

#calling the function with different tiers
original_price=200

for tier in ['gold','silver','bronze','none']:
    print(f'{tier}:  ${apply_a_discount(original_price,tier):.2f}')

#Exercise 3
#combining functions
def final_price(price,tier,tax_rate):
    discounted_price = apply_a_discount(price,tier)
    tax = calculate_tax(discounted_price,tax_rate)
    return discounted_price + tax
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

#Exercise 4
#Defining a function with a loop
orders = [(200,'gold'),(150,'silver'),(80,'bronze'),(500,'none')]

rate=0.07
for price,tier in orders:
    total = final_price(price,tier,rate)
    print(f'Order: ${price} | Tier: {tier} | Final Price: ${total:.2f}')


#Exercise 6
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here?
print(double_it()) # what prints here?
print(x)           # has x changed?

