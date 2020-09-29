import airflow
from .rbor_dag.dag import meta_wrapper
airflow.lineage.apply_lineage = meta_wrapper


from datetime import timedelta
import datetime
import logging
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.lineage.datasets import DataSet
import airflow

from rbor_dag.dag import MetaDAG
from rbor_dag.dumb_op import DumbOp
from airflow.utils.dates import days_ago



default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with MetaDAG(
    "sample1",
    default_args=default_args,
    description="A simple Subclassed DAG",
    schedule_interval=timedelta(days=1),
) as dag:
    t1 = DumbOp(task_id="t1")

    t2 = DumbOp(task_id="t2")
    
    
t1 >> t2

logging.info(dag.task_dict)