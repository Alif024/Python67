def analyze_purchases(purchases: list) -> dict:
    dict_purchases = {}
    for cust_id, category, product in purchases:
        if cust_id not in dict_purchases:
            dict_purchases[cust_id] = dict([])
        if category not in dict_purchases[cust_id]:
            dict_purchases[cust_id][category] = []
        dict_purchases[cust_id][category].append(product)
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
