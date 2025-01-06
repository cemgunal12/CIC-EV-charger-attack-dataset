# CIC-EV-charger-attack-dataset
# EVSE-A Idle Vulnerability Scan Dataset Analysis

This project analyzes the EVSE-A Idle Vulnerability Scan dataset using data mining and machine learning techniques to detect and classify security vulnerabilities.

---

## **Overview**
- **Dataset**: EVSE-A Idle Vulnerability Scan dataset from [UNB CIC](https://www.unb.ca/cic/datasets/evse-dataset-2024.html).
- **Objective**:
  - Preprocess data to handle missing values and encode categorical features.
  - Perform exploratory data analysis (EDA) for feature understanding.
  - Train and evaluate a Random Forest model to classify vulnerabilities.

---

## **Directory Structure**
├── data │ 
  └── EVSE-A-idle-vulnerability-scan.csv # Dataset used for analysis
├── dataset.py # Python script for preprocessing, EDA, and modeling 
├── README.md # Project documentation 
  └── results 
├── feature_importance.png # Feature importance visualization
  └── confusion_matrix.png # Confusion matrix visualization





## **Setup and Installation**
### **Prerequisites**
Ensure the following packages are installed:
- Python 3.8+
- Pandas
- Scikit-learn
- Seaborn
- Matplotlib
- Imbalanced-learn

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/evse-dataset-analysis.git
   cd evse-dataset-analysis
   ````
   2. Install dependencies
   ````bash
    pip install -r requirements.txt


### **EXECUTION**
   ```bash
   python dataset
````

## **Sample Data**
1-The dataset EVSE-A-idle-vulnerability-scan.csv is included in the data directory.
2-This dataset is automatically loaded when the script is executed.
3-To use your own dataset, replace the file in the data directory and ensure it follows the same format.



## Key Analysis Steps
1. **Preprocessing**:
   - Missing values handled using mean for numeric and mode for categorical features.
   - Categorical data encoded using `LabelEncoder`.

2. **EDA**:
   - Generated visualizations: histograms, correlation matrix, and boxplots.

3. **Model Training and Evaluation**:
   - Random Forest was selected for classification.
   - Achieved metrics:
     - **Precision**: 100%
     - **Recall**: 100%
     - **F1-Score**: 100%

## Limitations and Future Work
- **Class Imbalance**:
  - Dataset includes only one class, limiting generalization.
  - SMOTE or similar techniques recommended for future work.
- **Dimensionality Reduction**:
  - PCA or similar techniques could optimize feature space.










