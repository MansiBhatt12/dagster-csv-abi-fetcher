from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    FilesystemIOManager, 
    # sensor, 
    # RunRequest ,

)


from . import assets

# def should_trigger_sensor():
#     # Define the logic for your sensor triggering condition
#     # Return True or False based on the condition

#     # Example:
#     return True  

all_assets = load_assets_from_modules([assets])

# Addition: define a job that will materialize the assets
contract_job = define_asset_job("contract_job", selection=AssetSelection.all())

# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
contract_schedule = ScheduleDefinition(
    job=contract_job,
    cron_schedule="0 * * * *",  # every hour
)

io_manager = FilesystemIOManager(
    base_dir="data",  # Path is built relative to where `dagster dev` is run
)

# @sensor(job=contract_job)
# def materializes_asset_sensor():
#     yield RunRequest()


# @sensor
# def contract_sensor(context):

#     if should_trigger_sensor():
#         return RunRequest(run_key="2023-07-03T12:00:00", run_config={"config_key": "/path/to/fetch_csv_project/data/fetch_api.csv"})
#     return True 



defs = Definitions(
    assets=all_assets,
    jobs=[contract_job], 
    schedules=[contract_schedule],
    # sensors=[contract_sensor], 
    resources={
        "io_manager": io_manager,
    },  
)




