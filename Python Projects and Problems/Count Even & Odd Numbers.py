numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for x in numbers:
    if x % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Even numbers: ", count_even)
print("Odd numbers: ", count_odd)