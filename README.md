# Sales Data Analysis Project

This project provides scripts to analyze sales data and identify top-selling products, stores, brands, and cities within a specified date range. It utilizes pandas for data manipulation and analysis.
## Getting Started
This section contains instructions on how to get the project running on your local development environment.

### Running with Docker
1) Build your Docker image:
```bash
docker-compose build
```
This command builds the Docker image using the instructions in your Dockerfile and docker-compose.yml file.

2) Start the Docker container:
```bash
docker-compose up
```
## Features
- Analyze top seller products, stores, brands, and cities.
- Filter sales data by a given date range.
- Dynamically specify the number of top items to display.
- Custom logging for error tracking and debugging.

## Structure

`solution.py`: The main script that executes the analysis based on command-line arguments.

`argument_parser.py`: Defines command-line arguments and parses them.

`csv_loader.py`: Responsible for loading and preprocessing CSV data files.

`df_analyzer.py`: Contains the logic for filtering, merging, and analyzing sales data.

`logger.py`: Implements a custom logger for the application.

## Usage
Run the solution.py script with the desired arguments:
```bash
python solution.py --min-date YYYY-MM-DD --max-date YYYY-MM-DD --top N
```

### Where
--min-date: Start date of the analysis range in YYYY-MM-DD format.
--max-date: End date of the analysis range in YYYY-MM-DD format.
--top: Number of top items to display.

### Examples
```bash
docker-compose run app python solution.py --min-date 2020-01-01 --max-date 2020-06-30 --top 2
```
```bash
python solution.py --min-date 2020-01-01 --max-date 2020-06-30 --top 2
```

### Licence
This project is licensed under the MIT License. See the LICENSE file for more information.