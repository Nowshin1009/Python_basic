input_numbers = input("Enter numbers : ")
number_list = input_numbers.split(',')

for num in number_list :
    num = int(num)
    if num % 2 != 0:
        print(num)