# TODO-1: Ask the user for input
more_bidders = True
auction = {}
while more_bidders:
    name= input("What is your name?: ")
    bid_amount = input("What is your bid?: $")
    # TODO-2: Save data into dictionary {name: price}
    auction[name] = bid_amount


# TODO-3: Whether if new bids need to be added
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bidders == "no":
        more_bidders = False
    else:
        print(f" \n" * 20)
# TODO-4: Compare bids in dictionary
biggest = 0
peepy = ""
for person in auction:
    values = int(auction[person])
    if values > biggest:
        biggest = values
        peepy = person
print(f"The winner is {peepy} with ${biggest}")



