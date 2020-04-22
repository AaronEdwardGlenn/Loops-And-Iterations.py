# here is our basic for loop setup
nums = [1, 2, 3, 4, 5]

for intigers in nums:
    print(intigers)

# here we are going to add a break with an if statemnt
numbers = [1, 2, 3, 4, 5, 6]

for intigers in numbers:
    if intigers == 3:
        print('Found!')
        break
    print(intigers)

# here we will continue with the loop after printing what we are looking for
numbers = [1, 2, 3, 4, 5, 6]

for intigers in numbers:
    if intigers == 3:
        print('Found!')
        continue
    print(intigers)

# we can nest for loops to perform actions on each run through the set
numbers = [1, 2, 3, 4, 5, 6]

for intigers in numbers:
    for colors in ['blue', 'green', 'red']:
        print(intigers, colors)

# range is a good tool for setting the number of times we want to loop through the set
for i in range(1, 11):
    print(i)

# while loops
x = 0

while x < 10:
    print(x)
    x += 1

# adding breaks
x = 1

while True:
    if x == 5:
        break
    print(x)
    x += 1
