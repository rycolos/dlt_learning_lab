# Sample data containing pokemon details
import dlt, duckdb, pandas

data = [
    {"id": "1", "name": "bulbasaur", "size": {"weight": 6.9, "height": 0.7}},
    {"id": "4", "name": "charmander", "size": {"weight": 8.5, "height": 0.6}},
    {"id": "25", "name": "pikachu", "size": {"weight": 6, "height": 0.4}},
]

# Set pipeline name, destination, and dataset name
my_pipeline = dlt.pipeline(
    pipeline_name="quick_start",
    destination="duckdb",
    dataset_name="mydata",
)

# Run the pipeline with data and table name
_load_info = my_pipeline.run(data, table_name="pokemon")
print(_load_info)

# A database '<pipeline_name>.duckdb' was created in working directory so just connect to it

# Connect to the DuckDB database
conn = duckdb.connect(f"{my_pipeline.pipeline_name}.duckdb")

# Set search path to the dataset
conn.sql(f"SET search_path = '{my_pipeline.dataset_name}'")

# Describe the dataset
print(conn.sql("DESCRIBE").df())

# Fetch all data from 'pokemon' as a DataFrame
table = conn.sql("SELECT * FROM pokemon").df()

# Display the DataFrame
print(table)

# Query data from 'pokemon' using the SQL client
with my_pipeline.sql_client() as client:
    with client.execute_query("SELECT * FROM pokemon") as cursor:
        data_1 = cursor.df()
# Display the data
print(data_1)

dataset = my_pipeline.dataset()
exercise_df = dataset.pokemon.df()

print(f'{(len(exercise_df.columns))} columns in dataframe')