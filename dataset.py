import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
from scipy.stats import zscore
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE



# Data loading and inspection

df = pd.read_csv('CIC-EV-charger-attack-dataset/data/EVSE-A-idle-vulnerability-scan.csv', on_bad_lines='skip')
print("Dataset loaded successfully!")
print("Dataset information:")
print(df.info())
print("Dataset summary statistics:")
print(df.describe())

# Missing data analysis
print("Initial missing data check:")
print(df.isnull().sum())



# Filling missing values

# Fill missing values for numerical columns
numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Fill missing values for categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns
for column in categorical_columns:
    df[column].fillna(df[column].mode()[0], inplace=True)

# Verify missing values are handled
print("Final missing data check:")
print(df.isnull().sum())




# Encoding categorical data
for column in categorical_columns:
    df[column] = LabelEncoder().fit_transform(df[column].astype(str))

# Splitting target and features
X = df.drop('expiration_id', axis=1)
y = df['expiration_id']

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Model performance
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# Feature importance
feature_importances = model.feature_importances_
features = X.columns
sns.barplot(x=feature_importances, y=features)
plt.title("Feature Importances")
plt.show()

# Correlation matrix
corr = df.corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()


print("/"*200)
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("Eksik değer oranları:")
print(X_train.isnull().mean())

print("/"*200)





# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

print("Classification Report:")
print(classification_report(y_test, y_pred))

# Outlier detection and removal

z_scores = zscore(df[numeric_columns])
df_no_outliers = df[(z_scores < 3).all(axis=1)]
print(f"Dataset size after removing outliers: {df_no_outliers.shape}")

#Visualizing outliers for each column
for column in df.select_dtypes(include=['number']).columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df, x=column)
    plt.title(f"Outliers in {column}")
    plt.show()

# Target variable distribution
sns.countplot(data=df, x='expiration_id')
plt.title("Target Variable Distribution")
plt.show()

# Numerical column distributions
df[numeric_columns].hist(bins=20, figsize=(15, 10), color='skyblue', edgecolor='black')
plt.suptitle("Distribution of Numerical Columns")
plt.show()
































































