from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.scrape_yt_explore import get_youtube_trending_api

def scrapeYoutubeTrendingData():
    trending_api_data = get_youtube_trending_api()
    print('Data--->', trending_api_data)

with DAG(dag_id="yt_trending_scraper_dag",
    start_date=datetime(2021,1,1),
    schedule_interval="*/5 * * * *",
    catchup=False) as dag:
    task1 = PythonOperator(
        task_id="yt_trending_scraper_dag",
        python_callable=scrapeYoutubeTrendingData)
