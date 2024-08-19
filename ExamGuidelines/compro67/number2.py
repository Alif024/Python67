def find_repeated_substrings(s: str) -> list:
    possibility_message = dict()
    for left in range(len(s)):
        for right in range(left, len(s)):
            # print(left, right, s[left : right + 1])
            if s[left : right + 1] not in possibility_message:
                possibility_message[s[left : right + 1]] = 1
            else:
                possibility_message[s[left : right + 1]] += 1
            # print(possibility_message)
    list_result = [
        str_result
        for str_result, count in possibility_message.items()
        if count >= 2 and len(str_result) >= 2
    ]
    # print(possibility_message)
    return list_result


if __name__ == "__main__":
    print(find_repeated_substrings("banana"))
    print(find_repeated_substrings("abcdefg"))
    print(find_repeated_substrings("abcabcabc"))
    print(find_repeated_substrings("aaaa"))
