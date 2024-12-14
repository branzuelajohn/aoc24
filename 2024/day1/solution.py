
def parse_input(input_file):
    """
    Reads the input file and processes it into a usable format.
    :param input_file: Path to the input file
    :return: Processed input data
    """
    with open(input_file, 'r') as f:
        data = f.read().strip()
    # Modify this depending on the problem (e.g., splitlines(), split(), etc.)
    return data.splitlines()

def part1(data):
    """
    Solves Part 1 of the challenge.
    :param data: Parsed input data
    :return: Solution for Part 1
    """
    # Implement the logic for Part 1 here


    # pair up smallest number in left list and smallest number in right list
    # second smallest let number and second smallest right number so on and so forth

    result = 0
    left = []
    right = []
    for item in data:
        contents = item.split('   ')
        left.append(contents[0])
        right.append(contents[1])
    
    
    left.sort()
    right.sort()
    print(left)
    print(right) 

    for i in range(len(left)):
        result += abs(int(left[i]) - int(right[i]))
    return result

def part2(data):
    """
    Solves Part 2 of the challenge.
    :param data: Parsed input data
    :return: Solution for Part 2
    """
    # Implement the logic for Part 2 here
    result = 0
    left = []
    right = []
    map = {}
    for item in data:
        contents = item.split('   ')
        left.append(contents[0])
        # right.append(contents[1])
        map[contents[1]] = map.get(contents[1], 0) + 1
    
    
    # for r in right:
    #     map[r] = map.get(r, 0) + 1
    print(map)
    for l in left:
        if l in map:
            result += int(l) * map[l]
        else:
            result += 0 
    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python solution.py <input_file>")
        sys.exit(1)
    
    # Parse the input
    input_file = sys.argv[1]
    data = parse_input(input_file)
    
    # Solve Part 1
    print("Part 1:", part1(data))
    
    # Solve Part 2
    print("Part 2:", part2(data))