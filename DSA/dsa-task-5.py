my_array = [1, 2, 3, 4, 5]   #exited with code=0 in 0.108 seconds
my_array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_array_3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

# Big O of 1
def B1(my_value):
    print(1+1)
print("This indicates Big O of 1")
B1(my_array)

# Big O of N
def BN(my_value):
    for i in my_value:
        print(i)
print("This indicates Big O of n")
BN(my_array_2)

# Big O of N*N
def BNN(my_value):
    for numbers in my_value:
        for ids in numbers:
            print(ids)
print("This indicates Big O of N*N")
BNN(my_array_3)