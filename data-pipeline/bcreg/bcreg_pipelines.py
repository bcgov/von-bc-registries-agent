from data_integration.pipelines import Pipeline, Task
from data_integration.commands.python import ExecutePython

def bc_reg_root_pipeline():
    import bcreg

    parent_pipeline = Pipeline(
        id = 'holder_for_pipeline_versions',
        description = 'Holder for the different versions of the BC Registries pipeline.')

    parent_pipeline.add(bc_reg_pipeline())
    parent_pipeline.add(bc_reg_pipeline_status())

    init_pipeline = Pipeline(
        id = 'initialization_and_load_tasks',
        description = 'One-time initialization and data load tasks')

    init_pipeline.add(db_init_pipeline())
    init_pipeline.add(bc_reg_pipeline_initial_load())
    init_pipeline.add(bc_reg_pipeline_post_credentials())

    parent_pipeline.add(init_pipeline)

    test_pipeline = Pipeline(
        id = 'test_and_demo_tasks',
        description = 'Holder for test and demo tasks.')

    test_pipeline.add(bc_init_test_data())
    test_pipeline.add(bc_reg_test_corps())
    test_pipeline.add(bc_reg_pipeline_single_thread())
    test_pipeline.add(bc_reg_pipeline_jsonbender())

    parent_pipeline.add(test_pipeline)

    return parent_pipeline

def bc_reg_pipeline():
    import bcreg

    pipeline1 = Pipeline(
        id='bc_reg_event_processor',
        description='A pipeline that processes BC Registries events and generates credentials.')

    sub_pipeline1_2 = Pipeline(id='load_and_process_bc_reg_data', description='Load BC Reg data and generate credentials')
    sub_pipeline1_2.add(Task(id='register_un_processed_events', description='Register un-processed events',
                          commands=[ExecutePython('./bcreg/find-unprocessed-events.py')]))
    sub_pipeline1_2.add(Task(id='load_bc_reg_data', description='Load BC Registries data',
                          commands=[ExecutePython('./bcreg/process-corps-generate-creds.py')]), ['register_un_processed_events'])
    sub_pipeline1_2.add(Task(id='create_bc_reg_credentials', description='Create credentials',
                          commands=[ExecutePython('./bcreg/generate-creds.py')]), ['load_bc_reg_data'])
    pipeline1.add(sub_pipeline1_2)

    sub_pipeline1_3 = Pipeline(id='submit_bc_reg_credentials', description='Submit BC Reg credentials to P-X')
    sub_pipeline1_3.add(Task(id='submit_credentials', description='Submit credentials',
                          commands=[ExecutePython('./bcreg/submit-creds.py')]))
    pipeline1.add(sub_pipeline1_3, ['load_and_process_bc_reg_data'])

    sub_pipeline1_4 = Pipeline(id='populate_evp_audit_table', description='Populate Event Processor Audit Table')
    sub_pipeline1_4.add(Task(id='populate_audit_table', description='Populate Audit Table',
                          commands=[ExecutePython('./bcreg/populate_audit_table.py')]))
    pipeline1.add(sub_pipeline1_4, ['submit_bc_reg_credentials'])

    return pipeline1

def bc_reg_pipeline_single_thread():
    import bcreg

    pipeline1 = Pipeline(
        id='bc_reg_event_processor_single_thread',
        description='A pipeline that processes BC Registries events and generates credentials.')

    sub_pipeline1_2 = Pipeline(id='load_and_process_bc_reg_data_single_thread', description='Load BC Reg data and generate credentials')
    sub_pipeline1_2.add(Task(id='register_un_processed_events_single_thread', description='Register un-processed events',
                          commands=[ExecutePython('./bcreg/find-unprocessed-events.py')]))
    sub_pipeline1_2.add(Task(id='load_bc_reg_data_single_thread', description='Load BC Registries data',
                          commands=[ExecutePython('./bcreg/register_un_processed_events')]), ['register_un_processed_events_single_thread'])
    pipeline1.add(sub_pipeline1_2)

    sub_pipeline1_3 = Pipeline(id='submit_bc_reg_credentials_single_thread', description='Submit BC Reg credentials to P-X')
    sub_pipeline1_3.add(Task(id='submit_credentials_single_thread', description='Submit credentials',
                          commands=[ExecutePython('./bcreg/submit-creds-single-thread.py')]))
    pipeline1.add(sub_pipeline1_3, ['load_and_process_bc_reg_data_single_thread'])

    return pipeline1

def bc_reg_pipeline_initial_load():
    import bcreg

    pipeline1 = Pipeline(
        id='bc_reg_corp_loader',
        description='A pipeline that does the initial data load and credentials for all corporations.')

    sub_pipeline1_2 = Pipeline(id='load_and_process_bc_reg_corps', description='Load Active BC Reg corps and generate credentials')
    sub_pipeline1_2.add(Task(id='register_un_processed_corps', description='Register un-processed active corps',
                          commands=[ExecutePython('./bcreg/find-unprocessed-corps_actve.py')]))
    sub_pipeline1_2.add(Task(id='load_bc_reg_data_a', description='Load BC Registries data',
                          commands=[ExecutePython('./bcreg/process-corps-generate-creds.py')]), ['register_un_processed_corps'])
    pipeline1.add(sub_pipeline1_2)

    return pipeline1

