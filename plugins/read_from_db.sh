gsutil rm gs://reddit-info/Subreddit/subreddit.csv
gcloud sql export csv reddit-managed-storage gs://reddit-info/Subreddit/subreddit.csv --query='SELECT * FROM reddit.subreddits;'
gsutil cp -A gs://reddit-info/Subreddit/subreddit.csv /home/airflow_exec/airflow-medium/data/subreddit.csv
#Added column name to the file for easier accessing
echo 'subreddit_name,start_post\n' | cat - /home/airflow_exec/airflow-medium/data/subreddit.csv > temp && mv temp /home/airflow_exec/airflow-medium/data/subreddit.csv