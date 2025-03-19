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

