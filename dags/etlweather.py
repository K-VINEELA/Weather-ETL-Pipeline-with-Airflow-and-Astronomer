from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago

# Define multiple locations (City, Latitude, Longitude)
LOCATIONS = [
    ("London", "51.5074", "-0.1278"),
    ("New York", "40.7128", "-74.0060"),
    ("Tokyo", "35.6895", "139.6917"),
    ("Sydney", "-33.8688", "151.2093")
]

POSTGRES_CONN_ID = 'postgres_default'
API_CONN_ID = 'open_meteo_api'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1)
}

with DAG(dag_id='weather_etl_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    @task()
    def extract_weather_data(city, latitude, longitude):
        """Extract weather data from Open-Meteo API."""
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')
        endpoint = f'/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
        response = http_hook.run(endpoint)

        if response.status_code == 200:
            data = response.json()
            return {'city': city, **data['current_weather']}
        else:
            raise Exception(f"Failed to fetch weather data for {city}: {response.status_code}")

    @task()
    def transform_weather_data(weather_data):
        """Transform the extracted weather data."""
        transformed_data = {
            'city': weather_data['city'],
            'temperature': weather_data['temperature'],
            'windspeed': weather_data['windspeed'],
            'winddirection': weather_data['winddirection'],
            'weathercode': weather_data['weathercode']
        }
        return transformed_data
@task()
def load_weather_data(transformed_data):
    """Load transformed data into PostgreSQL."""
    try:
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        # Ensure the table exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            latitude FLOAT,
            longitude FLOAT,
            temperature FLOAT,
            windspeed FLOAT,
            winddirection FLOAT,
            weathercode INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Insert transformed data into the table
        cursor.execute("""
        INSERT INTO weather_data (latitude, longitude, temperature, windspeed, winddirection, weathercode)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            transformed_data['latitude'],
            transformed_data['longitude'],
            transformed_data['temperature'],
            transformed_data['windspeed'],
            transformed_data['winddirection'],
            transformed_data['weathercode']
        ))

        conn.commit()
        cursor.close()
        return f"Data for {transformed_data['latitude']}, {transformed_data['longitude']} loaded successfully!"

    except Exception as e:
        # If any error occurs, log and raise it
        print(f"Error loading data: {e}")
        raise Exception(f"Failed to load weather data: {e}")


    # Dynamically generate tasks for multiple locations
    weather_data_tasks = [extract_weather_data(city, lat, lon) for city, lat, lon in LOCATIONS]
    
    # Transform and load the data for each location
    for weather_data in weather_data_tasks:
        transformed_data = transform_weather_data(weather_data)
        load_weather_data(transformed_data)
