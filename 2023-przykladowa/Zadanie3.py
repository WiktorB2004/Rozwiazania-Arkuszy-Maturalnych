import os
import math

# Check if number is prime
def isPrime(number):
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


# Count the M prime numbers
def count_M_primes(data):
    count = 0
    for arr in data:
        if isPrime(arr[0]):
            count += 1
    return count


def count_numbers_where_GCD_1(data):
    count = 0
    for arr in data:
        if math.gcd(arr[0], arr[1]) == 1:
            count += 1
    return count


# Rozwiazanie bez uzycia funkcji wbudowanych pythona, mozna dodac jeszcze programowanie dynamiczne
# def modulo_exponentiation(a, x, M):
#     if x == 0:
#         return 1
#     if x % 2 == 0:
#         w = modulo_exponentiation(a, x / 2, M)
#         return w * w % M
#     if x % 2 == 1:
#         w = modulo_exponentiation(a, (x - 1) / 2, M)
#         return a * w * w % M


# def find_x_for_modulo(data):
#     count = 0
#     for arr in data:
#         for x in range(0, arr[0] - 1):
#             if modulo_exponentiation(arr[1], x, arr[0]) == arr[2]:
#                 count += 1
#                 break
#     return count

# rozwiazanie z uzyciem funkcji wbudowanych pythona
def find_x_for_modulo(data):
    count = 0
    for arr in data:
        for x in range(0, arr[0] - 1):
            d = pow(arr[1], x, arr[0])
            if d == arr[2]:
                count += 1
                break
    return count

# Main function, its execution time is not "instant"
def main():
    with open(os.path.join(os.path.dirname(__file__), "./zalaczniki/liczby.txt"), "r") as f:
        # Data extraction
        raw_data = f.read().split("\n")
        data = [list(map(int, x.split())) for x in raw_data]
        # Solutions
        solution_1 = count_M_primes(data)
        solution_2 = count_numbers_where_GCD_1(data)
        solution_3 = find_x_for_modulo(data)
        # Print statements to check answers
        # print(solution_1)
        # print(solution_2)
        # print(solution_3)

        # Write to answer files
    with open(os.path.join(os.path.dirname(__file__), "./wyniki3.txt"), "w") as f:
        f.write("Zadanie 3.3: " + str(solution_1) + "\n")
        f.write("Zadanie 3.4: " + str(solution_2) + "\n")
        f.write("Zadanie 3.5: " + str(solution_3))
        
if __name__ == '__main__':
    main()