import math

def calculate_mean(data):
    total = sum(data)
    mean = total / len(data)
    return mean

def calculate_standard_deviation(data):
    mean = calculate_mean(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_deviation = math.sqrt(variance)
    return std_deviation

def test_calculate_mean():
    # Test case 1
    data = [1, 2, 3, 4, 5]
    assert calculate_mean(data) == 3.0
    
    # Test case 2
    data = [0, 0, 0, 0]
    assert calculate_mean(data) == 0.0

def test_calculate_standard_deviation():
    # Test case 1
    data = [1, 2, 3, 4, 5]
    assert calculate_standard_deviation(data) == 1.4142135623730951
    
    # Test case 2
    data = [0, 0, 0, 0]
    assert calculate_standard_deviation(data) == 0.0

def main():
    data = [1, 2, 3, 4, 5]
    
    # Calculate mean
    mean = calculate_mean(data)
    print("Mean:", mean)
    
    # Calculate standard deviation
    std_deviation = calculate_standard_deviation(data)
    print("Standard Deviation:", std_deviation)

if __name__ == '__main__':
    main()

# Run the test cases
test_calculate_mean()
test_calculate_standard_deviation()
