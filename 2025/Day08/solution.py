from math import sqrt

def distance(vec1: tuple, vec2: tuple) -> float:
    return sqrt((vec1[0] - vec2[0])**2 + (vec1[1] - vec2[1])**2 + (vec1[2] - vec2[2])**2)

def part1(data: str, num_connection_pairs: int):
    lines = data.splitlines()
    
    # Create a dictionary,
    # where the key is each line converted into a tuple with 3 numbers (so a vector)
    # and the value is the circuit ID
    vectors = {
        tuple(map(int, line.split(","))): i
        for i, line in enumerate(lines, start=1)
    }
    
    # print(vectors)
    # print("-------")

    # Pre-compute all distances between vectors
    vec_list = list(vectors.keys())
    distances = dict()
    # print(vec_list)
    for i in range(len(vec_list)-1):
            for j in range(i+1, len(vec_list)):
                distances[(vec_list[i], vec_list[j])] = distance(vec_list[i], vec_list[j])
    
    # Sort distances from smallest to largest
    distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    
    while num_connection_pairs > 0:
        for (vec1, vec2), _ in distances.items():
            if vectors[vec1] != vectors[vec2]: # If not on same circuit
                # Connect the two circuits by assigning all vectors with circuit ID of vec2 to vec1
                old_circuit_id = vectors[vec2]
                new_circuit_id = vectors[vec1]
                for vec in vectors:
                    if vectors[vec] == old_circuit_id:
                        vectors[vec] = new_circuit_id
                break  # Exit the for loop to re-evaluate distances
            
        num_connection_pairs -= 1
        print(vectors)
        print("-------")
    
    # print(distances)
                
    circuit_count = len(set(vectors.values()))

    print(f"Part 1: {circuit_count}")

def part2(data: str):
    pass


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
        
    example_num_connection_pairs = 10
    input_num_connection_pairs = 1000
    
    part1(example_data, example_num_connection_pairs)
    part2(example_data) 