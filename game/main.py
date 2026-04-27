from data import ships, CURRENCY, regions, ZJ_PER_AU

# Player data
player_wallet = 5000
player_ship = "Ymir"
current_region = "Nyx"
current_fuel = 2000
cargo = []

print("Welcome to Sellestial")
print("---------------------")

while True:
    command = input("\nEnter command: ")

    if command == "exit":
        print("\nGoodbye.")
        break

    elif command == "list commands":
        print("\nAvailable Commands:")
        print("-------------------")
        print("list commands : show all commands")
        print("wallet : view your balance")
        print("inv : view ship, fuel, and cargo")
        print("ship wares : view ships for sale")
        print("item wares : view items in a region")
        print("buy fuel : purchase fuel for your ship")
        print("buy (item) : buy an item from current region")
        print("sell (item) : sell an item from cargo")
        print("travel to (region) : travel to another region")
        print("exit : quit the game")

    elif command == "wallet":
        print("\nWallet:", player_wallet, CURRENCY)

    elif command == "inv":
        ship = ships[player_ship]
        cargo_capacity = ship["cargo_capacity"]
        max_fuel = ship["max_fuel"]
        free_cargo_space = cargo_capacity - len(cargo)

        print("\nInventory")
        print("---------")
        print("Ship:", player_ship)
        print("Current Region:", current_region)
        print("Fuel:", current_fuel, "/", max_fuel)
        print("Cargo:", cargo)
        print("Free Cargo Space:", free_cargo_space)

    elif command == "ship wares":
        print("\nShips for Sale:\n")

        for ship_name in ships:
            ship = ships[ship_name]

            print(ship_name)
            print("  Price:", ship["price"], CURRENCY)
            print("  Cargo Capacity:", ship["cargo_capacity"])
            print("  Max Fuel:", ship["max_fuel"])
            print("  Description:", ship["description"])
            print()

    elif command.startswith("travel to "):
        destination = command.replace("travel to ", "")

        if destination not in regions:
            print("\nInvalid region.")
        elif destination not in regions[current_region]["routes"]:
            print("\nNo route to that region.")
        else:
            distance = regions[current_region]["routes"][destination]
            fuel_cost = distance * ZJ_PER_AU

            if current_fuel >= fuel_cost:
                current_fuel -= fuel_cost
                current_region = destination

                print("\nTravel successful!")
                print("Current Region:", current_region)
                print("Fuel Remaining:", current_fuel)
            else:
                print("\nNot enough fuel to travel.")

    elif command == "buy fuel":
        ship = ships[player_ship]
        max_fuel = ship["max_fuel"]
        fuel_price = regions[current_region]["fuel_price"]

        print("\nFuel Price:", fuel_price, CURRENCY, "per unit")

        amount = int(input("How much fuel do you want to buy? "))

        total_cost = amount * fuel_price

        if current_fuel + amount > max_fuel:
            print("\nCannot exceed max fuel capacity.")
        elif player_wallet < total_cost:
            print("\nNot enough money.")
        else:
            current_fuel += amount
            player_wallet -= total_cost

            print("\nFuel purchased!")
            print("Current Fuel:", current_fuel, "/", max_fuel)
            print("Wallet:", player_wallet, CURRENCY)

    elif command.startswith("buy "):
        item_name = command.replace("buy ", "")

        ship = ships[player_ship]
        cargo_capacity = ship["cargo_capacity"]

        if item_name not in regions[current_region]["prices"]:
            print("\nThat item is not sold in this region.")
        elif len(cargo) >= cargo_capacity:
            print("\nYour cargo hold is full.")
        else:
            price = regions[current_region]["prices"][item_name]

            if player_wallet >= price:
                player_wallet -= price
                cargo.append(item_name)

                print("\nPurchase successful!")
                print("Bought:", item_name)
                print("Wallet:", player_wallet, CURRENCY)
                print("Cargo:", cargo)
                print("Free Cargo Space:", cargo_capacity - len(cargo))
            else:
                print("\nYou do not have enough money.")

    elif command.startswith("sell "):
        item_name = command.replace("sell ", "")

        ship = ships[player_ship]
        cargo_capacity = ship["cargo_capacity"]

        if item_name not in cargo:
            print("\nYou do not have that item in your cargo.")
        elif item_name not in regions[current_region]["prices"]:
            print("\nThis region is not buying that item.")
        else:
            price = regions[current_region]["prices"][item_name]

            player_wallet += price
            cargo.remove(item_name)

            print("\nSale successful!")
            print("Sold:", item_name)
            print("Wallet:", player_wallet, CURRENCY)
            print("Cargo:", cargo)
            print("Free Cargo Space:", cargo_capacity - len(cargo))

    else:
        print("\nUnknown command.")