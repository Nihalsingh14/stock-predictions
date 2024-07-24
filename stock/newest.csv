from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

# Sample dataset (hypothetical)
data = {
    'Age': [25, 30, 35, 40, 45, 50, 75, 90],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'Socio-economic Status': ['High', 'Low', 'High', 'Low', 'High', 'High', 'Low', 'Low'],
    'Survived': [1, 1, 1, 0, 1, 0, 1, 0]  # 1 for survived, 0 for not survived
}

df = pd.DataFrame(data)

# Convert categorical variables into numerical
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Socio-economic Status'] = df['Socio-economic Status'].map({'Low': 0, 'High': 1})

# Split data into features and target variable
X = df.drop('Survived', axis=1)
y = df['Survived']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Input for a new person
age = int(input("Enter Age: "))
gender = input("Enter Gender (Male/Female): ")
socio_economic_status = input("Enter Socio-economic Status (High/Low): ")

# Convert input to numerical values
gender = 1 if gender.lower() == 'female' else 0
socio_economic_status = 1 if socio_economic_status.lower() == 'high' else 0

# Create a DataFrame for the new data
new_data = {'Age': [age], 'Gender': [gender], 'Socio-economic Status': [socio_economic_status]}
new_df = pd.DataFrame(new_data)

# Predict survival for the new person
prediction = model.predict(new_df)
if prediction[0] == 1:
    print("This person is likely to survive.")
else:
    print("This person is not likely to survive.")