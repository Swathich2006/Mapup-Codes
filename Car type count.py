mport pandas as pd

def get_type_count(dataframe):
    # Create a dictionary mapping car values to car types
    car_type_mapping = {
        'sedan': 'Type A',
        'SUV': 'Type B',
        'truck': 'Type C',
        # Add more mappings as needed
    }
    
    # Create a new column 'car_type' based on the mapping
    dataframe['car_type'] = dataframe['car'].map(car_type_mapping)
    
    # Count the occurrences of each car type
    type_count = dataframe['car_type'].value_counts()
    
    return dataframe, type_count

# Assuming 'dataset-1.csv' is your input CSV file
df = pd.read_csv("C:\Downloads\dataset-1.csv")

# Call the function with the DataFrame
df_with_types, type_count = get_type_count(df)

# Print the DataFrame with the new 'car_type' column
print(df_with_types)

# Print the count of each car type
print(type_count)
