# Random Forest Classifier for predicting Crop_Type
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Encode categorical data (Crop_Type and Soil_Type)
le_crop = LabelEncoder()
le_soil = LabelEncoder()

data['Crop_Type'] = le_crop.fit_transform(data['Crop_Type'])
data['Soil_Type'] = le_soil.fit_transform(data['Soil_Type'])

# Prepare the data
X = data[['Soil_pH', 'Temperature', 'Humidity', 'Wind_Speed', 'N', 'P', 'K', 'Soil_Quality']]
y = data['Crop_Type']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')