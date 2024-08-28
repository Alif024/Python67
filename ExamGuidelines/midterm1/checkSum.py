def convert_hex_num_to_digit(*args):
    list_hex_nums = []
    for arg in args:
        # print(hex(arg))
        hex_nums = hex(arg).replace("0x", "")
        list_hex_digits = []
        for str_digit in hex_nums:
            int16_digit = int("0x"+str_digit, 16)
            list_hex_digits.append(int16_digit)
            # print(hex(int16_digit))
        list_hex_nums.append(list_hex_digits)
    # print(list_hex_nums)
    return list_hex_nums


def get_hex_sum_partial(list_hex_nums):
    # print(list_hex_nums)
    list_carry_nums = []
    sum_partial = []
    for i in range(len(list_hex_nums[0])):
        last_digits = []
        for i in range(len(list_hex_nums)):
            if len(list_hex_nums[i]) != 0:
                last_digits.append(list_hex_nums[i].pop(-1))
        # print(last_digits)
        if len(list_carry_nums) == 0:
            sum_last_digit = sum(last_digits)
        else:
            sum_last_digit = sum(last_digits) + list_carry_nums[0]
        str_result_sum_last_digit = hex(sum_last_digit).replace("0x", "")
        list_str_result_sum_last_digit = list(str_result_sum_last_digit)
        # print(list_str_result_sum_last_digit)
        str_carry_num = []
        for i in range(len(list_str_result_sum_last_digit)):
            # print(list_str_result_sum_last_digit[i])
            if i == len(list_str_result_sum_last_digit)-1:
                sum_partial.insert(
                    0, int(list_str_result_sum_last_digit[i], 16))
            else:
                str_carry_num.insert(0, list_str_result_sum_last_digit[i])
        # print(str_carry_num)
        if len(str_carry_num) == 0:
            list_carry_nums.insert(0, 0)
        else:
            list_carry_nums.insert(0, int("0x"+("".join(str_carry_num)), 16))
    # print(list_carry_nums)
    # print(sum_partial)
    # print(list_hex_nums)
    return sum_partial, list_carry_nums


def get_hex_sum_result(sum_partial, list_carry_nums):
    len_nums_add = len(list_carry_nums) + 1 - len(sum_partial)
    list_nums_add = list_carry_nums[0:len_nums_add]
    str_sum_partial = "0x"+"".join([hex(int_digit)
                                   for int_digit in sum_partial]).replace("0x", "")
    int_sum_partial = int(str_sum_partial, 16)
    str_list_nums_add = "0x" + \
        "".join([hex(int_digit)
                for int_digit in list_nums_add]).replace("0x", "")
    int_nums_add = int(str_list_nums_add, 16)
    # print(hex(int_sum_partial+int_nums_add))
    return int_sum_partial+int_nums_add


def check_sum(sum_result):
    bin_sum_result = bin(sum_result).replace("0b", "")
    result_check_sum = ""
    for char in bin_sum_result:
        if char == "0":
            result_check_sum += "1"
        else:
            result_check_sum += "0"
    # print(bin_sum_result)
    # print(result_check_sum)
    # print(hex(int_check_sum))
    int_check_sum = int("0b"+result_check_sum, 2)
    return int_check_sum


def display(list_carry_nums, list_arg, sum_partial, sum_result, int_check_sum):
    print("-"*20)
    str_carry_nums = "".join([str(digit) for digit in list_carry_nums])
    for char in str_carry_nums:
        print(f"{char:>2}", end="")
    print()
    print()
    for i in list_arg:
        print("  ", end="")
        # print(hex(i).replace("0x", ""))
        for char_hex in hex(i).replace("0x", ""):
            if len(str(i)) == 1:
                print(f"{'0':>2}"*4, end="")
            else:
                print(f"{char_hex.upper():>2}", end="")
        print()
    print("  ---------")
    str_sum_partial = "".join(
        [hex(digit).replace("0x", "").upper() for digit in sum_partial])
    print("  ", end="")
    for char in str_sum_partial:
        print(f"{char:>2}", end="")
    print()
    list_add = list_carry_nums[0: len(
        list_carry_nums)+1 - len(hex(list_arg[0]).replace("0x", ""))]
    # list_add = [1,2,3]
    # print(list_add)
    if len(list_add) == 1:
        print(f"{list_add[0]:>10}")
    else:
        str_num_adds = "  ".join([str(digit) for digit in list_add])
        print(f"{str_num_adds:>10}")
    print("  ---------")
    print("  ", end="")
    for char in hex(sum_result).replace("0x", ""):
        print(f"{char.upper():>2}", end="")
    print()
    print("  ", end="")
    for char in hex(int_check_sum).replace("0x", ""):
        if int_check_sum == 0:
            print(f"{char.upper():>2}"*4, end="")
        else:
            print(f"{char.upper():>2}", end="")
    print()
    print("-"*20)


def sum_hex_num(*args):
    list_arg = list(args)
    list_hex_nums = convert_hex_num_to_digit(*args)
    sum_partial, list_carry_nums = get_hex_sum_partial(list_hex_nums)
    sum_result = get_hex_sum_result(sum_partial, list_carry_nums)
    int_check_sum = check_sum(sum_result)
    display(list_carry_nums, list_arg, sum_partial, sum_result, int_check_sum)


sum_hex_num(0x5,0x10,0xf,0xa,0x9)
# sum_hex_num(0x466f, 0x7267, 0x757a, 0x616e, 0x7040)
