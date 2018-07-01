from data_integration.pipelines import Pipeline, Task
from data_integration.ui.cli import run_pipeline
import mara_db.auto_migration
import mara_db.config
import mara_db.dbs
import data_integration
from bcreg.bcreg_pipelines import bc_reg_pipeline_jsonbender

mara_db.config.databases \
    = lambda: {'mara': mara_db.dbs.PostgreSQLDB(host='localhost', port=5444, user='mara_db', database='mara_db')}


parent_pipeline = Pipeline(
    id = 'holder_for_pipeline_versions',
    description = 'Holder for the different versions of the BC Registries pipeline.')

parent_pipeline.add(bc_reg_pipeline_jsonbender())

run_pipeline(parent_pipeline)


