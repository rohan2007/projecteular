i = 0
sum = 0

limit = int(input("Enter the initial limit for loops: "))

array = []

i = 0

while i < limit:
    if i % 3 == 0 or i % 5 == 0:
            array.append(i)
    i = i + 1

test_list = []

for i in array:
    if i not in test_list:
        test_list.append(i)


for i in test_list:
    sum = sum + i


print(sum)