from data_integration.commands.bash import RunBash
from data_integration.commands.python import ExecutePython
from data_integration.pipelines import Pipeline, Task
from data_integration.ui.cli import run_pipeline, run_interactively
from data_integration.ui.cli import run_pipeline
import mara_db.auto_migration
import mara_db.config
import mara_db.dbs
import data_integration
from bcreg.bcreg_pipelines import db_init_pipeline

mara_db.config.databases \
    = lambda: {'mara': mara_db.dbs.PostgreSQLDB(host='localhost', port='5444', user='mara_db', database='mara_db')}

parent_pipeline = Pipeline(
    id = 'holder_for_pipeline_versions',
    description = 'Holder for the different versions of the BC Registries pipeline.')

parent_pipeline.add(db_init_pipeline())

run_pipeline(parent_pipeline)
