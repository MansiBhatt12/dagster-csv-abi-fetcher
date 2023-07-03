# Dagster Project: Fetch APIs from CSV File and Save into CSV File

This Dagster project demonstrates a data pipeline that reads contract addresses from a CSV file which contain 500 contract addresses, fetches API data for each address, and saves the results into another CSV file. The project consists of the following files:

asset.py :  This file contains the code to fetch the APIs and also defines asset.
__init__.py : This file defines the jobs ans schedules that are used by the project.

## Features

* The project can fetch APIs for 5 contract addresses.
* The data is saved to a CSV file.
* The project includes scheduled pipeline, a predefined job and schedule to run the pipeline every hour. 
* The project uses the File System I/O Manager to store the fetched data in a directory called 'data' in your file system to a more permanent location. 

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



