import random
v_list = ['a', 'e', 'i', 'o', 'u']
random.shuffle(v_list)
# shuffles a sequence in place
print(''.join(v_list))
# joins all items in a list into a string, then seperates them with space(what is in front of .join)
