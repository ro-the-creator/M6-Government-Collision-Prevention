# Module 6: Pinpointing High-Risk Inferential Factors for Municipal Car Safety

<div align='center'>

<img width="2000" height="1429" alt="dcas" src="https://github.com/user-attachments/assets/c395712f-1f9f-4633-9e8d-a46f1c338a24" />


### **An inferential modeling project for the Department of Citywide Administrative Services (DCAS), Inferring seasonal and borough trends of collisions resulting in injury/death involving government vehicles in New York City.**
</div>


# Project Overview

→ [Project Overview](#project-overview)  
  → [About Us](#about-us)  
  → [Data Source](#data-source)  
  → [Business Problem](#business-problem)  
→ [Modeling Metrics](#modeling-metrics)  
  → [Features](#features)  
  → [Evaluation Metrics](#evaluation-metrics)  
→ [Ethics & Assumptions](#ethics--assumptions)  
  → [Bias](#bias)  
  → [Ethics](#ethics)  
  → [Assumptions](#assumptions)  
→ [Deployment](#deployment)  


## About Us

<div align='center'>

<img width="400" height="400" alt="s-blob-v1-IMAGE-bLZk3RNRCGY" src="https://github.com/user-attachments/assets/82c8ff05-b68e-4b8a-a665-a62085efaf35" />

### **Rolando Mancilla-Rojas**

23 Years Old

Data Analyst @ The Marcy Lab School

Project Management

Modeling

GitHub

App Deployment

***

<br>

<img width="400" height="400" alt="s-blob-v1-IMAGE-8ac22berePU" src="https://github.com/user-attachments/assets/02c04924-3c84-4b42-85a4-2667db86fe46" />


### **Debo Odutola**

21 Years Old

Data Analyst @ The Marcy Lab School

EDA

GitHub

Visuals

Cleaning

Feature Engineering

***

</div>


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

<div align='center'>

In creating features and modeling, there were several key ethical points that we noted. While this may not drastically influence the model's performance, it was important to be aware of these points in order to better interpret the output of the model.

</div>

### Bias

- Injury and death are grouped together, which can dilute the perceived severity.
  - For example, a bruise and a fatal crash fall within the same category.

- The data comes from an MV104-AN police report, meaning the officer who completed the form may have been the driver of the government vehicle involved.

- This may account for the large number of accidents with an ‘unspecified’ cause involving government vehicles.

### Ethics

- The system will be used solely for its intended purpose of targeted training, aimed at improving the stakeholder’s reputation and making New York City streets safer.

- If the model suggests a high likelihood, it must not be used to justify increasing tax costs.

- If the model suggests a low likelihood, it must not be used to downplay or conceal the risk of injury.

### Assumptions

- TheFuzz correctly categorized records using a similarity threshold of 70.

- For all vehicle-type columns, we assumed that missing values do not indicate government vehicle involvement unless explicitly stated.

- For Ambulance, Bus, Garbage Truck, Delivery Truck, and Fire Truck, we assumed these vehicles are government-owned rather than commercial or private.

- The EDA places all vehicles contributing to a collision on one line, separated by “|”, which may affect the specific count of government vehicles but correctly reflects the number of collisions involving government vehicles.

- We assumed that government vehicle types are listed with priority over vehicle style; for example, a vehicle listed as a Sedan is assumed not to be government-owned.

<div align='center'>

More information, including the cleaning process, assumptions, and bias, can be found [here](./notebooks/)

</div>

## Deployment

<div align='center'>

To run the app locally, you can run it in the preloaded environment straight from GitHub CodeSpaces:

<br>

<img width="319" height="269" alt="image" src="https://github.com/user-attachments/assets/3986290b-ff66-4493-bfc2-90e99cb5df6b" />

<br>

</div>

1. Fork the repository.

2. Create a workspace within the repository.

3. Run `streamlit run app.py` inside the app folder.


