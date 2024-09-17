Repository Structure:
Repository/
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── ...
├── data/
│   ├── raw/
│   ├── processed/
│   └── ...
├── models/
│   ├── trained_model.pkl
│   ├── model_evaluation_report.txt
│   └── ...
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── model_training.ipynb
│   └── ...
└── .gitignore

Summary: 
- Include functions to call in "src" folder
- Raw datasets should be in "data/raw"
- Output/Processed datasets should be in "data/processed"