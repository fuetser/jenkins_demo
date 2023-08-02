import pandas as pd
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns

# Load Titanic dataset from Seaborn
sns.set(style="whitegrid")
titanic = sns.load_dataset("titanic")

# Preprocessing
# Remove unnecessary columns
titanic = titanic.drop(['alive', 'embark_town', 'who', 'adult_male'], axis=1)

# Convert 'deck' column to categorical type with predefined categories
categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'Unknown']
titanic['deck'] = pd.Categorical(titanic['deck'], categories=categories)

# Fill missing values in the 'deck' column with a new category 'Unknown'
titanic['deck'].fillna('Unknown', inplace=True)

# Fill missing values in the 'embarked' column with the most frequent value
titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)

# Convert categorical variables to numerical using one-hot encoding
titanic = pd.get_dummies(titanic, columns=['sex', 'embarked', 'class', 'deck'], drop_first=True)

# Split the dataset into features and target variable
X = titanic.drop('survived', axis=1)
y = titanic['survived']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the CatBoost classifier
model = CatBoostClassifier(iterations=10000,  # Number of boosting iterations
                           learning_rate=0.1,  # Learning rate for gradient boosting
                           depth=6,  # Maximum depth of the tree
                           loss_function='Logloss',  # Loss function for binary classification
                           verbose=100)  # Print progress every 100 iterations

# Train the model
model.fit(X_train, y_train, eval_set=(X_test, y_test), early_stopping_rounds=50, verbose_eval=100)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
