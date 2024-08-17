def length_of_longest_substring_k_distinct(s: str, k: int) -> tuple:
    if k == 0:
        return 0, []
    left = 0
    max_length = 0
    max_substring = []
    for right in range(len(s)):
        current_set = set(s[left:right + 1])
        while len(current_set) > k:
            left += 1
            current_set = set(s[left:right + 1])
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            max_substring = [(s[left:right + 1])]
        elif current_length == max_length:
            max_substring = max_substring + [(s[left:right + 1])]
    return max_length, max_substring

# Example usage:
if __name__ == '__main__':
    print(length_of_longest_substring_k_distinct("eceba", 2))  # Output: (3, ["ece"])
    print(length_of_longest_substring_k_distinct("aa", 1))     # Output: (2, ["aa"])
    print(length_of_longest_substring_k_distinct("a", 2))      # Output: (1, ["a"])
    print(length_of_longest_substring_k_distinct("abcadcacacaca", 3))  # Output: (11, ["cadcacacaca"])
    print(length_of_longest_substring_k_distinct("aaabbbcccddd", 1))
    print(length_of_longest_substring_k_distinct("aaabbbcccddd", 0))