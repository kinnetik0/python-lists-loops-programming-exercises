import random
# Remember to import random function here

my_list = [4, 5, 734, 43, 45]

# The magic goes below
for x in range(10): 
    my_random = random.randint(1,100)
    my_list.append(my_random)

print(my_list)
