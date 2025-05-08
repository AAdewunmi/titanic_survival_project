import pandas as pd

"""
data_cleaning.py

This script loads and cleans the Titanic dataset (Kaggle version).
It processes missing values and saves a cleaned dataset for further analysis or 
modeling.
"""


def load_and_clean_data(csv_path='data/titanic.csv') -> pd.DataFrame:
    """
    Load and clean the Titanic dataset.

    This function performs the following cleaning steps:
    - Drops the 'Cabin' column due to excessive missing values.
    - Fills missing 'Age' values with the median of the column.
    - Fills missing 'Embarked' values with the most frequent port (mode).

    Parameters
    ----------
    csv_path : str, optional
        Path to the raw Titanic CSV file. Default is 'data/titanic.csv'.

    Returns
    -------
    pd.DataFrame
        A cleaned pandas DataFrame with processed missing values.

    Example
    -------
    >>> df = load_and_clean_data('data/titanic.csv')  # Load and clean dataset
    >>> df.head()  # Check first few rows of cleaned dataset
    """
    # Step 1: Load the Titanic dataset from the given CSV file
    df = pd.read_csv(csv_path)

    # Step 2: Drop the 'Cabin' column (if exists)
    # because it has too many missing values
    if 'Cabin' in df.columns:
        df.drop(columns='Cabin', inplace=True)

    # Step 3: Fill missing 'Age' values with the median age
    # from the 'Age' column
    if 'Age' in df.columns:
        median_age = df['Age'].median()
        df['Age'].fillna(median_age, inplace=True)

    # Step 4: Fill missing 'Embarked' values with the most frequent
    # Embarked value (mode)
    if 'Embarked' in df.columns:
        # Get the most frequent embarkation port
        mode_embarked = df['Embarked'].mode()[0]
        df['Embarked'].fillna(mode_embarked, inplace=True)

    # Return the cleaned DataFrame
    return df


if __name__ == "__main__":
    """
    If the script is executed directly, clean the dataset and save the cleaned
    data.
    """
    # Load, clean, and save the dataset
    cleaned_df = load_and_clean_data()

    # Define the output file path for the cleaned dataset
    output_path = 'data/titanic_cleaned.csv'

    # Save the cleaned DataFrame to a new CSV file
    cleaned_df.to_csv(output_path, index=False)

    # Inform the user that the cleaning process is complete
    print(f"✅ Cleaned dataset has been saved to: {output_path}")
