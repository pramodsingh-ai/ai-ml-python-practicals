import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Load Excel file
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "data", "loan_data.xlsx")

df = pd.read_excel(file_path)

# Convert EmploymentType to numeric
df["EmploymentType"] = df["EmploymentType"].map({
    "Salaried": 1,
    "Self-Employed": 0
})

# Define Features and Target
X = df[["Age", "Income", "CreditScore", "ExistingEMI", "EmploymentType"]]
y = df["EligibleLoanAmount"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate r2 and MAE
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("===== Model Evaluation =====")
print(f"R² Score: {r2:.4f}")
print(f"Mean Absolute Error: {mae:.2f}")

# User input prediction
print("\n===== Loan Amount Prediction =====")

age_input = int(input("Age: "))
income_input = float(input("Monthly Income: "))
credit_input = int(input("Credit Score: "))
emi_input = float(input("Existing EMI: "))
emp_input = input("Employment Type (Salaried/Self-Employed): ")

emp_numeric = 1 if emp_input.lower() == "salaried" else 0

input_data = pd.DataFrame([{
    "Age": age_input,
    "Income": income_input,
    "CreditScore": credit_input,
    "ExistingEMI": emi_input,
    "EmploymentType": emp_numeric
}])

predicted = model.predict(input_data)[0]

print(f"\nPredicted Eligible Loan Amount: {predicted:.2f}")

# Evaluate on test set
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("===== Model Evaluation =====")
print(f"R² Score: {r2:.4f}")
print(f"Mean Absolute Error: {mae:.2f}")
