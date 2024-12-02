from utils.utils import get_lines

def get_lists(lines: list[str]):
    left_list = []
    right_list = []
    for line in lines:
        elements = line.split()
        left, right = elements[0], elements[1]
        
        left_list.append(int(left))
        right_list.append(int(right))
    
    return left_list, right_list

def retrieve_gaps(list1: list[int], list2: list[int]):
    return [abs(list1[i] - list2[i]) for i in range(len(list1))]

def part_one(get_lists, retrieve_gaps):
    lines = get_lines("day1/input1.txt")
    left_list, right_list = get_lists(lines)

    left_list.sort()
    right_list.sort()

    gaps = retrieve_gaps(left_list, right_list)

    print(gaps)
    print(sum(gaps))

def part_two():
    lines = get_lines("day1/input1.txt")
    left_list, right_list = get_lists(lines)
    map_occurences = extract_occurences(left_list, right_list)

    total = 0
    for el in left_list:
        print(el, map_occurences[el])
        total+= el * map_occurences[el]

    return total

def extract_occurences(left_list, right_list):
    map_occurences = {}
    for el in left_list:
        map_occurences[el] = 0

    for el in right_list:
        if (el in map_occurences):
            map_occurences[el] += 1

    return map_occurences

if __name__ == '__main__':
    part_one(get_lists, retrieve_gaps)
    print(part_two())