import os
from data_integration.pipelines import Pipeline, Task
from data_integration.ui.cli import run_pipeline
import mara_db.auto_migration
import mara_db.config
import mara_db.dbs
import data_integration
import data_integration.config
import logging

from mara_app.monkey_patch import patch
from bcreg.bcreg_pipelines import bc_reg_root_pipeline
from bcreg.eventprocessor import EventProcessor
from bcreg.rocketchat_hooks import log_error, log_warning, log_info

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'WARNING').upper()
logging.basicConfig(level=LOG_LEVEL)


patch(data_integration.config.system_statistics_collection_period)(lambda: 15)

@patch(data_integration.config.root_pipeline)
def root_pipeline():
    return bc_reg_root_pipeline()

mara_host = os.environ.get('MARA_DB_HOST', 'bcregdb')
mara_database = os.environ.get('MARA_DB_DATABASE', 'mara_db')
mara_port = os.environ.get('MARA_DB_PORT', '5432')
mara_user = os.environ.get('MARA_DB_USER', 'mara_db')
mara_password = os.environ.get('MARA_DB_PASSWORD')

try:
    log_info("Starting bc_reg_bn_loader ...")
    mara_db.config.databases \
        = lambda: {'mara': mara_db.dbs.PostgreSQLDB(user=mara_user, password=mara_password, host=mara_host, database=mara_database, port=mara_port)}

    (child_pipeline, success) = data_integration.pipelines.find_node(['initialization_and_load_tasks', 'bc_reg_bn_loader']) 
    if success:
        run_pipeline(child_pipeline)
        log_info("Ran bc_reg_bn_loader - complete.")
    else:
        print("Pipeline not found")
        log_error("Pipeline not found for:" + "bc_reg_bn_loader")
except Exception as e:
    print("Exception", e)
    log_error("bc_reg_bn_loader processing exception: " + str(e))
    raise
