def change_me(lst, tup, scalar):
    scalar += 1
    lst *= scalar
    tup *= scalar
    print(lst, tup, scalar)     # [1, 2, 3, 1, 2, 3] (4, 5, 6, 4, 5, 6) 2


scalar = 1
lst = [1, 2, 3]
tup = (4, 5, 6)
change_me(lst, tup, scalar)
print(lst, tup, scalar)        # [1, 2, 3, 1, 2, 3] (4, 5, 6) 1
