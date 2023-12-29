import numpy as np
from scipy.stats import kurtosis, skew

def calculate_statistics(values):
    statistics = {}
    print("The results are: ");
    # Mean
    statistics['Mean'] = np.mean(values)

    # Median
    statistics['Median'] = np.median(values)

    # Mode
    mode_result = np.bincount(values)
    statistics['Mode'] = np.argmax(mode_result)

    # Standard Deviation
    statistics['Standard Deviation'] = np.std(values)

    # Kurtosis
    statistics['Kurtosis'] = kurtosis(values)

    # Skewness
    statistics['Skewness'] = skew(values)

    # Minimum
    statistics['Minimum'] = np.min(values)

    # Maximum
    statistics['Maximum'] = np.max(values)

    # Sum
    statistics['Sum'] = np.sum(values)

    # Count
    statistics['Count'] = len(values)

    return statistics

# Example usage:
array_of_values = [2834000, 26513000, 8759000, 3694000,5005000,
13622000,22151000,5873000,11727000,3074000,9036000,2986000,9882000,
6947000,5920000,26042000,22292000,5056000,20659000,1648000,
2533000,2667000,5113000,4112000]
result = calculate_statistics(array_of_values)

# Displaying the results
for key, value in result.items():
    print(f"{key}: {value}")
