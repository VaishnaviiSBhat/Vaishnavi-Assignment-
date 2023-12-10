import pandas as pd

def generate_car_matrix(df: pd.DataFrame) -> pd.DataFrame:
    return df[['id_1', 'id_2', 'car']].pivot(index='id_1', columns='id_2', values='car').fillna(0)

def get_type_count(df: pd.DataFrame) -> dict:
    car_type_counts = df['car'].apply(lambda x: 'low' if x <= 15 else ('medium' if x <= 25 else 'high'))
    return car_type_counts.value_counts().to_dict()

def get_bus_indexes(df: pd.DataFrame) -> list:
    mean_bus_value = df['bus'].mean()
    return df[df['bus'] > 2 * mean_bus_value].index.tolist()

def filter_routes(df: pd.DataFrame) -> list:
    average_truck_values = df.groupby('route')['truck'].mean()
    return average_truck_values[average_truck_values > 7].index.tolist()

def multiply_matrix(matrix: pd.DataFrame) -> pd.DataFrame:
    return matrix * 2

def time_check(df: pd.DataFrame) -> pd.Series:
    if 'timestamp' in df.columns:
        return df['timestamp'].between_time('00:00', '23:59').groupby(['id', 'id_2']).apply(lambda x: x.shape[0] == 24 * 7)
    else:
        return pd.Series()

# Load dataset-1
file_path1 = '../datasets/dataset-1.csv'
df1 = pd.read_csv(file_path1)

# Load dataset-2
file_path2 = '../datasets/dataset-2.csv'
df2 = pd.read_csv(file_path2)

# Apply the functions
result_matrix = generate_car_matrix(df1)
car_type_counts = get_type_count(df1)
bus_indexes = get_bus_indexes(df1)
filtered_routes = filter_routes(df1)
multiplied_matrix = multiply_matrix(result_matrix)
time_completeness = time_check(df2)

# Display the results
print("Generated Car Matrix:")
print(result_matrix)

print("\nCar Type Counts:")
print(car_type_counts)

print("\nBus Indexes:")
print(bus_indexes)

print("\nFiltered Routes:")
print(filtered_routes)

print("\nMultiplied Matrix:")
print(multiplied_matrix)

print("\nTime Completeness:")
print(time_completeness)
