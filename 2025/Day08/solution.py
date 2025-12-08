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
    
    print(vectors)
    print("-------")

    while num_connection_pairs > 0:
        vec_list = list(vectors.keys())
        closest_distance = -1
        closest_vectors = []
        for i in range(len(vec_list)-1):
            for j in range(i+1, len(vec_list)):
                v1 = vec_list[i]
                v2 = vec_list[j]
                
                # If they are in the same circuit, skip
                if vectors[v1] == vectors[v2]:
                    continue

                curr_distance = distance(v1, v2)
                if curr_distance < closest_distance or closest_distance == -1:
                    closest_distance = curr_distance
                    closest_vectors = [vec_list[i], vec_list[j]]
        
        # Put the closest vectors in the same circuit
        # The two vectors are guaranteed to be in different circuits
        # because of the check above
        vector_A = vectors[closest_vectors[0]]
        vector_B = vectors[closest_vectors[1]]

        # Find all keys that have the value vector_B and set them to vector_A
        for key in vectors:
            if vectors[key] == vector_B:
                vectors[key] = vector_A
                
        # vectors[closest_vectors[1]] = vectors[closest_vectors[0]]
        num_connection_pairs -= 1
        print(vectors)
        print("-------")
                
    # print(closest_distance)
    # print(closest_vectors)
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