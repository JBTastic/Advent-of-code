from ast import literal_eval

def toggle(state, pos):
    return state ^ (1 << pos)

def is_on(state, pos):
    return (state >> pos) & 1

def set_off(state, pos):
    return state & ~(1 << pos)


def part1(data: str):
    lines = data.splitlines()
    
    for machine in lines:
        start_of_buttons = machine.find("(")
        start_of_joltage = machine.find("{")
        
        indicator_lights = machine[0:start_of_buttons-1].strip()
        button_sequence = machine[start_of_buttons: start_of_joltage-1].strip()
        
        button_sequence = literal_eval("(" + button_sequence.replace(") (", "), (") + ")")
        length_indices = {}

        for idx, seq in enumerate(button_sequence):
            length = len(seq) if isinstance(seq, tuple) else 1
            if length not in length_indices:
                length_indices[length] = set()
            length_indices[length].add(idx)

        
        # Use bitmask to represent the state of 4 indicator lights to reach maximum speed
        initial_lights = 0
        
        completed_lights = 0
        for i, char in enumerate(indicator_lights.strip("[]")):
            if char == "#":
                completed_lights = toggle(completed_lights, i)
        
        print(f"Indicator Lights: {indicator_lights}")
        print(f"Button Sequence: {button_sequence}")
        print(f"Button Sequence lens: {length_indices}")
        print(f"Completed Lights: {bin(completed_lights)}")
        break

def part2(data: str):
    pass


if __name__ == "__main__":
    with open("example.txt", "r") as example:
        example_data = example.read()
        
    with open("input.txt", "r") as input:
        input_data = input.read()
        
    part1(example_data)
    part2(example_data) 