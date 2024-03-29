import numpy as np
from sklearn.linear_model import LinearRegression

# Data: Blood pressure readings after eating sugary, salty, and normal meals
X = np.array([
    [130, 125, 120],  # Patient 1
    [135, 130, 122],  # Patient 2
    [128, 127, 118],  # Patient 3
    [132, 128, 121],  # Patient 4
    [138, 131, 123],  # Patient 5
    [129, 126, 119],  # Patient 6
    [133, 129, 122],  # Patient 7
    [137, 132, 124],  # Patient 8
    [131, 126, 120],  # Patient 9
    [134, 130, 123]   # Patient 10
])

# Target: Blood pressure readings after next meal
y = X[:, 2] 

# Train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict function
def predict_next_blood_pressure(meal_type):
    if meal_type == 'sugary':
        return model.predict([[140, 135, 127]])[0]  # Random values for sugary meal
    elif meal_type == 'salty':
        return model.predict([[145, 138, 130]])[0]  # Random values for salty meal
    elif meal_type == 'normal':
        return model.predict([[135, 130, 125]])[0]  # Random values for normal meal
    else:
        return "Invalid meal type"

# Test the prediction
print("Predicted blood pressure after a sugary meal:", predict_next_blood_pressure('sugary'))
print("Predicted blood pressure after a salty meal:", predict_next_blood_pressure('salty'))
print("Predicted blood pressure after a normal meal:", predict_next_blood_pressure('normal'))
