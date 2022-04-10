# Question 21 from 'leetcode'
# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.
print("Create elements by typing anything then space between each of them")
ele1 = input("What are the elements to your first list?: ")
l1 = ele1.split()
# splits a string into a elements of a list
print(l1)

ele2 = input("What are the elements to your second list?: ")
l2 = ele2.split()
print(l2)

l3 = l1 + l2
l3.sort()
print("Here is your merged alphanumerical list:", l3)