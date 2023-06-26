def calculate_bill(units):
    rate_slabs = [(50, 0.50), (100, 0.75), (200, 1.20), (300, 1.50)]
    additional_rate = 2.00

    bill = 0.0
    remaining_units = units

    for slab_units, slab_rate in rate_slabs:
        if remaining_units <= 0:
            break
        elif remaining_units <= slab_units:
            bill += remaining_units * slab_rate
        else:
            bill += slab_units * slab_rate
            remaining_units -= slab_units

    if remaining_units > 0:
        bill += remaining_units * additional_rate

    return bill

# Example usage
units = float(input("Enter the number of units consumed: "))

bill_amount = calculate_bill(units)
print("Electricity Bill Amount: $", bill_amount)
