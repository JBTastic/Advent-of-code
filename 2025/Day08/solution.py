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

    # Pre-compute all distances between vectors
    vec_list = list(vectors.keys())
    distances = dict()
    for i in range(len(vec_list)-1):
        for j in range(i+1, len(vec_list)):
            distances[(vec_list[i], vec_list[j])] = distance(vec_list[i], vec_list[j])
    
    # Sort distances from smallest to largest and only take the first num_connection_pairs
    distances = dict(list(sorted(distances.items(), key=lambda item: item[1]))[:num_connection_pairs])
    
    # Connect first 10 junction boxes based on their distances
    for (vec1, vec2), _ in distances.items():
        if vectors[vec1] != vectors[vec2]: # If not on same circuit
            # Connect the two circuits by assigning all vectors with circuit ID of vec2 to vec1
            old_circuit_id = vectors[vec2]
            new_circuit_id = vectors[vec1]
            for vec in vectors:
                if vectors[vec] == old_circuit_id:
                    vectors[vec] = new_circuit_id
    
    # Number of distnict circuits
    circuit_count = len(set(vectors.values()))
    
    # Sizes of the three largest circuits multiplied together
    value_counts = {} # key: circuit ID, value: count of vectors in that circuit
    for value in vectors.values():
        if value in value_counts:
            value_counts[value] += 1
        else:
            value_counts[value] = 1
    sorted_counts = sorted(value_counts.values(), reverse=True) # Sort largest to smallest
    top3_counts = sorted_counts[:3] # Only take top 3
    circuit_sizes = top3_counts[0] * top3_counts[1] * top3_counts[2] # Mutliply together

    print(f"Part 1:\nCircuit count: {circuit_count}\nThe size of the three largest circuits multiplied together: {circuit_sizes}\n")

def part2(data: str):
    lines = data.splitlines()
    
    # Create a dictionary,
    # where the key is each line converted into a tuple with 3 numbers (so a vector)
    # and the value is the circuit ID
    vectors = {
        tuple(map(int, line.split(","))): i
        for i, line in enumerate(lines, start=1)
    }

    # Pre-compute all distances between vectors
    vec_list = list(vectors.keys())
    distances = dict()
    for i in range(len(vec_list)-1):
        for j in range(i+1, len(vec_list)):
            distances[(vec_list[i], vec_list[j])] = distance(vec_list[i], vec_list[j])
    
    # Sort distances from smallest to largest
    distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    
    # Connect all junction boxes based on their distances until all are connected
    for (vec1, vec2), _ in distances.items():
        if vectors[vec1] != vectors[vec2]: # If not on same circuit
            # Connect the two circuits by assigning all vectors with circuit ID of vec2 to vec1
            old_circuit_id = vectors[vec2]
            new_circuit_id = vectors[vec1]
            for vec in vectors:
                if vectors[vec] == old_circuit_id:
                    vectors[vec] = new_circuit_id
            last_vectors = (vec1, vec2) # Store the last connected vectors
    
    # Number of distnict circuits
    circuit_count = len(set(vectors.values()))
    
    # The X of the last vectors multiplied together
    multiplication_of_last_vectors_X = last_vectors[0][0] * last_vectors[1][0]

    print(f"Part 2:\nCircuit count: {circuit_count}\nThe X of the last vectors multiplied together: {multiplication_of_last_vectors_X}")


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
        
    example_num_connection_pairs = 10
    input_num_connection_pairs = 1000
    
    part1(input_data, input_num_connection_pairs)
    part2(input_data) 