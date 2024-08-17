def length_of_longest_substring_k_distinct(s: str, k: int) -> tuple:
    if k == 0:
        return 0, []

    char_map = {}
    left = 0        # (0, 0,  0, 1)
    max_len = 0     # (1, 2,  3)
    substrings = [] # (a,ab,abc,bcd)
                    # [abc,bcd]

              # (0,1,2,...,13)
    for right in range(len(s)):                        
        char = s[right]                                 
        if char in char_map:
            char_map[char] += 1                                                
        else:
            char_map[char] = 1                          

        while len(char_map) > k:                        
            left_char = s[left]                                                                             
            char_map[left_char] -= 1                                                                  
            if char_map[left_char] == 0:
                del char_map[left_char]
            left += 1    

      # (1,2,3,3)
        current_len = right - left + 1               
        if current_len > max_len:                       
            max_len = current_len                      
            substrings = [s[left:right + 1]]          
        elif current_len == max_len: 
            substrings.append(s[left:right + 1])    

# Example usage:
s = "aabbccdd"
k = 1
print(length_of_longest_substring_k_distinct(s, k))  # Output: (2, ["aa", "bb", "cc", "dd"])
