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

def find_minimum(data):
    min_val = min(data)
    return min_val

def find_maximum(data):
    max_val = max(data)
    return max_val

def sort_data(data):
    sorted_data = sorted(data)
    return sorted_data

def main():
    data = [1, 7, 3, 2, 5, 9, 4, 6, 8]
    
    # Calculate mean
    mean = calculate_mean(data)
    print("Mean:", mean)
    
    # Calculate standard deviation
    std_deviation = calculate_standard_deviation(data)
    print("Standard Deviation:", std_deviation)
    
    # Find the minimum value
    min_val = find_minimum(data)
    print("Minimum Value:", min_val)
    
    # Find the maximum value
    max_val = find_maximum(data)
    print("Maximum Value:", max_val)
    
    # Sort the data
    sorted_data = sort_data(data)
    print("Sorted Data:", sorted_data)

if __name__ == '__main__':
    main()
