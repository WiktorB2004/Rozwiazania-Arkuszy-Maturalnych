import os 
import math

# Task 4.1
def check_first_last_letter(numslist: list):
    first_occ = None
    count = 0
    for num in numslist:
        if str(num)[0] == str(num)[-1]:
            if first_occ == None:
                first_occ = num
                count += 1
                continue
            count += 1
    return [f'Ilosc slow zaczynajacych i konczacych sie na te sama litere: {count}', f'Pierwsza litera ktora konczy i zaczyna sie na te sama litere {int(first_occ)}']

# Task 4.2
def prime_factorization(numslist: list):
    most_factors = (-1,-1)
    most_distinct_factors = (-1,-1)
    for num in numslist:
        # Variables
        num = int(num)
        base_num = num
        # Computing
        factors = []
        while num % 2 == 0:
            factors.append(2)
            num /= 2
        for i in range(3, int(math.sqrt(num))+1,2):
            while num % i == 0:
                factors.append(i)
                num = num / i
        if num > 2:
            factors.append(int(num))
        
        if len(factors) > most_factors[1]:
            most_factors = base_num, len(factors)
        if len(set(factors)) >= most_distinct_factors[1]:
            most_distinct_factors = base_num, len(set(factors))

    return [f'Liczba z najwieksza iloscia czynnikow pierwszych oraz ich ilosc: {" ".join(map(str,most_factors))}', f'Liczba z najwieksza iloscia roznych czynnikow pierwszych oraz ich ilosc: {" ".join(map(str,most_distinct_factors))}']
                
            
# Task 4.3
# a)
def find_good_3set(numlist: list):
    numlist = list(map(int, numlist))
    res = []
    count = 0
    for x in numlist:
        for y in numlist:
            for z in numlist:
                if z % y == 0 and y % x == 0 and z != y and y !=x:
                    res.append([x,y,z])
                    count += 1
    return [res, count]

# b) The fastest way to do, probably not the most efficient!!!
def find_good_5set(numlist: list):
    numlist = list(map(int, numlist))
    res = []
    count = 0
    for u in numlist:
        for w in range(2,10000):
            tmp1 = u*w
            if tmp1 in numlist:
                for x in range(2,10000):
                    tmp2 = tmp1 * x
                    if tmp2 in numlist:
                        for y in range(2,10000):
                            tmp3 = tmp2 * y
                            if tmp3 in numlist:
                                for z in range(2,10000):
                                    tmp4 = tmp3 * z
                                    if tmp4 in numlist:
                                        if len(set([u,tmp1,tmp2,tmp3,tmp4])) == 5:
                                            res.append([u,tmp1,tmp2,tmp3,tmp4])
                                            count += 1
                                    if tmp4 > max(numlist):
                                        break
                            if tmp3 > max(numlist):
                                break
                    if tmp2 > max(numlist):
                        break
            if tmp1 > max(numlist):
                break
            
    return res, count


# Main function
def main():
    # Extract
    with open(os.path.join(os.path.dirname(__file__), './zalaczniki/liczby.txt'), 'r') as f:
        data = f.read().split()
        part1_solution = check_first_last_letter(data)
        part2_solution = prime_factorization(data)
        part31_solution = find_good_3set(data)
        part32_solution = find_good_5set(data)    
        
    # Write to answer files
    with open(os.path.join(os.path.dirname(__file__), './wyniki4.txt'), 'w') as f:
        f.write('Zadanie 4.1: \n')
        f.write('\n'.join(part1_solution))
        f.write('\nZadanie 4.2: \n')
        f.write('\n'.join(part2_solution))
        f.write('\nZadanie 4.3: \n')
        f.write('Trojki wypisane w pliku trojki.txt \nPiatki dostepne pod zmienna part32_solution[0]\n')
        f.write('a) Ilosc trojek: ' + str(part31_solution[1]) + '\n')
        f.write('b) Ilosc piatek: ' + str(part32_solution[1]))
        
    # Write answer to "trojki.txt" file
    with open(os.path.join(os.path.dirname(__file__), './trojki.txt'), 'w') as f:
        for trio in part31_solution[0]:
            f.write(f"{' '.join(map(str,trio))}\n")
        
if __name__=='__main__':
    main()
    