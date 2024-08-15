def length_of_longest_substring_k_distinct(s: str, k: int) -> tuple:
    # Your implementation here
    if k == 0:
        return (0, [])
    all_possibility_results = []
    for start_char in range(len(s)):
        string_for_check_results_this_senerio = ""
        the_possibility_results_this_senerio = []
        for char in s[start_char:]:
            string_for_check_results_this_senerio += char
            if len(set(list(string_for_check_results_this_senerio))) <= k:
                the_possibility_results_this_senerio.append(string_for_check_results_this_senerio)
        all_possibility_results.append(the_possibility_results_this_senerio[-1])
    ordered_pairs_length_and_result = {}
    for result in all_possibility_results:
        ordered_pairs_length_and_result.update({result: len(result)})
    if list(ordered_pairs_length_and_result.values()) == []:
        highest_len = 0
    else:
        highest_len = max(list(ordered_pairs_length_and_result.values()))
    final_list_result = [result for result, len in ordered_pairs_length_and_result.items() if len == highest_len]
    return (highest_len, final_list_result)


s = "eceba"
k = 2
print(length_of_longest_substring_k_distinct(s, k))

s = "aabbcc"
k = 1
print(length_of_longest_substring_k_distinct(s, k))

s = "a"
k = 2
print(length_of_longest_substring_k_distinct(s, k))

s = "abcdcacacacaca"
k = 3
print(length_of_longest_substring_k_distinct(s, k))