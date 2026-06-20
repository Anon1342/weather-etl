# Weather ETL with Prefect Scheduling

Fetches daily weather data from the Open-Meteo API, transforms the JSON into a DataFrame, and loads it into BigQuery. The raw data is modeled using dbt and the mart layer is connected to Looker Studio for visualization. The entire workflow is automated using Prefect, running daily at 9 AM.

## Tech Stack

- **Python** - For writing the script/code
- **Open-Meteo API** - For extracting the daily weather data
- **Pandas** - for transforming the json into a DataFrame
- **BigQuery** - as the cloud data warehouse for storing and querying transformed data
- **dbt** - to model the data
- **Looker Studio** - to visualize the data
- **Prefect** - to orchestrate the workflows
- **GitHub** - for version control and storing the code


## Architecture
```
Open-Meteo API → extract.py → transform.py → load_bq.py → BigQuery → dbt → Looker Studio
                                    ↑
                            Orchestrated by Prefect
```

## How To Run

1. `git clone <repo-url>`
2. `python -m venv env_1`
3. `env_1\Scripts\activate`
4. `pip install -r requirements.txt`
5.  Create .env file and add GOOGLE_APPLICATION_CREDENTIALS=credentials.json
6.  Place your credentials.json file in the project folder
7. `python pipeline_prefect.py`
8. `cd weather_dbt`
9. `dbt run`
10.`prefect deploy pipeline_prefect.py:prefect_pipeline` (for scheduling)

## Dashboard
Built using Looker Studio connected to the dbt mart layer in BigQuery.
Includes a heatmap table and average temperature trend line for Kathmandu.
