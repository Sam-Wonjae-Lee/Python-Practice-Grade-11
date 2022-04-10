def sum(x,y):
    sum = x + y
    if sum in range(15,21):
        return 20
    else:
        return sum

input_a = int(input("Enter a: "))
input_b = int(input("Enter b: "))
print(sum(input_a, input_b))