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

create_token = BashOperator(
    task_id='reddit_create_token',
    dag=dag,
    bash_command="cd /home/airflow_exec/airflow-medium/plugins;python -c 'import "
                 "reddit_token;print(reddit_token.create_token())'",
    do_xcom_push=True
)

get_subreddit_list = BashOperator(
    task_id="get_subreddits_list",
    dag=dag,
    bash_command="echo `python '/home/airflow_exec/airflow-medium/plugins/read_from_db.py'`",
    do_xcom_push=True
)

create_token >> get_subreddit_list

if __name__ == "__main__":
    dag.cli()
