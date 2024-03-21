# Python Script for Retrieving and Saving MySQL Data
This Python script connects to a MySQL database, executes a query to retrieve data, and saves the results to a CSV file. It utilizes the pyodbc library for database connectivity, pandas for data manipulation, and plyer for displaying notifications.

## Table of Contents
Installation

Dependencies

Configuration

Task Scheduling

### Installation
To run the script, you'll need to have Python installed on your system. You can download and install Python from the official Python website.

Once Python is installed, you can install the required dependencies using pip:

pip install pandas pyodbc plyer

### Dependencies
pandas: A powerful data manipulation and analysis library.

pyodbc: A Python library for connecting to databases using ODBC.

plyer: A Python library for accessing platform-specific features.

### Configuration
Before running the script, make sure to modify the database connection details (host, database name, username, password) in the script according to your MySQL server configuration.

### Task Scheduling

To automate the execution of the script at specified intervals, you can use Task Scheduler on Windows:

Open Task Scheduler by searching for it in the Start menu.

Click on "Create Basic Task" in the right-hand sidebar.

Follow the wizard to specify a name and description for the task.

Choose how often you want the task to run (daily, weekly, monthly, etc.).

Select "Start a program" as the action to perform.

Browse to the location of your Python executable (python.exe) and specify the script file (Chocolate.py) as the argument.

Complete the wizard, and the task will be scheduled to run automatically according to your specified schedule.
