"""
Data Fetching and User Splitting for MovieLens Dataset

This module provides utility functions to download, extract, and load data from the MovieLens 1M dataset.
It ensures that the dataset is fetched seamlessly and is readily available for analysis or modeling purposes
in a structured format. Additionally, it offers a function to create train, validation, and test splits based on user IDs.

Functions included are:
    - download_and_extract_movielens_1m(data_dir: str): Downloads the MovieLens 1M dataset and extracts its contents into a specified directory.
    - load_movielens_ratings(data_dir: str): Loads the ratings data from the MovieLens 1M dataset into a pandas DataFrame.
    - load_movielens_users(data_dir: str): Loads the user data from the MovieLens 1M dataset into a pandas DataFrame.
    - load_movielens_movies(data_dir: str): Loads the movie data from the MovieLens 1M dataset into a pandas DataFrame.
    - create_user_splits(dataframe: pd.DataFrame, data_dir: str, seed: int): Creates train/validation/test splits for user IDs and saves them to CSV files.
"""


import urllib.request
import zipfile
import os
import pandas as pd
from sklearn.model_selection import train_test_split


def download_and_extract_movielens_1m(data_dir: str = "data") -> None:
    """
    Downloads the MovieLens 1M dataset, extracts its contents into a specified directory.

    Args:
    - data_dir (str): The directory where the dataset should be saved and extracted.

    Returns:
    - None
    """
    # Define the URL and filename for the zip file
    url = "https://files.grouplens.org/datasets/movielens/ml-1m.zip"
    zip_filepath = os.path.join(data_dir, "ml-1m.zip")
    extraction_path = os.path.join(data_dir, "ml-1m")

    # Check if the data directory exists, if not, create it
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download the dataset only if it's not already present
    if not os.path.exists(zip_filepath):
        print(f"Downloading MovieLens 1M dataset to {zip_filepath}...")
        urllib.request.urlretrieve(url, zip_filepath)
        print("Download completed!")
    else:
        print(f"Dataset already exists at {zip_filepath}.")

    # If the extracted directory doesn't exist, extract the zip file
    if not os.path.exists(extraction_path):
        print(f"Extracting {zip_filepath} to {extraction_path}...")
        with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print("Extraction completed!")
    else:
        print(f"Extracted files already exist in {extraction_path}.")


def load_movielens_ratings(data_dir: str = "data") -> pd.DataFrame:
    """
    Loads the MovieLens 1M ratings dataset into a pandas DataFrame.

    Args:
    - data_dir (str): The directory where the dataset is saved.

    Returns:
    - df (pd.DataFrame): DataFrame containing the ratings data.
    """
    csv_filepath = os.path.join(data_dir, "ml-1m", "ratings.dat")
    col_names = ['user_id', 'movie_id', 'rating', 'timestamp']
    df = pd.read_csv(csv_filepath, sep="::", header=None, names=col_names, engine='python', encoding='ISO-8859-1')
    return df


def load_movielens_users(data_dir: str = "data") -> pd.DataFrame:
    """
    Loads the MovieLens 1M users dataset into a pandas DataFrame.

    Args:
    - data_dir (str): The directory where the dataset is saved.

    Returns:
    - df (pd.DataFrame): DataFrame containing the users data.
    """
    csv_filepath = os.path.join(data_dir, "ml-1m", "users.dat")
    col_names = ['user_id', 'gender', 'age', 'occupation', 'zip_code']
    df = pd.read_csv(csv_filepath, sep="::", header=None, names=col_names, engine='python', encoding='ISO-8859-1')
    return df


def load_movielens_movies(data_dir: str = "data") -> pd.DataFrame:
    """
    Loads the MovieLens 1M movies dataset into a pandas DataFrame.

    Args:
    - data_dir (str): The directory where the dataset is saved.

    Returns:
    - df (pd.DataFrame): DataFrame containing the movies data.
    """
    csv_filepath = os.path.join(data_dir, "ml-1m", "movies.dat")
    col_names = ['movie_id', 'title', 'genres']
    df = pd.read_csv(csv_filepath, sep="::", header=None, names=col_names, engine='python', encoding='ISO-8859-1')
    return df


def create_user_splits(dataframe: pd.DataFrame, data_dir: str = "data/splits", seed: int = 42):
    """
    Create train/validation/test splits for user IDs and save them to CSV files.

    Args:
    - dataframe (pd.DataFrame): The DataFrame containing the 'user_id' column.
    - data_dir (str): Directory where the split files will be saved.
    - seed (int): Random seed for reproducibility.

    Returns:
    None
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Extract the unique user IDs
    user_ids = dataframe['user_id'].unique()

    # Create train/validation/test splits
    train_ids, temp_ids = train_test_split(user_ids, test_size=0.4, random_state=seed)
    val_ids, test_ids = train_test_split(temp_ids, test_size=0.5, random_state=seed)

    # Convert to DataFrames for easy CSV writing
    df_train = pd.DataFrame(train_ids, columns=['user_id'])
    df_val = pd.DataFrame(val_ids, columns=['user_id'])
    df_test = pd.DataFrame(test_ids, columns=['user_id'])

    # Save to CSV files
    df_train.to_csv(os.path.join(data_dir, 'train_users.csv'), index=False)
    df_val.to_csv(os.path.join(data_dir, 'val_users.csv'), index=False)
    df_test.to_csv(os.path.join(data_dir, 'test_users.csv'), index=False)


if __name__ == "__main__":
    # Call the function to download and extract the dataset
    download_and_extract_movielens_1m()

    # Loading data
    df_ratings = load_movielens_ratings()
    df_users = load_movielens_users()
    df_movies = load_movielens_movies()

    print("Ratings Data:")
    print(df_ratings.head())

    print("\nUsers Data:")
    print(df_users.head())

    print("\nMovies Data:")
    print(df_movies.head())

    # Creating dataset split on users
    create_user_splits(df_users)
