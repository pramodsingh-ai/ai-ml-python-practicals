import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Get correct CSV path (works from anywhere)
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "..", "data", "data.csv")

# Load dataset
df = pd.read_csv(csv_path)

# Input (X) and Output (y)
X = df[["Experience"]]
y = df["Salary"]cd "D:\Practical\AI_ML\ai-ml-python-practicals"

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=420
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# User input
experience = float(input("Enter years of experience: "))

# Predict
input_data = pd.DataFrame({"Experience": [experience]})
predicted_salary = model.predict(input_data)

print(f"Predicted salary for {experience} years experience = {predicted_salary[0]:.2f}")
