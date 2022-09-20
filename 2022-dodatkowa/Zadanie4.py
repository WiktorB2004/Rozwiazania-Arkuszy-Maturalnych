import os
import math

# Find if number X after reversing its digits is divisible by 27 -> Task 4.1
def find_reflections_divisible_by_17(numbers):
    res = []
    for number in numbers:
        if int(number[::-1]) % 17 == 0:
            res.append(number[::-1])
            
    return res

#  Find the highest absolute value from numbers -> Task 4.2
def find_highest_absolute_value(data):
    absolute_values = []
    for number in data:
        absolute_values.append((int(number),abs(int(number)) - int(number[::-1])))
    return max(absolute_values)

# Checks if number is prime
def isPrime(number):
    for i in range(2,int(math.sqrt(int(number)))):
        if int(number) % i == 0:
            return False
    return True

# Check if prime number X after reversing its digits is also prime-> Task 4.3
def find_reflections_with_prime_numbers(data):
    res = []
    for number in data:
        if isPrime(number) and isPrime(number[::-1]):
            res.append(int(number))
            
    return res

# Count repetitions and their amount in data -> 4.4
def count_duplicates(data):
    different_values = []
    two_repetitions_count = 0
    three_repetitions_count = 0
    for number in data:
        count = data.count(number)
        if count >= 1 and number not in different_values:
            different_values.append(number)
        if count == 2:
            two_repetitions_count += 1
        if count == 3:
            three_repetitions_count += 1
    
    return len(different_values), two_repetitions_count//2, three_repetitions_count//3

# Main function
def main():
    # Extract data
    with open(os.path.join(os.path.dirname(__file__), './zalaczniki/liczby.txt'), 'r') as f:
        
        data = f.read().split()
        solution_1 = find_reflections_divisible_by_17(data)
        solution_2 = find_highest_absolute_value(data)
        solution_3 = find_reflections_with_prime_numbers(data)
        solution_4 = count_duplicates(data)
        
    # Write answers to file
    with open(os.path.join(os.path.dirname(__file__), './wyniki4.txt'), 'w') as f:
        f.write('4.1 -> ' + f'{" ".join(solution_1)}\n')
        f.write('4.2 -> ' + f'{" ".join(map(str,solution_2))}\n')
        f.write('4.3 -> ' + f'{" ".join(map(str,solution_3))}\n')
        f.write('4.4 -> ' + f'{" ".join(map(str,solution_4))}\n')
        
if __name__ == '__main__':
    main()