# Spotify ETL using Airflow

## Project Overview

The **Spotify Data ETL with Airflow** project is an end-to-end data pipeline designed to automate the extraction, transformation, and loading of data of artists from Spotify API. It integrates with the Spotify API, extracts data, processes it, and allows you to choose a destination for storage, which can include Amazon S3, Google Cloud Storage, or other storage solutions.

## Architecture

<img width="646" alt="image" src="https://github.com/Surendraprajapat18/airflow_spotify_etl_pipeline/assets/97840357/741039f8-d761-48d9-abed-87e591d871b2">

## Project Flow 
<img width="646" alt="image" src="https://github.com/Surendraprajapat18/airflow_spotify_etl_pipeline/assets/97840357/071edc75-e7a9-451d-81f1-7d7098b6a976">


## Project Components
The project is divided into several crucial components that play a significant role in efficiently processing and organizing Spotify artist data. The primary components are as follows:

- **Data Extraction:** To scrape the names of top global artists, I utilized the (https://kworb.net/itunes/) website and extracted their details such as genre, followers, and popularity via the Spotify API.

- **Data Transformation:** The extracted data is then converted into a structured format that is suitable for analysis.

- **Data Loading:** Following data preparation, the user can select the storage destination. In my project, I have opted for an Amazon S3 bucket to store the data.

- **Airflow Integration:** The project is integrated with Apache Airflow, allowing for scheduled or trigger-based ETL jobs. This integration plays a vital role in automating and orchestrating the entire pipeline.


## Final Output

<img width="646" alt="image" src="https://github.com/Surendraprajapat18/airflow_spotify_etl_pipeline/assets/97840357/cb3c2c28-823a-4fd1-99d8-a821db69fc20">
