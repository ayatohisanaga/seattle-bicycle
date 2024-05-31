# Documentation for Seattle Bicycle Traffic Weather Data
IMT 542 // Ayato Hisanaga

## About
The Seattle Bicycle Traffic Weather Data API contains information about cyclist traffic volumens and weather conditions for 14 locations across Seattle. While each dataset contains daily data, the ranges vary between 2012 and 2024. Out of the fourteen datasets, four are considered active. The information is intended for city planners and cyclists who want to understand bicycle traffic patterns based on weather conditions. The information can be accessed through an API with an intuitive web interface that allows users to obtain data for their desired location(s) and/or date range.

## Methodology
The data is collected from various sources. Bicycle traffic data is obtained through Seattle Open Data's Socrata API. Weather conditions such as thunder, hail, and snow are obtained from NOAA.gov, and wind data is obtained from Farmer's Almanac and WeatherUnderground via webscraping. Currently, the data is stored locally in CSV and JSON formats and is being updated with more current data. While the weather data is updated on a daily basis, the bicycle traffic data is updated at a monthly or biweekly basis; different locations are updated at different intervals. Considerations are being made to best represent the data to balance timeliness with completeness. 

## Access
Users will have access to a web interface that shows a map of Seattle with each sensor location marked on the map. There will also be an integrated menu that allows users to specify a date range if desired. Users can select locations directly on the map or in the menu to obtain only the information they desire. For example, a user who wants to obtain information for the Fremont Bridge and Burke Gilman Trail between 2020 and 2021 will be able to use this API to do so. Once the desired locations and date ranges are specified, the requested data will be displayed in a tabular format for readability with the option to download the data as either a CSV or JSON file. 

## Structure
The dataset appears to consist of daily weather observations with various meteorological parameters recorded. Here's a structured description of the main fields, their types, and the properties of the information schema:

1. **date**
   - **Description:** The date of the observation.
   - **Type:** Date (ISO 8601 format: YYYY-MM-DD)
   - **Properties:** This field represents the calendar date for each recorded observation.

2. **daily_total**
   - **Description:** The total precipitation for the day.
   - **Type:** Numeric (float)
   - **Properties:** Measured in millimeters (mm). Represents the cumulative amount of precipitation within a 24-hour period.

3. **PRCP**
   - **Description:** Daily precipitation.
   - **Type:** Numeric (float)
   - **Properties:** Measured in millimeters (mm). Represents the precipitation recorded during the day.

4. **SNOW**
   - **Description:** Daily snowfall.
   - **Type:** Numeric (float)
   - **Properties:** Measured in millimeters (mm). Represents the amount of snow that fell during the day.

5. **TAVG**
   - **Description:** Daily average temperature.
   - **Type:** Numeric (float)
   - **Properties:** Measured in degrees Celsius (°C). Calculated as the average of the maximum and minimum temperatures of the day.

6. **TMAX**
   - **Description:** Daily maximum temperature.
   - **Type:** Numeric (float)
   - **Properties:** Measured in degrees Celsius (°C). Represents the highest temperature recorded during the day.

7. **TMIN**
   - **Description:** Daily minimum temperature.
   - **Type:** Numeric (float)
   - **Properties:** Measured in degrees Celsius (°C). Represents the lowest temperature recorded during the day.

8. **T_RANGE**
   - **Description:** Daily temperature range.
   - **Type:** Numeric (float)
   - **Properties:** Calculated as the difference between the daily maximum temperature (TMAX) and the daily minimum temperature (TMIN).

9. **WT01**
   - **Description:** Indicator for the presence of fog.
   - **Type:** Boolean (0 or 1)
   - **Properties:** A value of 1 indicates fog was observed, while 0 indicates it was not.

10. **WT02**
    - **Description:** Indicator for the presence of heavy fog or mist.
    - **Type:** Boolean (0 or 1)
    - **Properties:** A value of 1 indicates heavy fog or mist was observed, while 0 indicates it was not.

11. **WT03**
    - **Description:** Indicator for the presence of thunderstorms.
    - **Type:** Boolean (0 or 1)
    - **Properties:** A value of 1 indicates thunderstorms were observed, while 0 indicates they were not.

12. **WT04**
    - **Description:** Indicator for the presence of ice pellets.
    - **Type:** Boolean (0 or 1)
    - **Properties:** A value of 1 indicates ice pellets were observed, while 0 indicates they were not.

13. **WT05**
    - **Description:** Indicator for the presence of hail.
    - **Type:** Boolean (0 or 1)
    - **Properties:** A value of 1 indicates hail was observed, while 0 indicates it was not.

14. **WT06**
    - **Description:** Indicator for the presence of glaze or rime.
    - **Type:** Boolean (0 or 1)
    - **Properties:** A value of 1 indicates glaze or rime was observed, while 0 indicates it was not.

15. **WT08**
    - **Description:** Indicator for the presence of smoke or haze.
    - **Type:** Boolean (0 or 1)
    - **Properties:** A value of 1 indicates smoke or haze was observed, while 0 indicates it was not.

16. **avg_wind_speed**
    - **Description:** Average wind speed for the day.
    - **Type:** Numeric (float)
    - **Properties:** Measured in meters per second (m/s). Represents the average wind speed throughout the day.

17. **max_wind_speed**
    - **Description:** Maximum wind speed for the day.
    - **Type:** Numeric (float)
    - **Properties:** Measured in meters per second (m/s). Represents the highest wind speed recorded during the day.

note: the boolean weather indicators ("WTxx") are to be updated with more human-readable names. The updated datasets will replace the current field names with respective condition names.

## Example
![Example request]("/Users/ayatohisanaga/University of Washington/2024 Spring/IMT 542/sample_request.png")

![Example output]("/Users/ayatohisanaga/University of Washington/2024 Spring/IMT 542/sample_output.png")

![Map]("/Users/ayatohisanaga/University of Washington/2024 Spring/IMT 542/map.png")