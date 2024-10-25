import pandas as pd

# Load the dataset
file_path = '/content/drive/MyDrive/Dataset/crop_yield_dataset.csv'
data = pd.read_csv(file_path)

# Display the first few rows and basic info of the dataset
data_info = data.info()
data_head = data.head()

data_info, data_head