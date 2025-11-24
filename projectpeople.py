import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
def get_integer_input(prompt, min_val=0, max_val=200):
    """Get integer input with validation"""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a value between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid number")
def get_float_input(prompt, min_val=0.0, max_val=100.0):
    """Get float input with validation"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a value between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid number")
def get_gender_input():
    """Get gender input with validation"""
    while True:
        gender = input("Gender (M/F): ").upper()
        if gender in ['M', 'F']:
            return gender
        else:
            print("Please enter 'M' for Male or 'F' for Female")
# Create and train model immediately
# Define feature names
feature_names = ['Gender', 'Pregnancies', 'Glucose', 'BloodPressure', 
                 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigree', 'Age']
# Create sample training data with gender
data = {
    'Gender': [0, 0, 1, 1, 0, 1, 0, 1, 0, 1],  # 0=Female, 1=Male
    'Pregnancies': [2, 8, 0, 0, 7, 0, 3, 0, 2, 0],  # 0 for males
    'Glucose': [120, 180, 85, 140, 130, 90, 125, 170, 110, 150],
    'BloodPressure': [70, 80, 60, 75, 72, 65, 68, 82, 74, 78],
    'SkinThickness': [25, 35, 20, 30, 28, 22, 26, 38, 27, 32],
    'Insulin': [80, 0, 0, 100, 120, 85, 90, 0, 95, 110],
    'BMI': [25.5, 35.0, 22.0, 30.0, 28.5, 23.0, 26.0, 33.0, 27.0, 31.0],
    'DiabetesPedigree': [0.5, 1.2, 0.3, 0.8, 0.6, 0.4, 0.7, 1.1, 0.5, 0.9],
    'Age': [35, 50, 25, 45, 38, 28, 32, 55, 40, 48],
    'Outcome': [0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
}
df = pd.DataFrame(data)
X = df[feature_names]  # Use feature names explicitly
y = df['Outcome']
# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
# Get user input
print("===========================================")
print("        DIABETES RISK ASSESSMENT")
print("===========================================")
try:
    # Get gender
    gender = get_gender_input()
    # Get pregnancies only for females
    if gender == 'F':
        pregnancies = get_integer_input("Number of pregnancies: ", 0, 20)
    else:
        pregnancies = 0
    # Get other health parameters with SI units
    glucose = get_integer_input("Glucose level (mg/dL) [Normal: 70-100]: ", 50, 300)
    blood_pressure = get_integer_input("Blood Pressure (mmHg) [Normal: 90-120]: ", 40, 200)
    skin_thickness = get_integer_input("Skin Thickness (mm) [Normal: 20-40]: ", 10, 60)
    insulin = get_integer_input("Insulin level (pmol/L) [Normal: 50-200]: ", 0, 500)
    bmi = get_float_input("Body Mass Index (kg/m²) [Normal: 18.5-25]: ", 15.0, 50.0)
    diabetes_pedigree = get_float_input("Diabetes Pedigree Function [Typical: 0.1-2.0]: ", 0.08, 2.5)
    age = get_integer_input("Age (years): ", 18, 100)
    # Convert gender to number (0=Female, 1=Male)
    gender_num = 1 if gender == 'M' else 0
    # Create DataFrame with correct feature names to avoid warning
    user_data = pd.DataFrame([[
        gender_num, pregnancies, glucose, blood_pressure, skin_thickness, 
        insulin, bmi, diabetes_pedigree, age
    ]], columns=feature_names)
    # Make prediction
    prediction = model.predict(user_data)[0]
    probability = model.predict_proba(user_data)[0]
    # Show result
    print("\n" + "=" * 50)
    print("            PREDICTION RESULT")
    print("=" * 50)
    if prediction == 1:
        print("RESULT: HIGH RISK OF DIABETES")
        print(f"Confidence: {probability[1]:.1%}")
        print("\nRecommendation: Please consult a healthcare provider")
    else:
        print("RESULT: LOW RISK OF DIABETES")
        print(f"Confidence: {probability[0]:.1%}")
        print("\nRecommendation: Maintain healthy lifestyle")
    print()
    print("Always consult healthcare professionals for medical advice.")
except KeyboardInterrupt:
    print("\n\nProgram interrupted by user")
except Exception as e:
    print(f"\nAn error occurred: {e}")
