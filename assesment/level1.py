inflation_rates = [5.4, 2.4, 3, 1.5, 6.2]

def check_economy(rates):
    total = 0
    for rate in rates:
        total += rate

    avg = total / len(rates)
    print("Total: ", total)
    print("Avg: ", avg)

    if (avg > 5):
        print("High Inflation")
    else:
        print("Stable")


check_economy(inflation_rates)
