import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


class EDAStatisticalAnalysis:
    """
    This class provides static methods for performing statistical analyses 
    commonly used in exploratory data analysis (EDA) including descriptive 
    statistics, correlation matrix, error analysis, ANOVA, linear regression,
    and model validation.
    """

    @staticmethod
    def descriptive_statistics(df):
        """
        Computes descriptive statistics for all numeric columns in the DataFrame.
        :param df: pandas DataFrame with numeric data.
        :return: Descriptive statistics (mean, std, min, max, etc.) for each column.
        """
        return df.describe()

    @staticmethod
    def correlation_matrix(df):
        """
        Computes the correlation matrix between all numeric columns in the DataFrame.
        :param df: pandas DataFrame with numeric data.
        :return: Correlation matrix of the numeric columns.
        """
        try:
            corr = df.corr()
            if corr.empty:
                raise ValueError("Unable to compute correlations.")
            return corr
        except Exception as e:
            return str(e)

    @staticmethod
    def error_analysis(df, reference_col, measurement_cols):
        """
        Calculates the absolute and relative errors between the reference column 
        and the measurement columns.
        :param df: pandas DataFrame with the data.
        :param reference_col: Column name of the reference values.
        :param measurement_cols: List of column names for measurements.
        :return: Tuple of (absolute errors, relative errors).
        """
        try:
            if reference_col not in df.columns:
                raise ValueError(f"Reference column '{reference_col}' not found in DataFrame.")
            if any(col not in df.columns for col in measurement_cols):
                raise ValueError("One or more measurement columns not found in DataFrame.")
            
            # Compute absolute and relative errors
            error_abs = df[measurement_cols].subtract(df[reference_col], axis=0).abs()
            error_rel = error_abs.div(df[reference_col], axis=0).replace([np.inf, -np.inf], np.nan).fillna(0)
            return error_abs, error_rel
        except Exception as e:
            return str(e), None

    @staticmethod
    def anova_test(df, measurement_cols):
        """
        Performs ANOVA (Analysis of Variance) on the measurement columns.
        Requires at least two measurement columns.
        :param df: pandas DataFrame with the data.
        :param measurement_cols: List of measurement column names.
        :return: F-value and p-value from ANOVA test.
        """
        try:
            if len(measurement_cols) < 2:
                raise ValueError("At least two columns are required for ANOVA.")
            measurements = [df[col] for col in measurement_cols if col in df.columns]
            f_val, p_val = stats.f_oneway(*measurements)
            return f_val, p_val
        except Exception as e:
            return str(e), None

    @staticmethod
    def linear_regression_model(df, reference_col, measurement_cols):
        """
        Fits a linear regression model (either simple or multiple) using the 
        measurement columns to predict the reference column.
        :param df: pandas DataFrame with the data.
        :param reference_col: Column name of the reference values.
        :param measurement_cols: List of measurement column names.
        :return: Trained LinearRegression model and predictions.
        """
        try:
            if reference_col not in df.columns:
                raise ValueError(f"Reference column '{reference_col}' not found in DataFrame.")
            
            # Prepare data for regression
            X = df[measurement_cols].values if len(measurement_cols) > 1 else df[[measurement_cols[0]]].values
            y = df[reference_col].values
            model = LinearRegression()
            model.fit(X, y)
            predictions = model.predict(X)
            return model, predictions
        except Exception as e:
            return str(e), None

    @staticmethod
    def model_validation(y_true, y_pred):
        """
        Validates the regression model by calculating MSE, MAE, and R2.
        :param y_true: True reference values.
        :param y_pred: Predicted values from the model.
        :return: Dictionary with validation metrics (MSE, MAE, R2).
        """
        try:
            mse = mean_squared_error(y_true, y_pred)
            mae = mean_absolute_error(y_true, y_pred)
            r2 = r2_score(y_true, y_pred)
            return {"MSE": mse, "MAE": mae, "R2": r2}
        except Exception as e:
            return str(e)

    @staticmethod
    def residual_analysis(y_true, y_pred):
        """
        Calculates the residuals of the model (true values - predicted values).
        :param y_true: True reference values.
        :param y_pred: Predicted values from the model.
        :return: Residuals (difference between actual and predicted values).
        """
        try:
            return y_true - y_pred
        except Exception as e:
            return str(e)

    @staticmethod
    def summary_statistics(df, reference_col, measurement_cols):
        """
        Provides a summary of the key statistical findings including descriptive 
        statistics, correlation matrix, error analysis, and ANOVA results.
        :param df: pandas DataFrame with the data.
        :param reference_col: Column name of the reference values.
        :param measurement_cols: List of measurement column names.
        :return: Dictionary summarizing all statistical outputs.
        """
        try:
            desc_stats = EDAStatisticalAnalysis.descriptive_statistics(df)
            corr_matrix = EDAStatisticalAnalysis.correlation_matrix(df)
            error_abs, error_rel = EDAStatisticalAnalysis.error_analysis(df, reference_col, measurement_cols)
            anova_result = EDAStatisticalAnalysis.anova_test(df, measurement_cols)

            return {
                "Descriptive Statistics": desc_stats,
                "Correlation Matrix": corr_matrix,
                "Absolute Errors": error_abs,
                "Relative Errors": error_rel,
                "ANOVA Result": anova_result
            }
        except Exception as e:
            return {"Error": str(e)}


