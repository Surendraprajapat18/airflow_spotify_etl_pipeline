from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_etl import run_spotify_etl



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 21),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='My firstl etl code',
    schedule_interval=timedelta(days=1),
)


run_etl = PythonOperator(
    task_id='Spotify_elt_pipeline',
    python_callable=run_spotify_etl,
    dag=dag,
)

run_etl