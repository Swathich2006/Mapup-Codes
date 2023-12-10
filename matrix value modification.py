import pandas as pd

# Assuming 'generate_car_matrix' is the function from Question 1
def generate_car_matrix(dataframe):
    pivot_df = dataframe.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = pivot_df.fillna(0)
    return car_matrix

def multiply_matrix(result_matrix):
    # Iterate over each element in the DataFrame and modify its value
    for index, row in result_matrix.iterrows():
        for column in result_matrix.columns:
            # Modify each value according to your specific logic
            result_matrix.at[index, column] *= 2  # Example: Multiply each value by 2
    
    return result_matrix

# Assuming 'dataset-1.csv' is your input CSV file
file_path = 'dataset-1.csv'
# Read the CSV into a DataFrame
df = pd.read_csv("C:\Downloads\dataset-1.csv")

# Generate the car matrix using the previous function
result_matrix = generate_car_matrix(df)

# Call the function to modify the matrix
modified_matrix = multiply_matrix(result_matrix)

# Print the modified matrix
print(modified_matrix)
