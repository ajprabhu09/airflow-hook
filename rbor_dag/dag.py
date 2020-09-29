from airflow import DAG
import functools
import logging
import airflow.lineage as al
from airflow.operators import BaseOperator
from airflow.utils.decorators import apply_defaults




def meta_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        logging.info(f"SENDING TO METADATA API{args},\n\n {kwargs}")
        ret = func(*args,**kwargs)
        if ret:
            logging.info(f"Sending to RBOR Retrun{ret}");
            return ret
    return al.apply_lineage(wrapper)








class MetaDAG(DAG):
    def __init__(self,*args,**kwargs):
        super(MetaDAG,self).__init__(*args,**kwargs)

    def create_dagrun(self,*args,**kwargs):
        return super(MetaDAG,self).create_dagrun(*args,**kwargs)

    def simple(self):
        pass


