rm -r /home/airflow_exec/airflow-medium/dags
mkdir /home/airflow_exec/airflow-medium/dags
gsutil cp -A gs://airflow-dags-sd/dags/* /home/airflow_exec/airflow-medium/dags

rm -r /home/airflow_exec/airflow-medium/plugins
mkdir /home/airflow_exec/airflow-medium/plugins
gsutil cp -A gs://airflow-dags-sd/plugins/* /home/airflow_exec/airflow-medium/plugins