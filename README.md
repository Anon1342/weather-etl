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

## How To Run(Docker)
1.`git clone <repo-url>`
2. install docker(https://docs.docker.com/get-docker/)
3. Obtain credentials.json from GCP and place it in the project folder
4. Copy .env.example to .env and fill in your values
5. Copy profiles.yml.example to profiles.yml and fill in your values
6. `docker build -t weather-etl .`
7. `docker run -v "path\to\your\project\.env:/app/.env"  -v "path\to\your\project\profiles.yml:/app/profiles.yml" -v "path\to\your\project\credentials.json:/app/credentials.json" weather-etl`





```



## Dashboard
Built using Looker Studio connected to the dbt mart layer in BigQuery.
Includes a heatmap table and average temperature trend line for Kathmandu.
