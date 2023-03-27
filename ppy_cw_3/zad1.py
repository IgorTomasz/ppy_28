numbers = input("podaj liczby rodzielone przecinkiem: ")
numbers_list = numbers.split(",")

max_num = int(numbers_list[0])
min_num = int(numbers_list[0])
for i in range(0, len(numbers_list)):
    if int(numbers_list[i]) > max_num:
        max_num = int(numbers_list[i])
    if int(numbers_list[i]) < min_num:
        min_num = int(numbers_list[i])
print(min_num)
print(max_num)
