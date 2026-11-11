def net_to_gross(price : float) -> float:
    return price * 1.19, price * 0.19

print(net_to_gross(100))
gross, tax = net_to_gross(100)
print(tax)