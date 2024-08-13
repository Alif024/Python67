def length_of_longest_substring_k_distinct(s: str, k: int):
    if k == 0:
        return 0
    list_all_answer = []
    for i in range(len(s)):
        list_answer = []
        scenario_answer = ""
        for char in s[i:]:
            scenario_answer += char
            set_answer = set(list(scenario_answer))
            if len(set_answer) <= k:
                list_answer.append(scenario_answer)
            # print(set_answer)
        # print(list_answer)
        list_all_answer.append(list_answer[-1])
    # print(list_all_answer)
    highest_len = 0
    for answer in list_all_answer:
        if len(answer) >= highest_len:
            highest_len = len(answer)
    # print(highest_len)
    result = []
    for answer in list_all_answer:
        if len(answer) == highest_len:
            result.append(answer)
    # print(result)
    return (highest_len, result)

s = "eceba"
k = 2
print(length_of_longest_substring_k_distinct(s, k))

s = "aa"
k = 1
print(length_of_longest_substring_k_distinct(s, k))

s = "a"
k = 2
print(length_of_longest_substring_k_distinct(s, k))

s = "abcdcacacacaca"
k = 3
print(length_of_longest_substring_k_distinct(s, k))