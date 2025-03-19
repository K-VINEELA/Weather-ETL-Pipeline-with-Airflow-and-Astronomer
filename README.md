# 🌤️ **Weather ETL Pipeline with Airflow and Astronomer**

### 🚀 **Overview**
The **Weather ETL Pipeline** is an end-to-end automated pipeline built using **Apache Airflow** and **Astronomer**. It fetches real-time weather data from the **Open-Meteo API**, processes it, and loads it into a **PostgreSQL database** for future analysis or reporting. This pipeline is designed to run daily, ensuring your weather data is always up to date.

With this project, you can seamlessly integrate data extraction, transformation, and loading into your data pipeline with the flexibility and power of Airflow.

---

## **🛠️ Features**

### **Data Extraction**
- Fetches real-time weather data from the **Open-Meteo API** for a specific location (London, in this case).
- Uses **Airflow’s HttpHook** for smooth API integration and data retrieval.

### **Data Transformation**
- Extracts and formats weather data (temperature, wind speed, wind direction, and weather code).
- Structures data into a format ready for loading into a database.

### **Data Loading**
- Inserts transformed weather data into a **PostgreSQL** database using **Airflow's PostgresHook**.
- Ensures that the data is inserted into the correct table with a timestamp for tracking purposes.

### **Dockerized Development**
- The project runs in a **Dockerized environment**, allowing for easy local development and testing.
- Spin up all necessary containers with just one command using **Astronomer CLI**.

### **Airflow Scheduling**
- The pipeline is set to run daily, ensuring regular data updates and easy automation.

---

## **📝 Project Structure**

- **dags/**: Contains the **weather_etl_pipeline.py** DAG file, which defines the entire ETL process (Extract, Transform, Load).
- **Dockerfile**: Sets up the containerized environment for the project using Docker.
- **include/**: Folder reserved for any additional files (empty by default).
- **packages.txt**: Contains OS-level package installations, usually for system dependencies.
- **requirements.txt**: Lists the Python dependencies for the project, which can be installed using `pip`.
- **airflow_settings.yaml**: Airflow's connection settings and configurations for external services.
- **README.md**: The documentation for the project, including setup instructions and descriptions.


---

## 🚀 **Getting Started**

To get started with this project, follow the steps below to set up your local development environment and run the Airflow-based ETL pipeline.

### Prerequisites

Before you begin, make sure you have the following installed:

- **Docker**: For containerization of Airflow and its components.
- **Astronomer CLI**: For managing the local Airflow environment.
- **Python 3.x**: Ensure Python 3 is installed along with `pip` for package management.

If you don't have Docker or Astronomer CLI installed, follow the installation instructions on their respective official websites.

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/weather-etl-airflow-astro.git
cd weather-etl-airflow-astro
```

### Step 2: Install Dependencies

Install the Python dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Configure Airflow Connections

Before running the project, you'll need to configure the Airflow connections.

1. Open the Airflow UI at [http://localhost:8080/](http://localhost:8080/) (default Airflow web UI port).
2. Log in using the default credentials:
   - **Username**: `admin`
   - **Password**: `admin`
3. Navigate to **Admin > Connections** and create the following connections:
   - **open_meteo_api**: HTTP connection for accessing the Open-Meteo API.
     - Set the connection type as **HTTP** and input the base URL for the Open-Meteo API.
   - **postgres_default**: PostgreSQL connection for storing weather data.
     - Set the connection type as **Postgres** and provide the necessary connection details such as:
       - **Database host**
       - **Port**
       - **Username**
       - **Password**
## ⚡ **Running the Project Locally**

After setting up the Airflow connections, you're ready to start the project locally.

### Step 1: Start the Airflow Environment

Use the following command to start the Airflow environment using Docker and Astronomer CLI:

```bash
astro dev start
```

This command will start up the following containers:

- **Postgres**: Airflow's metadata database.
- **Webserver**: The Airflow UI for monitoring DAGs and tasks.
- **Scheduler**: Responsible for running the tasks defined in your DAG.
- **Triggerer**: Manages the triggering of deferred tasks.

---

### Step 2: Monitor the ETL Process

Once the environment is up, open the Airflow UI by navigating to [http://localhost:8080/](http://localhost:8080/) in your browser. You will be able to see the `weather_etl_pipeline` DAG listed under the **DAGs** tab.

You can trigger the DAG manually by clicking the play button next to the DAG name, or let it run according to the defined schedule (`@daily`).

The pipeline will fetch weather data from the Open-Meteo API, transform the data, and load it into the PostgreSQL database.

---

### Step 3: Verify Data in PostgreSQL

To verify the data, you can use any PostgreSQL client like **DBeaver** to connect to the database and check the data in the `weather_data` table. The table will contain the following columns:

- `latitude`
- `longitude`
- `temperature`
- `windspeed`
- `winddirection`
- `weathercode`
- `timestamp` (auto-generated)

---

## 🧑‍💻 **How It Works**

This ETL pipeline uses Apache Airflow to automate the data extraction, transformation, and loading process.

### **Extract:**
The `extract_weather_data` task fetches current weather data from the Open-Meteo API using Airflow's `HttpHook`. The API provides temperature, wind speed, and other weather-related data for a given latitude and longitude.

### **Transform:**
The `transform_weather_data` task processes the raw API data and transforms it into a structured format suitable for insertion into a PostgreSQL database.

### **Load:**
The `load_weather_data` task inserts the transformed data into the `weather_data` table in PostgreSQL using Airflow's `PostgresHook`.

This entire workflow is orchestrated by the `weather_etl_pipeline` DAG, which runs on a daily schedule (`@daily`).

---

## 🔧 **Customization**

This project is highly customizable. You can adjust the following aspects based on your needs:

- **Latitude and Longitude**: You can change the values of `LATITUDE` and `LONGITUDE` to fetch weather data for any location.
- **Schedule**: Modify the `schedule_interval` in the DAG definition to control how often the pipeline runs (e.g., `@hourly`, `@weekly`).
- **API Integration**: You can replace the Open-Meteo API with other weather data sources by adjusting the `HttpHook` configuration and the API endpoint.




