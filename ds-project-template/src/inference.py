from config import RAW_DATA_DIR, PROCESSED_DATA_DIR, MODEL_DIR, logger
import pandas as pd
import joblib

import joblib
import pandas as pd

def run_inference(threshold=0.38):
    # List file paths
    model_path = MODEL_DIR / 'modelv3.pkl'
    test_data_path = PROCESSED_DATA_DIR / 'test2022.csv'
    output_path = PROCESSED_DATA_DIR / 'ie2022_inferencev2.csv'

    ### Insert code here

    
if __name__ == "__main__":
    run_inference()
