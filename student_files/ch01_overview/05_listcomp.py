a = [1, 2, 3, 4, 5]
del a[1:3]		                    # a is now [1, 4, 5]
print(a)

list1 = [1, 2, 3, 4, 5]
list2 = [x*2 for x in list1]
print(list2)                        # [2, 4, 6, 8, 10]

list1 = [1, 2, 3, 4, 5]
list2 = [x*2 for x in list1 if x % 2 == 0]
print(list2)                        # [4, 8]
