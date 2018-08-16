"""Configures the data integration pipelines of the project"""

import datetime
import functools

import data_integration.config
from data_integration.pipelines import Pipeline, Task
from mara_app.monkey_patch import patch

import app.config

from bcreg.bcreg_pipelines import db_init_pipeline, bc_reg_pipeline, bc_reg_pipeline_status, bc_reg_pipeline_load_active, bc_reg_pipeline_load_historical
from bcreg.bcreg_pipelines import bc_reg_test_corps, bc_reg_pipeline_jsonbender

patch(data_integration.config.data_dir)(lambda: app.config.data_dir())
patch(data_integration.config.first_date)(lambda: app.config.first_date())
patch(data_integration.config.default_db_alias)(lambda: 'dwh')


@patch(data_integration.config.root_pipeline)
@functools.lru_cache(maxsize=None)
def root_pipeline():

    parent_pipeline = Pipeline(
        id = 'holder_for_pipeline_versions',
        description = 'Holder for the different versions of the BC Registries pipeline.')

    parent_pipeline.add(bc_reg_pipeline())
    parent_pipeline.add(bc_reg_pipeline_status())
    parent_pipeline.add(bc_reg_pipeline_load_active())
    parent_pipeline.add(bc_reg_pipeline_load_historical())
    parent_pipeline.add(db_init_pipeline())

    test_pipeline = Pipeline(
        id = 'test_and_demo_tasks',
        description = 'Holder for test and demo tasks.')

    test_pipeline.add(bc_reg_test_corps())
    test_pipeline.add(bc_reg_pipeline_jsonbender())

    parent_pipeline.add(test_pipeline)

    return parent_pipeline

