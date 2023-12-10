import pandas as pd

# Assuming 'generate_car_matrix' is the function from Question 1
def generate_car_matrix(dataframe):
    pivot_df = dataframe.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = pivot_df.fillna(0)
    return car_matrix

def calculate_toll_rate(car_matrix):
    # Define toll rates based on vehicle types
    toll_rates = {
        'Type A': 5,  # Replace with your specific toll rate for Type A vehicles
        'Type B': 7,  # Replace with your specific toll rate for Type B vehicles
        'Type C': 10  # Replace with your specific toll rate for Type C vehicles
        # Add more types and rates as needed
    }
    
    # Map car types to toll rates
    toll_matrix = car_matrix.applymap(lambda car_type: toll_rates.get(car_type, 0))
    
    return toll_matrix


df = pd.read_csv("C:\Downloads\dataset-1.csv")

# Generate the car matrix using the previous function
result_matrix = generate_car_matrix(df)

# Call the function to calculate toll rates
toll_matrix = calculate_toll_rate(result_matrix)

# Print the resulting toll matrix
print(toll_matrix)
