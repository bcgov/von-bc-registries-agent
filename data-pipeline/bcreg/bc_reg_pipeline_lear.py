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
from bcreg.bcreg_lear import BCReg_Lear, lear_system_type
from bcreg.eventprocessor import EventProcessor
from bcreg.rocketchat_hooks import log_error, log_warning, log_info

MAX_CORPS = 10000
CRAZY_MAX_CORPS = 100000

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
    log_info("Starting bc_reg_event_processor ...")
    mara_db.config.databases \
        = lambda: {'mara': mara_db.dbs.PostgreSQLDB(user=mara_user, password=mara_password, host=mara_host, database=mara_database, port=mara_port)}

    (child_pipeline, success) = data_integration.pipelines.find_node(['bc_reg_event_processor_lear']) 
    if success:
        run_pipeline(child_pipeline)
        log_info("Ran bc_reg_event_processor - complete.")

        with EventProcessor() as eventprocessor:
            corps_ct = eventprocessor.get_outstanding_corps_record_count()
            if CRAZY_MAX_CORPS < corps_ct:
                log_error("bc-reg-pipeline More than cRaZy MaX corps outstanding: " + str(corps_ct))
            elif MAX_CORPS < corps_ct:
                log_warning("bc-reg-pipeline More than max corps outstanding: " + str(corps_ct))
    else:
        print("Pipeline not found")
        log_error("Pipeline not found for:" + "bc_reg_event_processor")
except Exception as e:
    print("Exception", e)
    log_error("bc_reg_event_processor processing exception: " + str(e))
    raise
