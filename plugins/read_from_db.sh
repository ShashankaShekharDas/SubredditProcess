gsutil rm gs://reddit-info/Subreddit/subreddit.csv
gcloud sql export csv reddit-managed-storage gs://reddit-info/Subreddit/subreddit.csv --query='SELECT * FROM reddit.subreddits;'
gsutil cp -A gs://reddit-info/Subreddit/subreddit.csv /home/airflow_exec/airflow-medium/data/subreddit.csv
