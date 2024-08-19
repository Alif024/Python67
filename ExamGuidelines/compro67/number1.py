def find_single_occurrence_numbers(numbers: list) -> list:
    dict_num = dict()
    for number in numbers:
        if number in dict_num:
            dict_num[number] += 1
        else:
            dict_num[number] = 1
    print(dict_num)
    return [number for number, count_num in dict_num.items() if count_num == 1]


if __name__ == "__main__":
    print(find_single_occurrence_numbers([4, 5, 6, 4, 7, 5, 8]))
    print(find_single_occurrence_numbers([1, 2, 2, 3, 3, 4, 4]))
    print(find_single_occurrence_numbers([1, 2, 3, 4, 5, 6]))
    print(find_single_occurrence_numbers([1, 1, 1, 1, 1]))
