import random
str_names = input("enter names separated with a , ")
names = str_names.split(", ")
random_num = random.randint(0, (len(names)-1))
print(f"{names[random_num]} is going to buy the meal today!")
