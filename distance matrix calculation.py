import pandas as pd

def calculate_distance_matrix(dataframe):
    # Create a DataFrame with unique toll locations
    toll_locations = pd.unique(dataframe[['toll_booth_A', 'toll_booth_B']].values.ravel('K'))
    distance_matrix = pd.DataFrame(index=toll_locations, columns=toll_locations)
    
    # Initialize the matrix with zeros
    distance_matrix = distance_matrix.fillna(0)
    
    # Update the matrix with cumulative distances along known routes
    for index, row in dataframe.iterrows():
        toll_A = row['toll_booth_A']
        toll_B = row['toll_booth_B']
        distance = row['distance']
        
        # Update the matrix with bidirectional distances
        distance_matrix.at[toll_A, toll_B] += distance
        distance_matrix.at[toll_B, toll_A] += distance
    
    return distance_matrix

df = pd.read_csv("C:\Downloads\dataset-3.csv")

# Call the function with the DataFrame
result_matrix = calculate_distance_matrix(df)

# Print the resulting distance matrix
print(result_matrix)
