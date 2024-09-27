import pandas as pd
import pickle
import re
import csv
import numpy as np
import joblib
import datetime
import os

class DataLoader:
    
    @staticmethod
    def transform_json_keys(input_data: pd.DataFrame, mapping: dict) -> pd.DataFrame:
        """
        Transforms the keys of input_data based on the provided mapping dictionary.
        Assumes input_data is a DataFrame with columns that need to be renamed.

        Parameters:
        input_data (pd.DataFrame): The DataFrame with columns that need to be renamed.
        mapping (dict): A dictionary that maps the original column names to the new column names expected by the model.

        Returns:
        pd.DataFrame: A new DataFrame with transformed column names.
        """
        # Verificar y mapear cada columna del DataFrame
        new_columns = []
        for col in input_data.columns:
            if col in mapping:
                new_columns.append(mapping[col])
            else:
                # Si no se encuentra mapeo, lanzar una advertencia o manejar el caso
                raise KeyError(f"La columna '{col}' no tiene un mapeo en el modelo.")

        # Renombrar las columnas del DataFrame según el mapeo
        input_data.columns = new_columns
        
        return input_data

    
    @staticmethod
    def apply_mapping(input_data, diccionary: dict) -> pd.DataFrame:
        """
        Applies a mapping dictionary to the data (X) by iterating through columns and applying
        the corresponding mapping manually.

        Parameters:
        input_data (pd.DataFrame): The input data as a pandas DataFrame. 
        diccionary (dict): A dictionary containing the mapping for each column.

        Returns:
        DataFrame: The transformed data with mapped features.
        """
        # Iterar sobre las columnas del diccionario de mapeo
        for column, mapping in diccionary.items():
            if column in input_data.columns:
                # Aplicar el mapeo de valores para cada columna de manera individual
                input_data[column] = input_data[column].map(mapping)
        
        return input_data

    @staticmethod
    def save_array_to_txt( array, filename_path):
        """
        Save a given array to a text file in CSV format.

        Parameters:
        array (array-like): The array to be saved. It can be a list or a numpy array.
        filename_path (str): The name of the file to save the array to.

        Returns:
        None
        """
        # Construct the full path for the output file
        path = filename_path
        
        # Ensure the input is a numpy array
        if not isinstance(array, np.ndarray):
            array = np.array(array)
        
        # Save the array to a text file with comma as the delimiter
        np.savetxt(path, array, delimiter=',', fmt='%s', newline='\n')

    @staticmethod
    def load_data_csv(filename_path, encoding='latin1', delimiter=';'):
        """
        Load data from a CSV file and attempt to convert columns to numeric types.

        Parameters:
        filename_path (str): The name of the CSV file to be loaded.
        encoding (str, optional): The encoding of the CSV file. Default is 'latin1'.
        delimiter (str, optional): The delimiter used in the CSV file. Default is ';'.

        Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame. If there is a parsing error, returns None.
        """
        path = f"{filename_path}"
        try:
            data = pd.read_csv(path, encoding=encoding, delimiter=delimiter, header=0, quoting=csv.QUOTE_NONE, decimal=',')
            for column in data.columns:
                original_data = data[column].copy()
                data[column] = pd.to_numeric(data[column], errors='coerce')
                if data[column].isna().any():
                    data[column] = original_data
        except pd.errors.ParserError as e:
            print(f"Error reading the file: {e}")
            return None
        return data

    @staticmethod
    def save_data_to_csv(data: pd.DataFrame, filename_path: str, encoding='utf-8', index=False):
        """
        Save a pandas DataFrame to a CSV file.

        Parameters:
        data (pd.DataFrame): The DataFrame to be saved.
        filename_path (str): The path (including filename) where the CSV will be saved.
        encoding (str, optional): The encoding of the CSV file. Default is 'utf-8'.
        index (bool, optional): Whether to write row names (index). Default is False.

        Returns:
        None
        """
        data.to_csv(filename_path, encoding=encoding, index=index, quoting=csv.QUOTE_NONE, sep=',')

    @staticmethod
    def load_data_txt_to_array( filename_path, delimiter='\n', encoding='utf-8'):
        """
        Load data from a text file and return it as a NumPy array of strings.

        Parameters:
        folder_name (str): The name of the folder containing the file.
        filename_path (str): The name of the text file to be loaded.
        delimiter (str, optional): The delimiter used to separate values in the text file. Default is '\n'.
        encoding (str, optional): The encoding of the text file. Default is 'utf-8'.

        Returns:
        np.ndarray: A NumPy array containing the data from the text file.
        """
        path = f"{filename_path}"
        return np.genfromtxt(path, delimiter=delimiter, dtype=str, encoding=encoding)
    
    @staticmethod
    def save_data_pickle( data, filename_path, filter_condition=None):
        """
        Save data to a pickle file, optionally filtering it based on a condition.

        Parameters:
        data (DataFrame): The data to be saved.
        filename_path (str): The name of the file to save the data in.
        filter_condition (str, optional): A condition to filter the data before saving. Defaults to None.

        Returns:
        None
        """
        # Construct the full path for the output file
        path = f"{filename_path}"
        
        # If a filter condition is provided, filter the data
        if filter_condition:
            data = data.query(filter_condition)
        
        # Open the file in write-binary mode and save the data using pickle
        with open(path, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def load_data_pickle(namefile_path):
        with open( namefile_path, 'rb') as f:
            return pickle.load(f)

        
    @staticmethod
    def save_model( filename_path, model):
        """
        Save a machine learning model to a file with a timestamped filename.

        Parameters:
        model (object): The machine learning model to be saved.
        filename_path (str): The base name for the model file.

        Returns:
        str: The name of the saved model file.
        """
        # Get the current date and time as a string formatted as 'YYYY-MM-DD_HH-MM-SS'
        date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        full_filename = f"{filename_path}#{date_str}.pkl"
        joblib.dump(model, full_filename)
        
        # Return the name of the saved model file
        return full_filename
    
    @staticmethod
    def load_model(filename_path):
        """
        Load a machine learning model from a specified file.

        Parameters:
        filename_path (str): The name of the model file to be loaded.

        Returns:
        object: The loaded machine learning model.
        """
        return joblib.load(filename_path)
    
    @staticmethod
    def get_last_trained_model_name(base_path):
        """
        Get the name of the last trained model based on the timestamp in the filename.

        Parameters:
        base_path (str): The path to the directory containing the model files.

        Returns:
        str: The name of the last trained model file.
        """
        # List all files in the directory
        files = os.listdir(base_path)
        model_files = [file for file in files if file.endswith('.pkl')]

        if not model_files:
            return None
        
        model_files.sort(key=lambda x: datetime.datetime.strptime(x.split('#')[-1].replace('.pkl', ''), "%Y-%m-%d_%H-%M-%S"), reverse=True)
        return os.path.join(base_path, model_files[0])
    