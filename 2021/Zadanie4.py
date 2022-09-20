import os

# Convert instructions into text, "DOPISZ", "USUN", "ZMIEN", "PRZESUN"
def convert_instructions(data):
    res = []
    for arr in data:
        instr, char = arr.split()
        if instr == 'DOPISZ':
            res.append(char)
        elif instr == 'USUN':
            res = res[:-1]
        elif instr == 'PRZESUN':
            if char in res:
                idx = res.index(char)
                if ord(char) == 90:
                    res[idx] = 'A'
                else:
                    res[idx] = chr(ord(char) + 1)
        elif instr == 'ZMIEN':
            res[-1] = char
    return res

# Find longest sequence of same instructions
def longest_sequence_of_instructions(data):
    longest = 0
    most_used = ''
    act = 1
    curr = data[0].split()[0]
    for arr in data:
        instr, char = arr.split()
        if curr == instr:
            curr = instr
            act += 1
        else:
            curr = instr
            act = 1
        
        longest = max(longest, act)
        if longest == act:
            most_used = instr
        
        
    return longest, most_used

# Count most written letter by "DOPISZ"
def most_written_letter(data):
    stats = {}
    for arr in data:
        instr, char = arr.split()
        if instr == 'DOPISZ':
            if char in stats.keys():
                stats[char] += 1
            else:
                stats[char] = 1
    most_written = max(stats, key=stats.get)
    return most_written, stats.get(most_written)

# Main function
def main():
    # Extract data
    with open(os.path.join(os.path.dirname(__file__), './zalaczniki/instrukcje.txt'), 'r') as f:
        data = f.read().split('\n')[:-1] 
        solution_1 = len(convert_instructions(data))
        solution_2 = longest_sequence_of_instructions(data)
        solution_3 = most_written_letter(data)
        solution_4 = "".join(convert_instructions(data))
        # Print statements to check anwers
        # print(solution_1)
        # print(solution_2)
        # print(solution_3)
        # print(solution_4)
    # Write to answer file
    with open(os.path.join(os.path.dirname(__file__), './wyniki4.txt'), 'w') as f:
        f.write('Zadanie 4.1: ' + str(solution_1) + '\n')
        f.write('Zadanie 4.2: ' + " ".join(map(str,solution_2))+ '\n')
        f.write('Zadanie 4.3: ' + " ".join(map(str,solution_3))+ '\n')
        f.write('Zadanie 4.4: ' + str(solution_4))

if __name__ == '__main__':
    main()