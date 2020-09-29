from airflow.lineage import apply_lineage
from airflow.operators import BaseOperator
from airflow.utils.decorators import apply_defaults


class DumbOp(BaseOperator):
    
    ui_color = '#e8f7e4'

    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(DumbOp, self).__init__(*args, **kwargs)


    @apply_lineage
    def post_execute(self,context,result=None):
        pass

    def execute(self, context):
        pass

