# AI-Project: Lab (Group 7)
# Project Submitted By : Nazmus Sadat Shohag
## Team Members
- 2018331099: Nazmus Sadat
- 2018331097: Aisha Hayder Chowdhury
##  Description
A heart disease prediction system that can predict whether a person has heart disease or not. In this AI system, we provide information about patients, and our system predicts the result.

## Overview

Our dataset contained the following attributes :

1.Age | Objective Feature | age | int (days) <br>
2.Height | Objective Feature | height | int (cm) | <br>
3.Weight | Objective Feature | weight | float (kg) | <br>
4.Gender | Objective Feature | gender | categorical code | <br>
5.Systolic blood pressure | Examination Feature | ap_hi | int |<br>
6.Diastolic blood pressure | Examination Feature | ap_lo | int |<br>
7.Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |<br>
8.Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |<br>
9.Smoking | Subjective Feature | smoke | binary |<br>
10.Alcohol intake | Subjective Feature | alco | binary |<br>
11.Physical activity | Subjective Feature | active | binary |<br>
12.Presence or absence of cardiovascular disease | Target Variable | cardio | binary<br>

<br><br>

The machine-learning model is first trained with the test dataset. Then the 12th attribute (the presence or absence of heart disease) is predicated.
Here, the random forest algorithm is used to build the model.
To predict, give value to the above attribute, and our system will predict the result.


## Dataset
[Kaggle: Cardiovascular Disease dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset)

### Frontend:
This project is done using python's framework Streamlit.

## To run this project:
*Prerequisites:*

- [python3](https://www.python.org/downloads/release/python-380/)
<br>

Clone this repository and run the command `streamlit run app.py`

## Acknowledgement
We would like to offer our heartfelt appreciation to our project manager, **Enamul Hassan** sir, for his invaluable input, assistance, and knowledge.

- **Enamul Hassan**

  - **Assistant Professor**, Dept. of CSE, SUST
  
    **Office Address:** Room no: 119, Department of Computer Science and Engineering, Dr. M. A. Wazed Miah IICT Building, Shahjalal University of Science and Technology,          Sylhet-3114  
    **Phone:** +8801914061632  
    **Email:** enam-cse@sust.edu  
     **Faculty Web Page:**
     [https://www.sust.edu/d/cse/faculty-profile-detail/590/4](https://www.sust.edu/d/cse/faculty-profile-detail/590/4)

# Demo of our project are :
### Screenshot 1 :
![ScreenShot1_Demo of app](https://github.com/nsshohag/heart_disease_prediction/blob/main/screenshot1.PNG)

### Screenshot 2 :
![ScreenShot2_Demo of app](https://github.com/nsshohag/heart_disease_prediction/blob/main/screenshot2.PNG)

### Screenshot 3 :
![ScreenShot3_Demo of app](https://github.com/nsshohag/heart_disease_prediction/blob/main/screenshot3.PNG)
