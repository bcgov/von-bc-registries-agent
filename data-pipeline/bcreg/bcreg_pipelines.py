from data_integration.pipelines import Pipeline, Task
from data_integration.commands.python import ExecutePython

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

def bc_reg_test_corps():
    import bcreg

    pipeline = Pipeline(
        id='bc_reg_test_corps',
        description='A pipeline that queues up a small set of test corporations.')

    pipeline.add(Task(id='register_test_corps', description='Register some test corps for processing',
                        commands=[ExecutePython('./bcreg/find-test-corps.py')]))

    return pipeline

def bc_reg_pipeline():
    import bcreg

    pipeline1 = Pipeline(
        id='bc_reg_event_processor',
        description='A pipeline that processes BC Registries events and generates credentials.')

    sub_pipeline1_2 = Pipeline(id='load_and_process_bc_reg_data', description='Load BC Reg data and generate credentials')
    sub_pipeline1_2.add(Task(id='register_un_processed_events', description='Register un-processed events',
                          commands=[ExecutePython('./bcreg/find-unprocessed-events.py')]))
    sub_pipeline1_2.add(Task(id='load_bc_reg_data', description='Load BC Registries data',
                          commands=[ExecutePython('./bcreg/process-corps.py')]), ['register_un_processed_events'])
    sub_pipeline1_2.add(Task(id='create_bc_reg_credentials', description='Create credentials',
                          commands=[ExecutePython('./bcreg/generate-creds.py')]), ['load_bc_reg_data'])
    pipeline1.add(sub_pipeline1_2)

    sub_pipeline1_3 = Pipeline(id='submit_bc_reg_credentials', description='Submit BC Reg credentials to P-X')
    sub_pipeline1_3.add(Task(id='submit_credentials', description='Submit credentials',
                          commands=[ExecutePython('./bcreg/submit-creds.py')]))
    pipeline1.add(sub_pipeline1_3, ['load_and_process_bc_reg_data'])

    return pipeline1

def bc_reg_pipeline_status():
    import bcreg

    pipeline = Pipeline(
        id='bc_reg_pipeline_status',
        description='Display overall event processing status.')

    pipeline.add(Task(id='display_pipeline_status', description='Display status of the overall pipeline processing status',
                        commands=[ExecutePython('./bcreg/display_pipeline_status.py')]))

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
  
