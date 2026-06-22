# Weather ETL with Prefect Scheduling

Fetches daily weather data from the Open-Meteo API, transforms the JSON into a DataFrame, and loads it into BigQuery. The raw data is modeled using dbt and the mart layer is connected to Looker Studio for visualization. The entire workflow is automated using Prefect, running daily at 9 AM.

## Tech Stack

- **Python** - For writing the script/code
- **Open-Meteo API** - For extracting the daily weather data
- **Pandas** - For transforming the json into a DataFrame
- **BigQuery** - As the cloud data warehouse for storing and querying transformed data
- **dbt** - To model the data
- **Looker Studio** - to visualize the data
- **Prefect** - To orchestrate the workflows
- **GitHub** - For version control and storing the code
- **Docker** - Used for containerizing the project, enabling it to run anywhere without dependency issue
- **GitHub Actions** - Used for CI/CD. The docker image automatically gets pushed to Docker Hub when the code is pushed to GitHub repo


## Architecture
```
        Open-Meteo API → [Docker Container: extract.py → transform.py → load_bq.py → dbt] → BigQuery → Looker Studio
                           ↑
                    Orchestrated by Prefect

Note: load_bq.py writes to BigQuery; dbt reads and writes back to BigQuery
 ```

## How To Run (Docker)
1.`git clone https://github.com/Anon1342/weather-etl.git`
2. install docker(https://docs.docker.com/get-docker/)
3. Obtain credentials.json from GCP and place it in the project folder
4. Copy .env.example to .env and fill in your values
5. Copy profiles.yml.example to profiles.yml and fill in your values
6. `docker-compose up`


## Dashboard
Built using Looker Studio connected to the dbt mart layer in BigQuery.
Includes a heatmap table and average temperature trend line for Kathmandu.
