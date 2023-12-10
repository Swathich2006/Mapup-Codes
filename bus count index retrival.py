import pandas as pd

def get_bus_indexes(dataframe):
    # Calculate the mean value of the 'bus' column
    bus_mean = dataframe['bus'].mean()
    
    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = dataframe[dataframe['bus'] > 2 * bus_mean].index.tolist()
    
    # Sort the indices in ascending order
    bus_indexes.sort()
    
    return bus_indexes

# Read the CSV into a DataFrame
df = pd.read_csv("C:\Downloads\dataset-1.csv")

# Call the function with the DataFrame
result_indexes = get_bus_indexes(df)

# Print the list of indices
print(result_indexes)
