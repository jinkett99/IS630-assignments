from config import RAW_DATA_DIR, PROCESSED_DATA_DIR
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import pandas as pd


def advanced_describe(df):
    """
    Function to generate descriptive statistics for numerical variables in the employee dataset.

    Parameters:
    df (pd.DataFrame): The employee dataset.

    Returns:
    pd.DataFrame: A DataFrame containing descriptive statistics for numerical variables.
    """
    # Selecting only numerical columns from the dataframe
    numerical_df = df.select_dtypes(include=['number'])

    # Drop any irrelevant column like 'Employee ID' or 'Name' if needed
    if 'Name' in numerical_df.columns:
        numerical_df = numerical_df.drop(columns=['Name'])

    # Generate descriptive statistics
    descriptive_stats = numerical_df.describe().transpose()

    # Add additional statistics: Median and Range
    descriptive_stats['median'] = numerical_df.median()
    descriptive_stats['range'] = numerical_df.max() - numerical_df.min()

    # Rename index to include column names
    descriptive_stats.index.name = 'Variable'

    return descriptive_stats

def plot_descriptive_stats():
    # Import dataframe
    file_path = RAW_DATA_DIR / "employee_data.csv"
    df = pd.read_csv(file_path)

    # Remove columns if it exists
    if "Name" in df.columns:
        df = df.drop(columns=["Name", "DOJ", "Position"])

    # Separate numerical and categorical columns
    num_cols = df.select_dtypes(include=['number']).columns
    cat_cols = df.select_dtypes(include=['object', 'category']).columns

    # Set the general aesthetic style of the plots
    sns.set(style="whitegrid")

    # Plot histograms for numerical columns
    for col in num_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True, bins=30, color='skyblue')
        plt.title(f'Histogram for {col}', fontsize=14)
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    # Plot count plots for categorical columns
    for col in cat_cols:
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x=col, palette='Set2')
        plt.title(f'Count Plot for {col}', fontsize=14)
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