def bc_reg_pipeline_post_credentials():
    import bcreg

    pipeline1 = Pipeline(
        id='bc_reg_credential_poster',
        description='A pipeline that posts generated credentials to TOB.')

    sub_pipeline1_3 = Pipeline(id='submit_bc_reg_credentials_a', description='Submit BC Reg credentials to P-X')
    sub_pipeline1_3.add(Task(id='submit_credentials_a', description='Submit credentials',
                          commands=[ExecutePython('./bcreg/submit-creds.py')]))
    pipeline1.add(sub_pipeline1_3)

    sub_pipeline1_4 = Pipeline(id='populate_evp_audit_table_a', description='Populate Event Processor Audit Table')
    sub_pipeline1_4.add(Task(id='populate_audit_table_a', description='Populate Audit Table',
                          commands=[ExecutePython('./bcreg/populate_audit_table.py')]))
    pipeline1.add(sub_pipeline1_4, ['submit_bc_reg_credentials_a'])

    return pipeline1

def bc_reg_pipeline_status():
    import bcreg

    pipeline = Pipeline(
        id='bc_reg_pipeline_status',
        description='Display overall event processing status.')

    pipeline.add(Task(id='display_pipeline_status', description='Display status of the overall pipeline processing status',
                        commands=[ExecutePython('./bcreg/display_pipeline_status.py')]))
    # remove these from the pipeline due to issues connecting to DB's on openshift
    #pipeline.add(Task(id='display_pipeline_stats', description='Display stats of each stage in the pipeline processing',
    #                    commands=[ExecutePython('./bcreg/display_processed_corps_counts.py')]))
    pipeline.add(Task(id='display_event_processor_stats', description='Display stats of each event processor stage',
                        commands=[ExecutePython('./bcreg/display_event_processor_counts.py')]))

    return pipeline

def db_init_pipeline():
    import bcreg

    pipeline = Pipeline(
      id = 'bc_reg_db_init',
      description = 'Initialize BC Registries Event Processor database')

    pipeline.add(Task(id='create_tables', description='Create event processing tables',
                        commands=[ExecutePython('./bcreg/create.py')]))
    pipeline.add(Task(id='initialize_tables', description='Insert configuration data',
                        commands=[ExecutePython('./bcreg/insert.py')]), ['create_tables'])

    return pipeline

def bc_init_test_data():
    import bcreg

    pipeline = Pipeline(
        id='bc_reg_test_data',
        description='A pipeline that initializes event processor database for testing.')

    pipeline.add(Task(id='register_test_corps', description='Insert some test data for processing',
                        commands=[ExecutePython('./bcreg/insert-test.py')]))

    return pipeline

def bc_reg_test_corps():
    import bcreg

    pipeline = Pipeline(
        id='bc_reg_test_corps',
        description='A pipeline that queues up a small set of test corporations.')

    pipeline.add(Task(id='register_test_corps', description='Register some test corps for processing',
                        commands=[ExecutePython('./bcreg/find-test-corps.py')]))

    return pipeline

def bc_reg_pipeline_jsonbender():
    import bcreg

    pipeline2 = Pipeline(
        id='bc_reg_event_processor_json_transform_demo',
        description='A demo pipeline that processes events and generates credentials using JSONBender.')

    sub_pipeline2_2 = Pipeline(id='load_and_process_bc_reg_data', description='Load BC Reg data and generate credentials')
    sub_pipeline2_2.add(Task(id='register_un_processed_events', description='Register un-processed events',
                          commands=[ExecutePython('./bcreg/find-unprocessed-events.py')]))
    sub_pipeline2_2.add(Task(id='load_bc_reg_data', description='Load BC Registries data',
                          commands=[ExecutePython('./bcreg/process-corps.py')]), ['register_un_processed_events'])
    sub_pipeline2_2.add(Task(id='create_credentials_jsonbender', description='Create credentials using JSONBender transform',
                          commands=[ExecutePython('./bcreg/generate-creds-bender.py')]), ['load_bc_reg_data'])
    pipeline2.add(sub_pipeline2_2)

    sub_pipeline2_3 = Pipeline(id='submit_bc_reg_credentials', description='Submit BC Reg credentials to P-X')
    sub_pipeline2_3.add(Task(id='submit_credentials', description='Submit credentials',
                          commands=[ExecutePython('./bcreg/submit-creds.py')]))
    pipeline2.add(sub_pipeline2_3, ['load_and_process_bc_reg_data'])

    return pipeline2
  
