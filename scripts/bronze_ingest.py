import requests
import json
from datetime import datetime
from pathlib import Path

URL = "https://opensky-network.org/api/states/all"

def run_bronze_ingestion(**context):
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    data = response.json()

    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")

    bronze_dir = Path("/opt/airflow/data/bronze")
    
    # Ensure directory exists
    bronze_dir.mkdir(parents=True, exist_ok=True)

    path = bronze_dir / f"flights_{timestamp}.json"


    with open(path, "w") as f:
        json.dump(data, f)
    
    context["ti"].xcom_push(key="bronze_file", value=str(path))

    