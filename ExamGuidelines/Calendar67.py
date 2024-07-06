m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def first_day(num_m, m):
    total_day = 0
    count_m = 0
    for num_day in m:
        if num_m - 1 == count_m:
            break
        total_day += num_day
        count_m += 1
    return total_day % 7


num_m = int(input("Enter month: "))
start = first_day(num_m, m) + 1
print("=" * 20)
print("Su Mo Tu We Th Fr Sa")
print("=" * 20)
for i in range(1, (m[num_m - 1] + 1) + start):
    if i - start <= 0:
        print("  ", end=" ")
    else:
        print(f"{i-start:>2}", end=" ")
    if (i) % 7 == 0:
        print()
print()
print("=" * 20)