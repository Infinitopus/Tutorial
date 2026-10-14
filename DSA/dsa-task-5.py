my_array = [1, 2, 3, 4, 5]   #exited with code=0 in 0.108 seconds
my_array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_array_3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

# Big O of 1
def my_big_o_of_one(my_value):
    print(1+1)
print("This indicates Big O of 1")

# Big O of N
def my_big_o_of_n(my_value):
    for i in my_value:
        print(i)
print("This indicates Big O of n")

# Big O of N*N
def my_big_o_of_n_n(my_value):
    for numbers in my_value:
        for ids in numbers:
            print(ids)
print("This indicates Big O of N*N")
my_big_o_of_n_n(my_array_3)