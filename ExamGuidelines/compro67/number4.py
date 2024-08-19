def analyze_purchases(purchases: list) -> dict:
    dict_purchases = {}
    for data in purchases:
        if data[0] not in dict_purchases:
            dict_purchases[data[0]] = dict([])
        if data[1] not in dict_purchases[data[0]]:
            dict_purchases[data[0]][data[1]] = []
        dict_purchases[data[0]][data[1]].append(data[2])
        # print(dict_purchases)

    print(dict_purchases)


purchases = [
    ("cust1", "electronics", "laptop"),
    ("cust2", "groceries", "apple"),
    ("cust1", "electronics", "laptop"),
    ("cust1", "electronics", "mouse"),
    ("cust2", "groceries", "apple"),
    ("cust2", "groceries", "banana"),
    ("cust3", "groceries", "banana"),
    ("cust3", "groceries", "apple"),
    ("cust3", "electronics", "camera"),
]

if __name__ == "__main__":
    # print(analyze_purchases(purchases))
    analyze_purchases(purchases)
