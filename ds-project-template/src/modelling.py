from config import RAW_DATA_DIR, PROCESSED_DATA_DIR, MODEL_DIR, logger
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report
from scipy.stats import randint
import argparse
import joblib
import os

def train_eval_model(): 
    train_path = PROCESSED_DATA_DIR / 'train.csv'
    train = pd.read_csv(train_path)

    ### Insert code here

    if __name__ == "__main__":
        train_eval_model()