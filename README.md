[![CI](https://github.com/nogibjj/IDS706_Mini_PJT6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/IDS706_Mini_PJT6/actions/workflows/cicd.yml)

## Overview 
This project is focused on establishing a cloud-based database and performing data queries through Azure Databricks. It involves the creation of a data pipeline and developing queries that encompass operations such as data joins and aggregations.

Dataset used: [Hate-crimes](https://github.com/fivethirtyeight/data/blob/master/hate-crimes/hate_crimes.csv)

The dataset is organized into two separate sets by dividing a specific column. This partitioning is done with the intention of merging these datasets together at a later stage for analysis and processing. 

## Workflow Steps
1. Set Up Codespaces
    * Open GitHub Codespaces.
    * Create and add an '.env' file to securely store my Databricks credentials for connection.
2. Azure Databricks Configuration
    * Generate an Azure Databricks Workspace.
    * Create a Computer Cluster within the Databricks environment.
3. Data Processing
    * Execute complex SQL queries in Databricks
4. Data Pipeline
    * Implement data ETL (Extract, Transform, Load) and querying using the following syntax:
    * Use 'make etract' for data extraction.
    * Utilize 'make transform_load' for data transformation and loading.
    * Employ 'make query' for querying the dataset

## Query Explanation 
```sql
SELECT a.state, 
        AVG(a.median_household_income) AS average_median_household_income,
        AVG(a.share_unemployed_seasonal) AS average_share_unemployed_seasonal,
        a.share_population_in_metro_areas,
        b.gini_index
    FROM default.hate_crimes1DB AS a
    JOIN default.hate_crimes2DB AS b ON a.id = b.id
    GROUP BY a.state, a.share_population_in_metro_areas, b.gini_index
    ORDER BY b.gini_index
    LIMIT 5
```
This SQL query retrieves data from two tables (hate_crimes1 and hate_crimes2) and performs an inner join based on the id column. It then groups the data by state, share_population_in_metro_areas, and gini_index. Within each group, it calculates the average of median_household_income and share_unemployed_seasonal. The results are ordered by gini_index in ascending order and limited to the top 5 rows. This query is useful for analyzing and summarizing economic and demographic data based on the Gini index. 

## Result of Query 
![image](https://github.com/nogibjj/IDS706_Mini_PJT6/assets/141780408/a0d6eb74-1e18-4d91-a506-a1e8031ed34a)

## Test Result
![image](https://github.com/nogibjj/IDS706_Mini_PJT6/assets/141780408/36d9dcae-3166-4af8-b999-44a6005cc588)

