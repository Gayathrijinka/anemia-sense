import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, accuracy_score

# Load and clean the dataset
df = pd.read_csv("anemia.csv")

# Rename columns for consistency
df.rename(columns={
    'Gender': 'gender', 'Hemoglobin': 'hemoglobin',
    'MCH': 'mch', 'MCHC': 'mchc', 'MCV': 'mcv', 'Result': 'target'
}, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Drop rows with null values
df.dropna(inplace=True)

# Convert categorical columns if needed
if df['gender'].dtype == 'object':
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})

# Exploratory Data Analysis
print("📊 Dataset Info:")
print(df.info())
print("\n🔍 Summary Statistics:")
print(df.describe())
print("\n📈 Class Distribution:")
print(df['target'].value_counts())

# Features and target
X = df[['gender', 'hemoglobin', 'mch', 'mchc', 'mcv']]
y = df['target']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models to compare
models = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'SVM': SVC()
}

# Evaluate models
print("\n📚 Model Comparison (using 5-fold cross-validation):")
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"{name}: Mean Accuracy = {scores.mean():.4f}")

# Choose best model (RandomForest in this case, change if needed)
best_model = RandomForestClassifier(n_estimators=100, random_state=42)
best_model.fit(X_train, y_train)

# Evaluate on test set
y_pred = best_model.predict(X_test)
print("\n✅ Test Set Evaluation for Random Forest:")
print(classification_report(y_test, y_pred))
print("Test Accuracy:", accuracy_score(y_test, y_pred))

# Save the model
joblib.dump(best_model, "model.joblib")
print("✅ Model saved as 'model.joblib'!")
