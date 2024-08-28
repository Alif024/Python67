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

def analyze_purchases(purchases: list) -> dict:
    dict_purchases = {}
    all_buy_product = []
    for cust, category, item in purchases:
        if cust not in dict_purchases:
            dict_purchases[cust] = {}
        if category not in dict_purchases[cust]:
            dict_purchases[cust][category] = {}
        if item not in dict_purchases[cust][category]:
            dict_purchases[cust][category][item] = 1
        else:
            dict_purchases[cust][category][item] += 1
        all_buy_product.append((category, item))
    top_custs_category = {}
    for cust in dict_purchases:
        top_cat_cust = {}
        for category in dict_purchases[cust]:
            cat_count_list = []
            for item in dict_purchases[cust][category]:
                cat_count_list.append(dict_purchases[cust][category][item])
            max_cat = max(cat_count_list)
            list_top_cat_cust = []
            for item in dict_purchases[cust][category]:
                if dict_purchases[cust][category][item] == max_cat:
                    list_top_cat_cust.append(item)
            if len(list_top_cat_cust) == 1:
                top_cat_cust[category] = max_cat
            else:
                top_cat_cust[category] = {}
        if len(top_cat_cust) == 1:
            top_custs_category[cust] = top_cat_cust
        else:
            top_custs_category[cust] = {}
    dict_all_buy_product = {}
    for category, product in all_buy_product:
        if category not in dict_all_buy_product:
            dict_all_buy_product[category] = {}
        if product not in dict_all_buy_product[category]:
            dict_all_buy_product[category][product] = 1
        else:
            dict_all_buy_product[category][product] += 1
    dict_most_frequency = {}
    for category, values in dict_all_buy_product.items():
        frequency_rate = max([rate for rate in values.values()])
        for product, frequency in values.items():
            if frequency == frequency_rate:
                dict_most_frequency.update({category: product})
    top_custs_category["most_frequent"] = dict_most_frequency
    return top_custs_category


if __name__ == "__main__":
    print(analyze_purchases(purchases))
