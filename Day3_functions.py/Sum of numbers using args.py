def sum_all_numbers(*args):
    total = 0
    for num in args:
        total +=num
    return total
    
input_numbers = input("Enter numbers separated by spaces: ")
numbers=[int(i) for i in input_numbers.split()]
print("Sum of all the numbers is:", sum_all_numbers(*numbers))

