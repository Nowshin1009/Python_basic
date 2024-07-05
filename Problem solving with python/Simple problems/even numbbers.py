def get_even_number(numbers):
    even_numbers = [num for num in numbers if num % 2== 0]
    return even_numbers
list_1 = [0,1,2,3,4,5,6,7,8,9,10]

print(get_even_number(list_1))