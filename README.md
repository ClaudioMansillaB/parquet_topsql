# Parquet to PostgreSQL Converter

This proyect provides a solution to convert Parquet files to PostgreSQL databases using DuckDB as an intermediary.

## Requirements

- Python 3.8+
- DuckDB
- PostgreSQL

# Configuration

## Clone this repository:
Copygit clone https://github.com/claudiomansillab/parquet-to-psql.git
cd parquet-to-psql

## Create a virtual environment and activate it:

Copypython -m venv venv
source venv/bin/activate  # In Windows: venv\Scripts\activate

## Install the dependencies:
Copypip install -r requirements.txt

## Copy the .env.example file to .env and edit the environment variables according to your PostgreSQL configuration:
Copycp .env.example .env


# Usage

Place your Parquet files in the data/input/ folder.

## Execute the main script:
Copypython src/main.py

The data will be loaded into PostgreSQL and a summary will be generated in data/output/.

# Project Structure

src/: Contains the main Python scripts.
scripts/: Shell scripts for configuration and execution.
data/: Folders for input and output files.
tests/: Unit tests.

# Contributions

The contributions are welcome. Please open an issue to discuss major changes before submitting a pull request.
