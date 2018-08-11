#:Create a new dictionary called prices using {} format like the example above.")
# Put these values in your prices dictionary, in between the {}:

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Create a stock dictionary with the values below.
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

print("""
A: for each key, print out the key along with its price and stock information. Print the answer in the following format:
# apple
# price: 2
# stock: 0
""")
print()
for key in prices:
    print()
    print(key)
    print(" price : {0} ".format(prices[key]))
    print(" stock : {0} ".format(stock[key]))
print()
print("* "*50)
print("B: Let's determine how much money you would make if you sold all of your food.")

total = 0
for key in prices:
    print()
    print(key)
    print(prices[key] * stock[key])
    total += prices[key] * stock[key]
print()
print("Tổng số: " , total)