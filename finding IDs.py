import pandas as pd

# Assuming 'generate_car_matrix' is the function from Question 1
def generate_car_matrix(dataframe):
    pivot_df = dataframe.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = pivot_df.fillna(0)
    return car_matrix

def unroll_distance_matrix(distance_matrix):
    distance_df = distance_matrix.stack().reset_index()
    distance_df.columns = ['id_start', 'id_end', 'distance']
    return distance_df

def find_ids_within_ten_percentage_threshold(distance_df, reference_value):
    # Filter rows where the 'distance' column is within 10% of the reference value
    threshold_percentage = 10
    lower_threshold = reference_value * (1 - threshold_percentage / 100)
    upper_threshold = reference_value * (1 + threshold_percentage / 100)
    
    result_df = distance_df[(distance_df['distance'] >= lower_threshold) & (distance_df['distance'] <= upper_threshold)]
    
    return result_df


df = pd.read_csv("C:\Downloads\dataset-1.csv")

# Generate the car matrix using the previous function
result_matrix = generate_car_matrix(df)

# Call the function to unroll the distance matrix
unrolled_df = unroll_distance_matrix(result_matrix)

# Choose a reference value from the 'id_start' column (replace 1 with your desired reference value)
reference_value = 1

# Call the function to find rows within 10% threshold
result_within_threshold = find_ids_within_ten_percentage_threshold(unrolled_df, reference_value)

# Print the resulting DataFrame
print(result_within_threshold)
