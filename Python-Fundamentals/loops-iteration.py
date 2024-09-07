
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('found!')
        # break
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)


for i in range(1,11):
    print(i)



# While loops
x = 0
while x < 10: # Finite loop
    if x == 5:
        break
    print(x)
    x+=1

# Infinite Loop
while True:
    print(x)
    x+=1