from config import RAW_DATA_DIR, PROCESSED_DATA_DIR, logger
import pandas as pd
import pyreadstat
import argparse
import os

def load_data(filename):
    """Load data from a file based on its extension."""
    file_path = RAW_DATA_DIR / filename
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension == '.csv':
        logger.info(f"Loading CSV file from {file_path}")
        return pd.read_csv(file_path)
    elif file_extension == '.sas7bdat':
        logger.info(f"Loading SAS file from {file_path}")
        df, meta = pyreadstat.read_sas7bdat(file_path)
        return df
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")

def save_data(df, filename):
    """Save data to a file."""
    df.to_csv(PROCESSED_DATA_DIR / filename, index=False)

# def main():
#     parser = argparse.ArgumentParser(description='Data processing script.')
#     subparsers = parser.add_subparsers(dest='command', help='Sub-command help')

#     # Sub-parser for the load_data function
#     parser_load = subparsers.add_parser('load', help='Load data from a file')
#     parser_load.add_argument('input_filename', type=str, help='The input filename')

#     # Sub-parser for the save_data function
#     parser_save = subparsers.add_parser('save', help='Save data to a file')
#     parser_save.add_argument('input_filename', type=str, help='The input filename')
#     parser_save.add_argument('output_filename', type=str, help='The output filename')

# if __name__ == "__main__":
#     main()