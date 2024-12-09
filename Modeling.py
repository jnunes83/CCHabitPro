"""
Modeling Class to handle predictive modeling for habit recommendations.
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from tensorflow import keras

class HabitModel:
    def __init__(self):
        self.model = None

    def train_model(self, data):
        """
        Trains a predictive model using the provided data.
        
        Parameters
        ----------
        data: pd.DataFrame
            A DataFrame containing features and labels.
        """
        X = data.drop('target', axis=1)  # Assuming 'target' is the label column
        y = data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)
        print("Model trained successfully.")

    def predict(self, new_data):
        """
        Makes predictions based on the trained model.
        
        Parameters
        ----------
        new_data: np.array
            New data for which predictions are to be made.
        """
        if self.model:
            return self.model.predict(new_data)
        else:
            print("Model is not trained yet.")

    def create_tensorflow_model(self, input_shape):
        """
        Creates and compiles a TensorFlow model.
        
        Parameters
        ----------
        input_shape: tuple
            Shape of the input data.
        """
        model = keras.Sequential([
            keras.layers.Dense(64, activation='relu', input_shape=input_shape),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')  # Binary classification
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        self.model = model