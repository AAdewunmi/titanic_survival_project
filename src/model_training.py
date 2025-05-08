import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

"""
model_training.py

This script loads the cleaned Titanic dataset, prepares the data, trains a
logistic
regression model to predict survival, evaluates its performance, and saves the
trained model and encoders.
"""


def train_and_save_model(
    csv_path='data/titanic_cleaned.csv',
    model_output_path='models/logistic_model.pkl',
    encoder_output_paths={
        'sex': 'models/encoder_sex.pkl',
        'embarked': 'models/encoder_embarked.pkl'
    }
):
    """
    Train a logistic regression model on the Titanic dataset and save the
    trained model and label encoders.

    The function performs the following steps:
    - Loads the cleaned Titanic dataset.
    - Prepares the features (X) and target (y).
    - Encodes categorical variables (Sex and Embarked) using LabelEncoder.
    - Splits the dataset into training and testing sets.
    - Trains a logistic regression model.
    - Evaluates the model using accuracy and classification report.
    - Saves the trained model and label encoders to specified file paths.

    Parameters
    ----------
    csv_path : str, optional
        Path to the cleaned Titanic CSV file
        (default is 'data/titanic_cleaned.csv').
          
    model_output_path : str, optional
        Path where the trained model will be saved 
        (default is 'models/logistic_model.pkl').

    encoder_output_paths : dict, optional
        Dictionary containing the paths for saving the label encoders for
        categorical features.
        The keys are 'sex' and 'embarked', and the values are paths where each
        encoder will be saved.

    Returns
    -------
    None

    Example
    -------
    >>> train_and_save_model()
    """
    # Step 1: Load the cleaned Titanic dataset
    df = pd.read_csv(csv_path)

    # Step 2: Define features (X) and target (y)
    X = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
    y = df['Survived']

    # Step 3: Encode categorical features (Sex, Embarked) using LabelEncoder
    le_sex = LabelEncoder()
    le_embarked = LabelEncoder()

    # Encode 'Sex' column
    X['Sex'] = le_sex.fit_transform(X['Sex'])

    # Encode 'Embarked' column
    X['Embarked'] = le_embarked.fit_transform(X['Embarked'])

    # Step 4: Split the data into training and testing sets (80%/20%)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Step 5: Train the Logistic Regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Step 6: Evaluate the model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Step 7: Save the trained model and label encoders
    joblib.dump(model, model_output_path)
    joblib.dump(le_sex, encoder_output_paths['sex'])
    joblib.dump(le_embarked, encoder_output_paths['embarked'])

    print(
        f"✅ Model and encoders saved to: {model_output_path}, "
        f"{encoder_output_paths['sex']}, {encoder_output_paths['embarked']}"
    )


if __name__ == "__main__":
    """
    Run the function to train and save the model if this script is executed
    directly.
    """
    train_and_save_model()
