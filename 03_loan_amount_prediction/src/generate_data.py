import numpy as np
import pandas as pd
import os

# Set seed for reproducibility
np.random.seed(42)

# Number of records
n = 20000

# Generate synthetic NBFC customer data
age = np.random.randint(21, 60, n)
income = np.random.randint(20000, 150000, n)
credit_score = np.random.randint(550, 850, n)
existing_emi = np.random.randint(0, 20000, n)
employment_type = np.random.choice(["Salaried", "Self-Employed"], n)

# Business logic to calculate eligible loan amount
loan_amount = (
    income * 5
    + credit_score * 100
    - existing_emi * 10
    + np.where(employment_type == "Salaried", 50000, 0)
    - age * 1000
)

loan_amount = np.maximum(loan_amount, 50000)

# Create DataFrame
df = pd.DataFrame({
    "Age": age,
    "Income": income,
    "CreditScore": credit_score,
    "ExistingEMI": existing_emi,
    "EmploymentType": employment_type,
    "EligibleLoanAmount": loan_amount
})

# Create data folder if not exists
base_dir = os.path.dirname(__file__)
data_folder = os.path.join(base_dir, "..", "data")
os.makedirs(data_folder, exist_ok=True)

file_path = os.path.join(data_folder, "loan_data.xlsx")

# Save to Excel
df.to_excel(file_path, index=False)

print(f"Excel file generated successfully at: {file_path}")
print(df.head())
