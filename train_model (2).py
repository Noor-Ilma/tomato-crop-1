import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Use RandomForestRegressor for regression tasks
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load dataset
data = pd.read_csv('crop_yield_dataset.csv')  # Replace with your dataset's filename

# Data preprocessing
# Calculate additional features if necessary (e.g., moisture levels, temperature variations)
# For example: 
data['debt_income_ratio'] = data['Wind_Speed'] / data['Humidity']  # Adjust this feature as needed

# Prepare feature and target variables
# Select relevant features based on your dataset
X = data[['Soil_pH', 'Temperature', 'Humidity', 'N', 'K', 'Wind_Speed']]
y = data['Crop_Yield']  # Assuming Crop_Yield is the target variable for prediction

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model for regression
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)

# Print evaluation metrics
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"R² Score: {r2_score(y_test, y_pred)}")

# Save the model
joblib.dump(model, 'tomato_crop_yield_model.pkl')
