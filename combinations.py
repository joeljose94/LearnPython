#!/usr/bin/env python3

def get_pairs(elements):
    combinations = []
    size_limit = len(elements)  - 1
    for i in range(0, size_limit):
        for j in range(i, size_limit):
            combinations.append(elements[i] + elements[j])

    print(f'possible combinations are: {combinations}')
    

def get_count(limit):
    result = 0
    for i in range(0, limit - 1):
        for j in range(i, limit - 1):
            result += 1
    print("possible pairs: " + str(result))
    return result


elements = ["A", "B", "C", "D"]
# Should return ['AA', 'AB', 'AC', 'BB', 'BC', 'CC']
get_pairs(elements)
# Should Return: 6
get_count(4)
# Should Return: 45
get_count(10)