def analyze_purchases(purchases: list) -> dict:
    dict_purchases = {}
    for cust_id, category, product in purchases:
        if cust_id not in dict_purchases:
            dict_purchases[cust_id] = dict([])
        if category not in dict_purchases[cust_id]:
            dict_purchases[cust_id][category] = []
        dict_purchases[cust_id][category].append(product)
    # print(dict_purchases)

    dict_analyze = {}
    all_buy_product = []
    for cust_id, values in dict_purchases.items():
        # print(cust_id, values)
        # print(list(values.keys())[0])     # get category
        # print(len(list(values.keys())))   # get len of category
        high_frequen = 0
        set_products_frequen = set([])
        for category in list(values.keys()):
            # print(category)     # get category
            # print(dict_purchases[ust_id][category])     # get list products
            for product in dict_purchases[cust_id][category]:
                # print(cust_id, category, product)
                all_buy_product.append((category, product))
                if dict_purchases[cust_id][category].count(product) > high_frequen:
                    high_frequen = dict_purchases[cust_id][category].count(
                        product)
                    set_products_frequen = set(
                        [(category, product, high_frequen)])
                elif dict_purchases[cust_id][category].count(product) == high_frequen:
                    set_products_frequen.add((category, product, high_frequen))
        if len(set_products_frequen) == 1:
            dict_analyze[cust_id] = {list(set_products_frequen)[0][0]: list(set_products_frequen)[0][2]}
        else:
            dict_analyze[cust_id] = {}
        # print(category_product_high_frequency, high_frequen)
        # print(set_products_frequen)
        # print(len(set_products_frequen))

    dict_all_buy_product = {}
    for category, product in all_buy_product:
        if category not in dict_all_buy_product:
            dict_all_buy_product[category] = {}
        if product not in dict_all_buy_product[category]:
            dict_all_buy_product[category][product] = 1
        else:
            dict_all_buy_product[category][product] += 1
    # print(all_buy_product)
    # print(dict_all_buy_product)

    dict_most_frequency = {}
    for category, values in dict_all_buy_product.items():
        # print(category, values)
        frequency_rate = max([rate for rate in values.values()])
        # print(frequency_rate)
        for product, frequency in values.items():
            if frequency == frequency_rate:
                dict_most_frequency.update({category: product})
    # print(list_most_frequency)

    dict_analyze["most_frequent"] = dict_most_frequency
    # print(dict_analyze)
    return dict_analyze


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
    print(analyze_purchases(purchases))
