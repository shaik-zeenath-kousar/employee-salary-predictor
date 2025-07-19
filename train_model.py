import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load CSV
df = pd.read_csv("salary.csv")

# Use only YearsExperience as feature for simplicity
X = df[['YearsExperience']]
y = df['Salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
