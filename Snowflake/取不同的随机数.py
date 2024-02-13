import random

class NumericUniformSamplingWithReplacement:
    def __init__(self):
        pass

    def next_value(self):
        return random.random()

class IntegerUniformSamplingWithoutReplacement:
    def __init__(self):
        self.uniform_zero_one = NumericUniformSamplingWithReplacement()
        self.current_index = 0
        self.values = {}
    
    def next_value(self):
        uint32_max = 2**32 - 1
        sampling_range = uint32_max - self.current_index
        exchange_index = self.current_index + int(sampling_range * self.uniform_zero_one.next_value())
        
        current_value = self.get_value(self.current_index)
        exchange_value = self.get_value(exchange_index)
        
        self.values[exchange_index] = current_value
        self.current_index += 1
        
        return exchange_value

    def get_value(self, index):
        return self.values.get(index, index)
    
    def get_num_stored_values(self):
        return len(self.values)


if __name__ == '__main__':
    randomize = IntegerUniformSamplingWithoutReplacement()

    validation_size = 1000000
    visited = set()

    for _ in range(validation_size):
        value = randomize.next_value()
        if value in visited:
            print(f"Error: duplicated {value}")
            break
        visited.add(value)

    print(f"# store values = {randomize.get_num_stored_values()}")

