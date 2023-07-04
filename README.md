# Dagster Project: Fetch ABIs from CSV File and Save into CSV File

This Dagster project demonstrates a data pipeline that reads contract addresses from a CSV file which contain 500 contract addresses, fetches ABI data for each address, and saves the results into another CSV file. The project consists of the following files:

* asset.py :  This file contains the code to fetch the ABIs and also defines asset.
* __init__.py : This file defines the jobs and schedules that are used by the project.

## Setup

To run the project, you will need to have Dagster installed (installation instructions: https://docs.dagster.io/getting_started/installation). Once you have Dagster installed in your python local environment, you can run the project by following these steps:

1. Clone the repository or download the project files.
   
2. Install the dependencies
```bash
pip install -e ".[dev]"
```
* Note: Don't forget to import, install necessary packages
```bash
pip install package_name
```
3. The input CSV file is already placed in the data directory named address.csv, this CSV file contains one column named "ADDRESS" that holds the contract addresses.

4. Run the command
```bash
dagster dev
```
This will start the Dagster UI on your local machine. You can then use the UI to interact with the project.

Open your web browser and navigate to http://localhost:3000 to access the Dagster UI.

Click on the Materialize in the Dagster UI and execute it. Monitor the pipeline execution in the Dagster web UI. Once completed, the fetch_api.csv file in the data directory will contain the fetched ABI data. 
