def analyze_purchases(purchases: list) -> dict:
    dict_result = {}

    for cust_id, category, product in purchases:
        if cust_id not in dict_result:
            dict_result[cust_id] = [{category: []}]
        if {category: []} not in dict_result[cust_id]:
            dict_result[cust_id].append({category: []})

        for item_category in dict_result[cust_id]:
            # dict_result[cust_id]
            # item_category[list(item_category.keys())[0]].append(product)
            # if list(item_category.keys())[0] == category:
            #     item_category
            print(item_category)
    print(dict_result)


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
