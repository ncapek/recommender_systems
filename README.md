# Movie Recommender System Exploration

# Objective
The primary aim of this project is educational. We are working to familiarize ourselves with various approaches to building recommender systems, focusing on movie recommendation. While the ultimate goal is not to build the most sophisticated recommender system, the methodologies and techniques employed here could be instrumental in our professional projects, particularly for recommending products in industries like insurance.

# Dataset
We are utilizing the MovieLens dataset, which consists of several tables:

- movies: Includes details such as movie ID, title, and genres.
- ratings: Contains the movie ratings given by different users.
- users: Provides demographic information about the users.

The MovieLens dataset is a widely used resource for building movie recommendation systems and serves as an excellent basis for understanding the intricacies of recommender algorithms.

# Modules
The project is organized into the following modules:

- mapping_tables: Contains mapping tables to convert categorical variables into numerical or Boolean values.
- data_fetching: Responsible for downloading and loading the dataset.
- data_preprocessing: Includes functions for feature engineering and data transformation.

# Approaches
## Methods of Dataset/Task Construction
We'll be exploring two distinct methods for constructing our machine learning tasks, as outlined in this paper.

### Method 1: Random Masking
In this approach, we focus on the user's current set of rated movies. One movie is randomly masked to serve as the target variable for prediction. The model will predict which movie was masked, based on the premise that the user gave it a positive or at least neutral rating.

### Method 2: Sequential
This method takes into account the temporal sequence of user interactions, aiming to predict whether a user will like a given movie, considering their historical evolution of ratings.

# Modeling Approaches
We plan to test various machine learning models to understand their performance and characteristics:

- Static View: A user's history of rated movies will be used to predict the next movie they might like. Models like decision trees, random forests, and gradient boosting machines will be tested.

- Sequential Approaches: These methods account for the temporal sequence of user actions. The algorithms we aim to explore include:

  - Recurrent Neural Networks (RNNs)
  - 1D Convolutional Neural Networks
  - Transformers

# Train/Test Split
To mimic real-world conditions and ensure a robust model evalution, we're employing a user-based train/test split, segregating unique user IDs into separate training, validation, and test sets.

# Setup
The user of this repository is advised to setup a virtual environment using the `requirements.txt` file and running the `data_fetching.py` script to download and prepare the necessary dataset.