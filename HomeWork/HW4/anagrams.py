def group_anagrams(words: list) -> list: 
    group_list = []
    for word in words:
        if set(list(word)) not in group_list:
            group_list.append(set(list(word)))

    result = []
    for group in group_list:
        temp = []
        for word in words:
            if set(list(word)) == group:
                temp.append(word)
        result.append(temp)
    return result

if __name__ == '__main__':
    # ตัวอย่างที่ 1 
    words = ["eat", "tea", "tan", "ate", "nat", "bat"] 
    print(group_anagrams(words)) 
    # เอาต์พุต: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] 

    # ตัวอย่างที่ 2 
    words = ["listen", "silent", "enlist", "hello", "world"] 
    print(group_anagrams(words)) 
    # เอาต์พุต: [["listen", "silent", "enlist"], ["hello"], ["world"]] 