import matplotlib.pyplot as plt
import seaborn as sns

class EDAGraphicalAnalysis:
    """
    This class provides static methods for generating common visualizations used 
    in exploratory data analysis (EDA), including histograms, boxplots, correlation 
    heatmaps, scatter plots, and residual plots.
    """

    @staticmethod
    def plot_distributions(df, cols, title='Sensor Distributions'):
        """
        Generates histograms for the selected columns.
        :param df: pandas DataFrame with the data.
        :param cols: List of column names to plot.
        :param title: Title for the plot.
        """
        try:
            df[cols].hist(bins=15, figsize=(15, 10))
            plt.suptitle(title)
            plt.show()
        except Exception as e:
            print(f"Error generating histograms: {e}")

    @staticmethod
    def plot_boxplots(df, cols, title='Measurement Boxplots'):
        """
        Generates boxplots for the selected measurement columns.
        :param df: pandas DataFrame with the data.
        :param cols: List of column names to plot.
        :param title: Title for the plot.
        """
        try:
            df[cols].plot(kind='box', figsize=(10, 8))
            plt.title(title)
            plt.show()
        except Exception as e:
            print(f"Error generating boxplots: {e}")

    @staticmethod
    def plot_correlation_matrix(df, title='Correlation Matrix'):
        """
        Generates a heatmap of the correlation matrix.
        :param df: pandas DataFrame with the data.
        :param title: Title for the plot.
        """
        try:
            plt.figure(figsize=(10, 8))
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
            plt.title(title)
            plt.show()
        except Exception as e:
            print(f"Error generating correlation matrix: {e}")

    @staticmethod
    def plot_error_trends(df, reference_col, measurement_cols):
        """
        Generates scatter plots showing the relationship between the reference values 
        and the measurements for each sensor.
        :param df: pandas DataFrame with the data.
        :param reference_col: Column name of the reference values.
        :param measurement_cols: List of measurement column names.
        """
        try:
            plt.figure(figsize=(10, 6))
            for col in measurement_cols:
                plt.scatter(df[reference_col], df[col], label=f'Measurement {col}')
            plt.plot(df[reference_col], df[reference_col], color='red', label='Reference Value')
            plt.xlabel('Reference Value')
            plt.ylabel('Measurements')
            plt.legend()
            plt.title('Measurements vs Reference Value')
            plt.show()
        except Exception as e:
            print(f"Error generating error trends plot: {e}")

    @staticmethod
    def plot_residuals(y_true, residuals, title='Residual Plot'):
        """
        Generates a scatter plot of residuals (errors between true and predicted values).
        :param y_true: True reference values.
        :param residuals: Residuals (true values - predicted values).
        :param title: Title for the plot.
        """
        try:
            plt.scatter(y_true, residuals)
            plt.axhline(0, color='red', linestyle='--')
            plt.title(title)
            plt.xlabel('Reference Value')
            plt.ylabel('Residuals')
            plt.show()
        except Exception as e:
            print(f"Error generating residual plot: {e}")
