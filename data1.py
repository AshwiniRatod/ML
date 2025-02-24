#encoding data[one hot encoding of data using scikit learn library]
import pandas as pd
from sklearn.preprocessing import LabelEncoder  # ✅ Corrected import

# Create a DataFrame
df = pd.DataFrame({"name": ["cube", "car", "dog", "pink"]})

# Initialize LabelEncoder
le = LabelEncoder()

# Apply Label Encoding
df["encoded_name"] = le.fit_transform(df["name"])  # ✅ Use column name, not double brackets

print(df)
