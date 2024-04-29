# London Marathon Data Analysis

![London Marathon](/doc/London_Marathon_mens.png)

## Overview

This project aims to scrape and analyze data from the London Marathon editions spanning from 2010 to 2024. By analyzing this data, we can gain insights into trends, participant performance, and more.

## Requirements

To run this project, ensure you have the following installed:

- Python (3.x recommended)
- pip

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Data Gathering
To gather data from results.tcslondonmarathon.com, use the following command from the project's root directory:

```bash
python3 utils/london_marathon_results_scraper.py
```
This script will fetch the data and store it locally for further processing.

## Data Cleaning
Before analysis, the raw data needs to be cleaned and formatted. Use the following command to convert raw data to CSV files:

```bash
python3 utils/utils.py
```

## Analysis
Once the data is prepared, you can perform analysis by running:

```bash
python3 analysis.py
```
This script will generate insights and visualizations based on the collected and cleaned data.