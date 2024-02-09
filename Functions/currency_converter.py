#usd to pkr conversion


def currency_converter(usd):
    pkr = usd * 279.08
    return pkr


usd = float(input("Enter amount in USD: "))
print("Amount in PKR: ", currency_converter(usd))
