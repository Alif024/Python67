def format_strings(*args):
    # lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_char = "abcdefghijklmnopqrstuvwxyz"
    upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str_args = ""
    result = ""
    for arg in args:
        str_args += arg
    for char_args in str_args:
        if char_args in upper_char:
            result += char_args
        elif char_args == " ":
            result += "-"
        else:
            for position_char in range(26):
                if char_args == lower_char[position_char]:
                    result += upper_char[position_char]
    return result


if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)  # Output: "HELLOWORLDTHISISATEST"

    result = format_strings("Python", "is", "fun")
    print(result)  # Output: "PYTHONISFUN"

    result = format_strings("Hello world")
    print(result)  # Output: "HELLO-WORLD"