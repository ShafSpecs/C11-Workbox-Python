#####
# LIST COMPREHENSION
# Constructing new arrays from an iterable(lists, ranges, etc.)
#####

lst = [x for x in range(1, 6)]
print(lst)

lst2 = list(map(lambda x: x * 10, [i for i in range(1, 4)]))
print(lst2)

lst3 = list(range(1, 11))
print(lst3)

lst4 = list(map(lambda i: i * 2, range(1, 11)))
print(lst4)


### Square the values of even numbers between 1-100 and just print the odd ones, i.e [1, 4, 3, 16,...].
play = [x**2 if x % 2 == 0 else x for x in range(1, 101)]
print(play)

play2 = list(map(lambda i: i**2 if i % 2 == 0 else i, range(1, 101)))
print(play2)


work = [i for i in range(2, 100)]
print(work)


user_input = [int(input("Enter a grade: ")) for i in range(1, 6)]
print(user_input)
