# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale  #Add a plus because it will keep overwriting wtih just an = sign
print(f"Total: ${total}")

count = 0
for sale in sales:   #add a colon at the end since it is a loop
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1
