import pandas as pd

# Assuming 'generate_car_matrix' is the function from Question 1
def generate_car_matrix(dataframe):
    pivot_df = dataframe.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = pivot_df.fillna(0)
    return car_matrix

def unroll_distance_matrix(distance_matrix):
    # Reset the index to convert the matrix into a DataFrame
    distance_df = distance_matrix.stack().reset_index()
    
    # Rename the columns to match the desired output
    distance_df.columns = ['id_start', 'id_end', 'distance']
    
    return distance_df

df = pd.read_csv("C:\Downloads\dataset-1.csv")

# Generate the car matrix using the previous function
result_matrix = generate_car_matrix(df)

# Call the function to unroll the distance matrix
unrolled_df = unroll_distance_matrix(result_matrix)

# Print the resulting DataFrame
print(unrolled_df)
