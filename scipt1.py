import pandas as pd
import numpy as np
import logging
from sklearn.utils import resample

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_missing_values(df: pd.DataFrame, strategy: str = 'mean') -> pd.DataFrame:
    """
    Fills missing values using the specified strategy.
    
    Args:
    df (pd.DataFrame): The dataframe to be processed.
    strategy (str): The strategy for handling missing data ('mean', 'median', 'mode').

    Returns:
    pd.DataFrame: The dataframe with missing values handled.
    
    Raises:
    ValueError: If an unsupported strategy is provided.
    """
    if strategy not in ['mean', 'median', 'mode']:
        logging.error("Invalid strategy for handling missing values: %s", strategy)
        raise ValueError("Strategy not supported. Use 'mean', 'median', or 'mode'.")
    
    for column in df.columns:
        if df[column].isnull().any():
            if strategy == 'mean':
                df[column].fillna(df[column].mean(), inplace=True)
            elif strategy == 'median':
                df[column].fillna(df[column].median(), inplace=True)
            elif strategy == 'mode':
                df[column].fillna(df[column].mode()[0], inplace=True)
    
    logging.info("Missing values handled using %s strategy.", strategy)
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Removes duplicates from the dataframe.
    
    Args:
    df (pd.DataFrame): The dataframe from which to remove duplicates.

    Returns:
    pd.DataFrame: The dataframe with duplicates removed.
    """
    initial_count = df.shape[0]
    df.drop_duplicates(inplace=True)
    final_count = df.shape[0]
    logging.info("Removed %d duplicates.", initial_count - final_count)
    return df

def handle_outliers(df: pd.DataFrame, method: str = 'IQR', threshold: float = 1.5) -> pd.DataFrame:
    """
    Handles outliers in the dataframe using the specified method.
    
    Args:
    df (pd.DataFrame): The dataframe from which to remove outliers.
    method (str): The method for detecting outliers ('IQR' or 'Z-score').
    threshold (float): The threshold value for defining what is an outlier.

    Returns:
    pd.DataFrame: The dataframe with outliers handled.

    Raises:
    NotImplementedError: If an unsupported method is provided.
    """
    if method == 'IQR':
        for column in df.select_dtypes(include=[np.number]).columns:
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - (threshold * IQR)
            upper_bound = Q3 + (threshold * IQR)
            df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    elif method == 'Z-score':
        from scipy.stats import zscore
        df = df[(np.abs(zscore(df.select_dtypes(include=[np.number]))) < threshold).all(axis=1)]
    else:
        logging.error("Unsupported method for handling outliers: %s", method)
        raise NotImplementedError("Only 'IQR' and 'Z-score' methods are supported.")
    
    logging.info("Outliers handled using %s method.", method)
    return df

def handle_imbalanced_data(df: pd.DataFrame, target_column: str, method: str = 'upsampling') -> pd.DataFrame:
    """
    Perform handling of imbalanced data by either upsampling or downsampling.
    
    Args:
    df (pd.DataFrame): The dataframe to balance.
    target_column (str): The name of the target variable column.
    method (str): The technique for balancing ('upsampling' or 'downsampling').
    
    Returns:
    pd.DataFrame: The balanced dataframe.
    
    Raises:
    ValueError: If an unrecognized balancing method is specified.
    """
    if method not in ['upsampling', 'downsampling']:
        logging.error("Invalid method for handling imbalanced data: %s", method)
        raise ValueError("Balancing method not supported. Use 'upsampling' or 'downsampling'.")

    class_counts = df[target_column].value_counts()
    max_class = class_counts.idxmax() if method == 'downsampling' else class_counts.idxmin()
    min_class = class_counts.idxmin() if method == 'downsampling' else class_counts.idxmax()

    df_major = df[df[target_column] == max_class]
    df_minor = df[df[target_column] == min_class]

    if method == 'upsampling':
        df_minor_balanced = resample(df_minor, replace=True, n_samples=len(df_major), random_state=123)
        df_balanced = pd.concat([df_major, df_minor_balanced])
    else:  # 'downsampling'
        df_major_balanced = resample(df_major, replace=False, n_samples=len(df_minor), random_state=123)
        df_balanced = pd.concat([df_major_balanced, df_minor])

    logging.info("Data balanced using %s method on column %s.", method, target_column)
    return df_balanced

def handle_skewed_data(df: pd.DataFrame, method: str = 'log_transform') -> pd.DataFrame:
    """
    Handle skewed numerical data using transformations.
    
    Args:
    df (pd.DataFrame): The dataframe with skewed data.
    method (str): The method to use for handling skew ('log_transform' or 'sqrt_transform').
    
    Returns:
    pd.DataFrame: The dataframe with skewness reduced.
    
    Raises:
    ValueError: If an unrecognized method is specified.
    """
    if method not in ['log_transform', 'sqrt_transform']:
        logging.error("Invalid method for handling skewed data: %s", method)
        raise ValueError("Skew handling method not supported. Use 'log_transform' or 'sqrt_transform'.")

    numerical_cols = df.select_dtypes(include=[np.number]).columns

    for column in numerical_cols:
        if df[column].min() <= 0:
            df[column] += (-df[column].min() + 1)  # Making data positive if the log transform is chosen.

        if method == 'log_transform':
            df[column] = np.log(df[column])
        elif method == 'sqrt_transform':
            df[column] = np.sqrt(df[column])

    logging.info("Skewed data handled using %s method.", method)
    return df

def handle_data_discrepancies(df: pd.DataFrame, corrections: dict = None, custom_mappings: dict = None) -> pd.DataFrame:
    """
    Applies corrections and mappings to resolve discrepancies in categorical data.
    
    Args:
    df (pd.DataFrame): The dataframe with potential data discrepancies.
    corrections (dict): A dictionary mapping incorrect entries to correct ones.
    custom_mappings (dict): A dictionary describing column-specific mappings.
    
    Returns:
    pd.DataFrame: A dataframe with discrepancies handled.

    Example:
    corrections = {'NYC': 'New York', 'SF': 'San Francisco'}
    custom_mappings = {'country': {'USA': 'United States', 'UK': 'United Kingdom'}}
    """
    if corrections:
        for column in df.columns:
            df[column] = df[column].replace(corrections)
            logging.info(f"Applied global corrections for discrepancies in column: {column}")

    if custom_mappings:
        for column, mapping in custom_mappings.items():
            if column in df.columns:
                df[column] = df[column].replace(mapping)
                logging.info(f"Applied column-specific mappings for discrepancies in column: {column}")

    return df

def deal_with_data_sparsity(df: pd.DataFrame, threshold: float = 0.8) -> pd.DataFrame:
    """
    Remove columns with a high percentage of missing values.

    Args:
    df (pd.DataFrame): The dataframe to process.
    threshold (float): The threshold for determining sparsity. Columns with a higher fraction of missing values are removed.
    
    Returns:
    pd.DataFrame: Dataframe with sparse columns removed.
    """
    initial_columns = df.columns.size
    sparsity_threshold = threshold  # Columns with more than this percentage of missing values are considered sparse
    sparse_cols = [col for col in df.columns if df[col].isnull().mean() > sparsity_threshold]
    df.drop(sparse_cols, axis=1, inplace=True)
    final_columns = df.columns.size
    logging.info(f"Removed {initial_columns - final_columns} sparse columns with more than {threshold*100}% missing values.")
    return df

def handle_data_redundancy(df: pd.DataFrame, correlation_threshold: float = 0.9) -> pd.DataFrame:
    """
    Removes highly correlated redundant columns from the dataframe.

    Args:
    df (pd.DataFrame): The dataframe to process.
    correlation_threshold (float): The correlation threshold above which columns are considered redundant.
    
    Returns:
    pd.DataFrame: Dataframe with redundant columns removed based on correlation threshold.
    """
    corr_matrix = df.corr().abs()
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    redundant_columns = [column for column in upper.columns if any(upper[column] > correlation_threshold)]
    
    df.drop(redundant_columns, axis=1, inplace=True)
    logging.info(f"Removed {len(redundant_columns)} columns with correlation higher than {correlation_threshold}, which are: {redundant_columns}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    The function to clean the provided DataFrame using all individual cleaning functions.

    Args:
    df (pd.DataFrame): The data frame to clean.

    Returns:
    pd.DataFrame: The cleaned data frame.
    """
    try:
        df = handle_missing_values(df=df, strategy='mean')
        df = remove_duplicates(df=df)
        df = handle_outliers(df=df, method='IQR', threshold=1.5)
        df = handle_imbalanced_data(df=df, target_column='target_column', method='upsampling')
        df = handle_skewed_data(df=df, method='log_transform')
        # Additional cleaning functions would be called here.
        data = {
        'city': ['NYC', 'SF', 'N.Y.C', 'New York', 'San Francisco', 'SF'],
        'country': ['USA', 'USA', 'UK', 'USA', 'USA', 'USA'],
        'value': [1, 2, 3, 4, 5, 6]
        }
        df = pd.DataFrame(data)
        
        # Define corrections and custom mappings for handling discrepancies
        global_corrections = {'NYC': 'New York', 'SF': 'San Francisco', 'N.Y.C': 'New York'}
        country_mappings = {'country': {'USA': 'United States', 'UK': 'United Kingdom'}}
        
        # Clean the DataFrame
        df_cleaned = handle_data_discrepancies(df, corrections=global_corrections, custom_mappings=country_mappings)
        df_cleaned = deal_with_data_sparsity(df_cleaned, threshold=0.2)  # Setting low threshold for demonstration
        df_cleaned = handle_data_redundancy(df_cleaned)
    except Exception as e:
        logging.error("An error occurred in the cleaning process: %s", str(e))
        raise
    return df




# Main script
if __name__ == "__main__":
    # Example usage:
    # Assume `df` was read from some file or another source.
    df = pd.DataFrame({'columns': ['data']})  # Placeholder DataFrame creation
    df_cleaned = clean_data(df=df)
    logging.info("Data cleaning complete.")

