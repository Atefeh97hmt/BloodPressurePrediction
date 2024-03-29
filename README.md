# Blood Pressure Prediction
This Python script is a simple Blood Pressure Prediction system that predicts the next blood pressure based on the type of meal eaten (sugary, salty, or normal). It utilizes a Linear Regression model from scikit-learn library for prediction.

## Dependencies
This script requires the following dependencies:
-	numpy
-	scikit-learn

You can install these dependencies using pip:
-	pip install numpy 
-	pip install scikit-learn

## Usage
1. Make sure you have installed the dependencies mentioned above.
2. Clone or download this repository.
3. Run the “BloodPressurePrediction.py” script using Python: python BloodPressurePrediction.py

## Data
The dataset contains blood pressure readings for 10 patients after eating sugary, salty, and normal meals. This data is used to train the Linear Regression model.

## Predictions
The script provides a function “predict_next_blood_pressure()” to predict the blood pressure after the next meal based on the type of meal eaten. You can call this function with the meal type as an argument:
print("Predicted blood pressure after a sugary meal:", predict_next_blood_pressure('sugary'))
print("Predicted blood pressure after a salty meal:", predict_next_blood_pressure('salty'))
print("Predicted blood pressure after a normal meal:", predict_next_blood_pressure('normal'))

## Note
This script contains random values for meal types (sugary, salty, and normal) for demonstration purposes. You should replace these values with actual data for accurate predictions.
