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
from bcreg.eventprocessor import EventProcessor
from bcreg.rocketchat_hooks import log_error, log_warning, log_info


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
    mara_db.config.databases \
        = lambda: {'mara': mara_db.dbs.PostgreSQLDB(user=mara_user, password=mara_password, host=mara_host, database=mara_database, port=mara_port)}

    (post_credential_pipeline, success) = data_integration.pipelines.find_node(['initialization_and_load_tasks','bc_reg_credential_poster']) 
    if success:
        creds_ct = 0
        with EventProcessor() as eventprocessor:
            creds_ct = eventprocessor.get_outstanding_creds_record_count()
        while 0 < creds_ct:
            run_pipeline(post_credential_pipeline)
            with EventProcessor() as eventprocessor:
                creds_ct = eventprocessor.get_outstanding_creds_record_count()
            log_info("Ran bc_reg_credential_poster for " + str(creds_ct) + " corps")
    else:
        print("Pipeline not found")
        log_error("Pipeline not found for:" + "bc_reg_credential_poster")
except Exception as e:
    print("Exception", e)
    log_error("bc_reg_credential_poster processing exception: " + str(e))
    raise
