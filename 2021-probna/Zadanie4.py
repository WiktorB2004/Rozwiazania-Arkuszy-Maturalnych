import os

# Count from how many countries do we have galleries in dataset
def count_countries(data):
    res = {}
    for option in data:
        country, city, *dimensions = option.split()
        if country in res.keys():
            res[country] += 1
        else:
            res[country] = 1
    
    return res

# Count galeries and their area
def count_galleries_and_calculate_area(data):
    res = {}
    for option in data:
        country, city, *dimensions = option.split()
        res[city] = [sum([int(dimensions[i])*int(dimensions[i+1]) for i in range(0,len(dimensions)-2,2)]) , sum(int(x) > 0 for x in dimensions)//2]
        
    return res

# Find similar (by area) locals in city
def count_similar_locals(data):
    res = {}
    for option in data:
        country, city, *dimensions = option.split()
        locals = {}
        for i in range(0,len(dimensions)-2,2):
            if int(dimensions[i]) > 0:
                square_dim = int(dimensions[i])*int(dimensions[i+1])
                if square_dim in locals.keys():
                    locals[square_dim] += 1
                else:
                    locals[square_dim] = 1
        res[city] = len(locals)
            
        
        
    return res
            
# Main function
def main():
    with open(os.path.join(os.path.dirname(__file__), './zalaczniki/galerie.txt'), 'r') as f:
        data = f.read().split('\n')[:-1]
    
        solution_1 = count_countries(data)
        solution_2 = count_galleries_and_calculate_area(data)
        similar_locals = count_similar_locals(data)
        solution_3 = f'Najmniej: {min(similar_locals, key=similar_locals.get)} {min(similar_locals.values())}', f'Najwiecej: {max(similar_locals, key=similar_locals.get)} {max(similar_locals.values())}'
    # Print solutions to check the answer
    # print(solution_1)
    # print(solution_2)
    # print(solution_3)
    
    # 4.1 Solution
    with open(os.path.join(os.path.dirname(__file__), './wynik4_1.txt'), 'w') as f:
        f.write('\n'.join(map(str,solution_1.items())))
        
    # 4.2 A solution write to file, on exam you should do it different way (data should be without parenthesis etc.). The best is to just exec the programm and copy/paste the solutions to file
    with open(os.path.join(os.path.dirname(__file__), './wynik4_2a.txt'), 'w') as f:
        f.write('\n'.join(map(str, solution_2.items())))

    # 4.2 B solution write to file
    with open(os.path.join(os.path.dirname(__file__), './wynik4_2b.txt'), 'w') as f:
        highest_area_city = max(solution_2, key=solution_2.get)
        lowest_area_city = min(solution_2, key=solution_2.get)
        highest = highest_area_city, solution_2[highest_area_city][0]
        lowest = lowest_area_city, solution_2[lowest_area_city][0]
        f.write(' '.join(map(str, highest)) + '\n')
        f.write(' '.join(map(str, lowest)))
    
    # 4.3 Solution write to file
    with open(os.path.join(os.path.dirname(__file__), './wynik4_3.txt'), 'w') as f:
        f.write('\n'.join(solution_3))


if __name__=='__main__':
    main()