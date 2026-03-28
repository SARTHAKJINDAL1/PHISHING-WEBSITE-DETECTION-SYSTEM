# Phishing Website Detection System

## Overview

This project is a Machine Learning-based system designed to detect phishing websites using URL-related features. Phishing attacks are a major cybersecurity threat where malicious websites attempt to steal sensitive information such as passwords, credit card details, and personal data.

The system uses a Decision Tree Classifier trained on a phishing dataset to classify websites into three categories:

* Legitimate (Safe)
* Suspicious
* Phishing (Malicious)

The project also includes an interactive command-line interface where users can manually input feature values and get real-time predictions.
This project solves a real-world cybersecurity problem using machine learning techniques.

---

## Problem Statement

Phishing attacks are increasing rapidly and pose a serious threat to individuals and organizations. Many users are unable to distinguish between legitimate and fake websites.

This project aims to solve this problem by building an intelligent system that can automatically detect phishing websites based on key indicators.

---

## Objectives

* To build a machine learning model for phishing detection
* To train and evaluate the model using a real-world dataset
* To provide an interactive system for real-time prediction
* To improve awareness of cybersecurity risks

---

## Dataset

The dataset used in this project is sourced from Kaggle:
Phishing Training Dataset

Features:

* Contains 30 attributes related to URL and website behavior
* Includes features such as:

  * SSL Final State
  * URL Anchor
  * Web Traffic
  * Subdomain Presence
  * Links in Tags
  * Prefix/Suffix usage

Target Variable:

* Result (1 = Legitimate, 0 = Suspicious, -1 = Phishing)

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib

---

## Model Details

* Algorithm: Decision Tree Classifier
* Criterion: Entropy
* Max Depth: 15
* Train-Test Split: 80:20

---

## Project Structure

```
phishing-detection/
│
├── model.py
├── Phising_Training_Dataset.csv
├── phishing_model.pkl
├── README.md
├── Project_Report.pdf
├── Screenshots
   ├── Code
   ├── Output
```

---

## Installation and Setup

1. Clone the repository:

```
git clone https://github.com/your-username/phishing-detection.git
```

2. Navigate to the project folder:

```
cd phishing-detection
```

3. Install dependencies:

```
pip install pandas numpy scikit-learn joblib
```

---

## How to Run

Run the Python file:

```
python model.py
```

---

## How It Works

1. The system loads the dataset
2. It trains a Decision Tree model
3. The model is saved as a .pkl file
4. User enters feature values
5. Model predicts whether the website is safe or phishing

---

## Sample Output

* Model Accuracy: ~95%
* Interactive system asks for inputs like SSL state, web traffic, etc.
* Outputs classification result instantly

---

## Key Features

* Real-time phishing detection
* Interactive command-line interface
* Lightweight and fast model
* Easy to use and understand

---

## Limitations

* Requires manual input of features
* Not directly integrated with real URLs
* Limited to dataset features

---

## Future Improvements

* Convert to web application using Flask
* Accept real URL input instead of manual values
* Use advanced models like Random Forest or XGBoost
* Improve UI/UX

---

## Learning Outcomes

* Understanding of supervised machine learning
* Model training and evaluation
* Working with real-world datasets
* Building interactive ML applications

---

## Details

* Name: Sarthak Jindal
* Registration Number: 25BCE10189
* Course Code: CSA2001
* Course Title: Fundamentals of AI and ML
* Faculty: Prof. J. Manikandan

---
