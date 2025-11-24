# Diabetes Risk Assessment Program

## Problem Statement
Diabetes is a chronic disease affecting millions worldwide, often leading to serious health complications if not detected early. This program assists in preliminary assessment of diabetes risk by using common health indicators and symptom data provided by the user. It helps in raising awareness and advising early medical consultation.

## Scope of the Project
This console-based Python application collects key diabetes-related health parameters from users, such as glucose level, blood pressure, BMI, insulin levels, and family history. Using a Random Forest machine learning model trained on a small synthetic dataset, it predicts whether the user is likely at high or low risk of diabetes. The project emphasizes user-friendly input validation and clear result presentation.

## Target Users
- Individuals wanting a quick health check for diabetes risk.
- Students and learners exploring practical machine learning applications.
- Healthcare educators demonstrating ML models for medical diagnosis.
- Developers seeking a base for more comprehensive health diagnostics tools.

## High-Level Features
- Collects validated user inputs for gender, pregnancies (if female), glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, and age.
- Trains a Random Forest Classifier on example training data internally.
- Predicts diabetes risk and shows associated confidence percentages.
- Provides simple lifestyle and consultation recommendations based on results.
- Includes robust input validation to ensure meaningful data entry.
- Handles exceptions gracefully, including keyboard interrupt and invalid inputs.
