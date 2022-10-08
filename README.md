# Eonlabs-Data-Representation--TTA-

# Data Representation TTA

by Aurelle TCHAGNA KOUANOU (tkaurelle@gmail.com)


## General Idea

The goal is to output time series of consistent Google Trends data from 2017
 till the present with time interval of hours based on three csv raw data: monthly_data.csv, weekly_data.csvand hourly_data.csv

## Approach

to deal with this problem,

1. we joint the differents csv data based on time
2. multiply the hourly_data by the weekly_data and the monthly_dataand normalize them because the scale is different
3. the reference here is the monthly_data

## Instructions

To run this code you have to install these library first
- Pandas
- Numpy
-plotly

After that just run the test.py file

```console
python test.py
```
