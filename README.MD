# Instructions For Running SFL Take Home Assignment

## Installation & Setup
Within a virtual enviornment run the following command:
```commandline
pip install {path to sfl_assignment}
```
Replace {path to sfl_assignment} with the path to sfl_assignment on your machine.

The default database used in this assignment is sqlite. Run the following command to setup the database:
```commandline
create_database sqlite
```
This command will create a `.sfl_assignment` directory in your home directory and a `users.db` file will be created in
 the newly created directory.
 
 Later, you can clean up the `.sfl_assignment` directory and its contents by running the following command:
 ```commandline
remove_database sqlite
``` 

## Usage

Once the database has been created, run the following command to execute the etl pipeline:
```commandline
run_etl_pipeline {path to the data file}
```
Replace {path to the data file} with the path to the data file to be processed on your machine

To view the records in the database run the following command:
```commandline
show_records
```  
