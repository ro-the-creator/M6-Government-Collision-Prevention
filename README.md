# Module 6: Pinpointing High-Risk Inferential Factors for Municipal Car Safety

<div align='center'>

<img width="2000" height="1429" alt="dcas" src="https://github.com/user-attachments/assets/c395712f-1f9f-4633-9e8d-a46f1c338a24" />


### **An inferential modeling project for the Department of Citywide Administrative Services (DCAS), Inferring seasonal and borough trends of collisions resulting in injury/death involving government vehicles in New York City.**
</div>


# Project Overview

(README Directory here)

## Data Source

<div align='center'>

The dataset consists of vehicle accidents, where each row represents a unique crash event. According to NYC OpenData, each row is an MV104-AN police report, which is required to be filled out when someone is injured, killed, or when there is at least $1,000 worth of damage. More details, including an option to download the dataset, can be found [here](https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data).

<br>

<details> <summary><strong> Data Dictionary (Click to Expand)</strong></summary> <br>
  
| **Column Name (Original)**    | **Description**                            | **Field Name (Cleaned)**        | **Type**           |
| ----------------------------- | ------------------------------------------ | ------------------------------- | ------------------ |
| CRASH DATE                    | Occurrence date of collision               | `crash_date`                    | Floating Timestamp |
| CRASH TIME                    | Occurrence time of collision               | `crash_time`                    | Text               |
| BOROUGH                       | Borough where collision occurred           | `borough`                       | Text               |
| ZIP CODE                      | Postal code of incident occurrence         | `zip_code`                      | Text               |
| LATITUDE                      | Latitude coordinate (WGS 1984, EPSG 4326)  | `latitude`                      | Number             |
| LONGITUDE                     | Longitude coordinate (WGS 1984, EPSG 4326) | `longitude`                     | Number             |
| LOCATION                      | Latitude, Longitude pair                   | `location`                      | Location           |
| ON STREET NAME                | Street on which the collision occurred     | `on_street_name`                | Text               |
| CROSS STREET NAME             | Nearest cross street to the collision      | `off_street_name`               | Text               |
| OFF STREET NAME               | Street address if known                    | `cross_street_name`             | Text               |
| NUMBER OF PERSONS INJURED     | Number of persons injured                  | `number_of_persons_injured`     | Number             |
| NUMBER OF PERSONS KILLED      | Number of persons killed                   | `number_of_persons_killed`      | Number             |
| NUMBER OF PEDESTRIANS INJURED | Number of pedestrians injured              | `number_of_pedestrians_injured` | Number             |
| NUMBER OF PEDESTRIANS KILLED  | Number of pedestrians killed               | `number_of_pedestrians_killed`  | Number             |
| NUMBER OF CYCLIST INJURED     | Number of cyclists injured                 | `number_of_cyclist_injured`     | Number             |
| NUMBER OF CYCLIST KILLED      | Number of cyclists killed                  | `number_of_cyclist_killed`      | Number             |
| NUMBER OF MOTORIST INJURED    | Number of vehicle occupants injured        | `number_of_motorist_injured`    | Number             |
| NUMBER OF MOTORIST KILLED     | Number of vehicle occupants killed         | `number_of_motorist_killed`     | Number             |
| CONTRIBUTING FACTOR VEHICLE 1 | Factors contributing to the collision      | `contributing_factor_vehicle_1` | Text               |
| CONTRIBUTING FACTOR VEHICLE 2 | Factors contributing to the collision      | `contributing_factor_vehicle_2` | Text               |
| CONTRIBUTING FACTOR VEHICLE 3 | Factors contributing to the collision      | `contributing_factor_vehicle_3` | Text               |
| CONTRIBUTING FACTOR VEHICLE 4 | Factors contributing to the collision      | `contributing_factor_vehicle_4` | Text               |
| CONTRIBUTING FACTOR VEHICLE 5 | Factors contributing to the collision      | `contributing_factor_vehicle_5` | Text               |
| COLLISION_ID                  | Unique record code (Primary Key)           | `collision_id`                  | Number             |
| VEHICLE TYPE CODE 1           | Vehicle category type                      | `vehicle_type_code1`            | Text               |
| VEHICLE TYPE CODE 2           | Vehicle category type                      | `vehicle_type_code2`            | Text               |
| VEHICLE TYPE CODE 3           | Vehicle category type                      | `vehicle_type_code_3`           | Text               |
| VEHICLE TYPE CODE 4           | Vehicle category type                      | `vehicle_type_code_4`           | Text               |
| VEHICLE TYPE CODE 5           | Vehicle category type                      | `vehicle_type_code_5`           | Text               |
</details>

</div>

## Business Problem

<div align='center'>

With concerns over increased costs from settlements, workers' compensation, etc., the DCAS wants a way to infer government vehicle collisions that cause injury/death. They hope to roll out targeted training by borough and season, and allocate resources more effectively to areas and times with higher collision rates involving injury/death.

### **Eight people were hurt when an MTA bus crashed in Queens... Sources tell CBS News New York the bus driver misjudged the closeness of the curb.**

</div>

<div align='right'>

#### **- John Dias, Jesse Zanger, [CBS News](https://www.cbsnews.com/newyork/news/flushing-queens-mta-bus-crash/)**

</div>

<div align='center'>

With proper training, unfortunate events like these can be prevented, and the costs associated with these horrific collisions can be reduced.

</div>

## Modeling Metrics

<div align='center'>

Given our business question, we chose features that could best infer the factors that contribute to government vehicle collisions causing injury/death. Our features were categorical and binary, with the categorical variables requiring One Hot Encoding for the model to be able to interpret each borough and season.

</div>

### **Features**
- Borough (Queens, Bronx, Manhattan, Brooklyn, Staten Island)

- Season (Winter, Spring, Summer, Fall)

- Is Government Vehicle (Y/N)

### Evaluation Metrics

<div align='center'>

Looking at our errors, our complex model beat out our simple and baseline models, indicating to us that our features were indeed useful and not detrimental to the model's performance. This is the model we eventually input into our app, giving us correct injury/death identification roughyl 60% of the time.

Taking a deeper look into our confusion matrix, there was a reasonable balance between precision vs. recall. As a result, we got ~0.50 F1-scores across the two variables, injury/death and no injury/death. Although there is much room for improvement, the lack of absurdly high precision/recall values tells us that our data is not overfit or leaked.

</div>

## Ethics & Assumptions


