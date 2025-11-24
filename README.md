# Diabetes Risk Prediction System

## Overview
A machine learning-based console application that predicts the risk of diabetes in individuals based on their health parameters. The system uses a Random Forest classifier trained on synthetic medical data, providing accurate risk assessments with proper SI units and comprehensive error handling. The interface guides users through gender-based intelligent input collection and delivers clear, confidence-weighted predictions.

## Features
- Gender-aware input prompts (asks for pregnancy history only if female)  
- Validates all medical inputs with proper SI units and acceptable ranges  
- Real-time diabetes risk prediction with confidence scores  
- Robust error handling and data validation for reliable user experience  
- User-friendly textual interface with clear instructions and formatted results  

## Technologies Used
- Python 3.8+  
- scikit-learn: For machine learning model training and inference  
- pandas: Data handling and preprocessing  
- numpy: Numerical computations and data processing  
- Random Forest Classifier: Supervised learning algorithm used for prediction  

## Installation & Setup

### Prerequisites
- Python 3.8 or higher  
- pip (Python package manager)

### Step-by-Step Installation
git clone https://github.com/yourusername/diabetes-prediction-system.git
cd diabetes-prediction-system
python -m venv venv # Create virtual environment (optional but recommended)
source venv/bin/activate # Activate environment (Linux/macOS)
venv\Scripts\activate # Activate environment (Windows)
pip install -r requirements.txt # Install dependencies


### Running the Application
python diabetes_predictor.py

Follow the interactive prompts to enter your health parameters.

## Project Structure
diabetes-prediction-system/
├── diabetes_predictor.py # Main application file
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── statement.md # Problem statement and scope
├── docs/ # Additional documentation (architecture, design rationale)
└── tests/ # Test modules for validation
└── test_predictor.py


## Testing Instructions
- Run unit tests (if available) via:
pytest
- Manually test by running the program and entering sample inputs.

## Sample Input
Gender (M/F): M
Glucose level (mg/dL) [Normal: 70-100]: 95
Blood Pressure (mmHg) [Normal: 90-120]: 110
Skin Thickness (mm) [Normal: 20-40]: 25
Insulin level (pmol/L) [Normal: 50-200]: 120
Body Mass Index (kg/m²) [Normal: 18.5-25]: 23.5
Diabetes Pedigree Function [Typical: 0.1-2.0]: 0.4
Age (years): 35


## Expected Output
RESULT: LOW RISK OF DIABETES
Confidence: 85.2%
Recommendation: Maintain healthy lifestyle


## Contributing
Contributions, issues, and feature requests are welcome! Please fork the repo and open a pull request.
