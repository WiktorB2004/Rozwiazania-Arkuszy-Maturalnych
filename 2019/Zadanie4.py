from math import gcd
import os

data_path = os.path.join(os.path.dirname(__file__), './zalaczniki/liczby.txt')

def powers_of_three(data):
    count = 0
    for num in data:
        while int(num) % 3 == 0 and int(num) > 3:
            num = int(num)//3
        if int(num) == 3 or int(num) == 1:
            count += 1
    return count


def factorial(x):
    if x == 1:
        return 1
    elif x == 0:
        return 1
    else:
        return (x*factorial(x-1))


def solution_2(data):
    res = []
    for num in data:
        sum = 0
        for d in num:
            sum += factorial(int(d))
        if sum == int(num):
            res.append(num)    
        
    return res

def solution_3(data):
    data = [int(x) for x in data]
    streak_arr = 0
    max_streak = 0
    streak = 0
    j = 1
    for i in range(len(data)-1):
        if gcd(data[i],data[i+1]) > 1:
            streak += 1
        else:
            if streak > max_streak:
                max_streak = streak
                streak_arr = data[i-streak+1:i]
            streak = 0
            
    return streak_arr[0], max_streak, gcd(*streak_arr)
    
    

if __name__ == '__main__':
    
    with open(data_path, 'r') as f:
        data_arr = f.read()[:-1].split()
    
    
    ex_1 = powers_of_three(data_arr)
    ex_2 = solution_2(data_arr)
    ex_3 = solution_3(data_arr)
    
    print(ex_1)
    print(ex_2)
    print(ex_3)