import os
from data_integration.pipelines import Pipeline, Task
from data_integration.ui.cli import run_pipeline
import mara_db.auto_migration
import mara_db.config
import mara_db.dbs
import data_integration
import data_integration.config
from mara_app.monkey_patch import patch
from bcreg.bcreg_pipelines import bc_reg_root_pipeline


patch(data_integration.config.system_statistics_collection_period)(lambda: 15)

@patch(data_integration.config.root_pipeline)
def root_pipeline():
    return bc_reg_root_pipeline()

mara_host = os.environ.get('MARA_DB_HOST', 'bcregdb')
mara_database = os.environ.get('MARA_DB_DATABASE', 'mara_db')
mara_port = os.environ.get('MARA_DB_PORT', '5432')
mara_user = os.environ.get('MARA_DB_USER', 'mara_db')
mara_password = os.environ.get('MARA_DB_PASSWORD')

mara_db.config.databases \
    = lambda: {'mara': mara_db.dbs.PostgreSQLDB(user=mara_user, password=mara_password, host=mara_host, database=mara_database, port=mara_port)}

(populate_audit_table_pipeline, success) = data_integration.pipelines.find_node(['bc_reg_populate_audit_table']) 
if success:
	run_pipeline(populate_audit_table_pipeline)
else:
	print("Pipeline not found")
