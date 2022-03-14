from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.scrape_yt_explore import get_youtube_trending_api

def helloWorld():
    trending_api_data = get_youtube_trending_api()
    print('Data--->', trending_api_data)

with DAG(dag_id="hello_world_dag_adi",
    start_date=datetime(2021,1,1),
    schedule_interval="*/1 * * * *",
    catchup=False) as dag:
    task1 = PythonOperator(
        task_id="hello_world",
        python_callable=helloWorld)
