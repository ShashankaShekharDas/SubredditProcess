from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'Shashanka',
}

dag = DAG(
    dag_id='Reddit-Scrape',
    default_args=args,
    schedule_interval='0 * * * *',
    start_date=days_ago(2),
    dagrun_timeout=timedelta(minutes=60),
    tags=['reddit', 'scrape']
)

task1 = BashOperator(
    task_id='reddit_create_token',
    dag=dag,
    bash_command="python '../plugins/reddit_token.py"
)

task1

if __name__ == "__main__":
    dag.cli()
