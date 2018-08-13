import os
from data_integration.pipelines import Pipeline, Task
from data_integration.ui.cli import run_pipeline
import mara_db.auto_migration
import mara_db.config
import mara_db.dbs
import data_integration
from bcreg.bcreg_pipelines import bc_reg_pipeline_jsonbender

mara_host = os.environ.get('MARA_DB_HOST', 'bcregdb')
mara_database = os.environ.get('MARA_DB_DATABASE', 'mara_db')
mara_port = os.environ.get('MARA_DB_PORT', '5432')
mara_user = os.environ.get('MARA_DB_USER', 'mara_db')
mara_password = os.environ.get('MARA_DB_PASSWORD')

mara_db.config.databases \
    = lambda: {'mara': mara_db.dbs.PostgreSQLDB(user=mara_user, password=mara_password, host=mara_host, database=mara_database, port=mara_port)}

parent_pipeline = Pipeline(
    id = 'holder_for_pipeline_versions',
    description = 'Holder for the different versions of the BC Registries pipeline.')

parent_pipeline.add(bc_reg_pipeline_jsonbender())

run_pipeline(parent_pipeline)


