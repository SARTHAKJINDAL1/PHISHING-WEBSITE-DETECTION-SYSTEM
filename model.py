# edit : Improved input handling and clarity
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

def run_system():
    print("========================================")
    print("   PHISHING WEBSITE DETECTION SYSTEM")
    print("   Course: Fundamentals of AI and ML")
    print("   Name: Sarthak Jindal")
    print("   Reg No: 25BCE10189")
    print("========================================")
    print("\nWelcome! This AI model classifies URLs.")
    csv_file = 'Phising_Training_Dataset.csv'
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} missing.")
        return
    
    print("\nLoading dataset...")
    df = pd.read_csv(csv_file)
    print("Training the AI model... please wait.")
    X = df.drop(['key', 'Result'], axis=1)
    y = df['Result']

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    clf = DecisionTreeClassifier(criterion='entropy', max_depth=15)
    clf.fit(x_train, y_train)
    joblib.dump(clf, 'phishing_model.pkl')

    preds = clf.predict(x_test)
    acc = accuracy_score(y_test, preds)

    print(f" SUCCESS: Model Training Complete!")
    print(f" Final Accuracy Score: {acc * 100:.2f}%")


    while True:
        print("\n========================================")
        print("       INTERACTIVE LIVE DETECTOR")
        print("========================================")
        print("Enter values: 1 (Legitimate), 0 (Suspicious), -1 (Phishing)")
        
        try:
            # Asking for the top 6 most important features
            s_state    = int(input("1. SSL Final State: "))
            anchor     = int(input("2. URL Anchor Score: "))
            traffic    = int(input("3. Web Traffic Score: "))
            sub_domain = int(input("4. Having Sub-Domain: "))
            tags       = int(input("5. Links in Tags: "))
            prefix     = int(input("6. Prefix-Suffix (Hyphen in Domain): "))
            
            # Creating a full 30-feature row for the model
            test_input = [0] * 30
            
            # Mapping inputs to their correct column positions in the dataset
            test_input[7]  = s_state    
            test_input[13] = anchor     
            test_input[25] = traffic    
            test_input[6]  = sub_domain 
            test_input[14] = tags       
            test_input[5]  = prefix     
            
            final_df = pd.DataFrame([test_input], columns=X.columns)
            res = clf.predict(final_df)[0]
            
            print("\n********************")
            if res == 1:
                print("RESULT: Website is SAFE.")
            elif res == 0:
                print("RESULT: Website is SUSPICIOUS.")
            else:
                print("ALERT: This is a PHISHING site!")
            print("********************")
                
        except ValueError:
            print("Invalid input. Use -1, 0, or 1.")

        choice = input("\nCheck another site? (y/n): ").lower()
        if choice != 'y':
            print("System shutting down. Stay safe online!")
            break

if __name__ == "__main__":
    run_system()
