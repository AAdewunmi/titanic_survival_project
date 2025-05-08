import pandas as pd

"""
data_cleaning.py

This script loads and cleans the Titanic dataset (Kaggle version).
It handles missing values and saves a cleaned version for further analysis or
modeling.
"""


def load_and_clean_data(csv_path='data/titanic.csv') -> pd.DataFrame:
    """
    Load and clean the Titanic dataset.

    Steps performed:
    - Drop 'Cabin' column (too many missing values).
    - Fill missing 'Age' values with the median.
    - Fill missing 'Embarked' values with the mode.

    Parameters
    ----------
    csv_path : str, optional
        Path to the raw Titanic CSV file (default is 'data/titanic.csv').

    Returns
    -------
    pd.DataFrame
        Cleaned Titanic DataFrame.

    Example
    -------
    >>> df = load_and_clean_data('data/titanic.csv')
    >>> df.head()
    """
    # Load dataset
    df = pd.read_csv(csv_path)

    # Drop 'Cabin' column due to too many missing values
    if 'Cabin' in df.columns:
        df.drop(columns='Cabin', inplace=True)

    # Fill missing 'Age' values with the median
    if 'Age' in df.columns:
        median_age = df['Age'].median()
        df['Age'].fillna(median_age, inplace=True)

    # Fill missing 'Embarked' values with the most common value (mode)
    if 'Embarked' in df.columns:
        mode_embarked = df['Embarked'].mode()[0]
        df['Embarked'].fillna(mode_embarked, inplace=True)

    return df


if __name__ == "__main__":
    # Run script directly to clean the dataset and save the result
    cleaned_df = load_and_clean_data()
    output_path = 'data/titanic_cleaned.csv'
    cleaned_df.to_csv(output_path, index=False)
    print(f"✅ Cleaned dataset saved to: {output_path}")
