input_numbers = input()
number_list = input_numbers.split(',')
number_list = [int(num) for num in number_list]
for num in number_list:
    if num % 2 != 0:
        print(num)