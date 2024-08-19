def word_frequency(text: str) -> dict:
    text_lower = text.lower()
    list_words = text_lower.split(" ")
    set_pure_words = set()
    char_eng = "abcdefghijklmnopqrstuvwsyz"
    for word in list_words:
        pure_str = ""
        for char in word:
            if char in char_eng:
                pure_str += char
        set_pure_words.add(pure_str)
    dict_result = dict()
    for word in set_pure_words:
        dict_result[word] = text_lower.count(word)
    return dict_result


if __name__ == "__main__":
    print(word_frequency("Hello world! Hello everyone."))
    print(word_frequency("This is a test. This test is easy."))
    print(word_frequency("Python is fun. Fun fun fun!"))
    print(word_frequency("One word, one word."))
