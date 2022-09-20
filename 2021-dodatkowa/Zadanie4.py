import os
import re

# Count numbers in data string -> 4.1
def count_numbers(data):
    return len(re.findall('\d',data))

# Find hidden text using algorithm from task 4.2
def find_hidden_text(data):
    password = ''
    step = 0
    for i in range(0, len(data)+1, 20):
        password += data[i-1][step-1]
        step += 1
    
    return password[1:]

# Find hidden text using algorithm from task 4.3, if 1 letter missing for string to become PALINDROME -> extract middle letter and add to current word
def find_word_in_palindromes(data):
    palindromes = ''
    for arr in data:
        if arr + arr[0] == str(arr + arr[0])[::-1]:
            palindromes += arr[25]
        elif arr[-1] + arr   == str(arr[-1] + arr)[::-1]:
            palindromes += arr[24]
            
    return palindromes

# Find hidden text using algorithm from task 4.4
def group_find_word(data):
    res = ''
    for arr in data:
        digits = re.findall('\d', arr)
        for i in range(1,len(digits),2):
            if int(digits[i-1] + digits[i]) >= 65 and int(digits[i-1] + digits[i]) <= 90 and res[-3:] != 'XXX':
                res += chr(int(digits[i-1] + digits[i]))
                
    return res



# Main function of the programm
def main():
    # Load and extract data from file
    with open(os.path.join(os.path.dirname(__file__), './zalaczniki/napisy.txt'), 'r') as f:
        raw_data = f.read()
        data_arr = raw_data.split()

        solution_1 = count_numbers(raw_data)
        solution_2 = find_hidden_text(data_arr)
        solution_3 = find_word_in_palindromes(data_arr)
        solution_4 = group_find_word(data_arr)
        # Print statements to check answers
        # print(solution_1 == 46504)
        # print(solution_2 == "UDALOSIEIZDAJEMYEGZAMINYMATURALNEZWIELUPRZEDMIOTOW")
        # print(solution_3 == "INFORMATYKA")
        # print(solution_4 == "NAPISANIEMATURYXXX")
    # Write to answer file
    with open(os.path.join(os.path.dirname(__file__), './wyniki4.txt'), 'w') as f:
        f.write('Zadanie 4.1: ' + str(solution_1) + '\n')
        f.write('Zadanie 4.2: ' + str(solution_2) + '\n')
        f.write('Zadanie 4.3: ' + str(solution_3) + '\n')
        f.write('Zadanie 4.4: ' + str(solution_4) + '\n')
    
if __name__ == '__main__':
    main()