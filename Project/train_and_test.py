import pandas as pd
import logging
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc

# =====================================================================
# CONFIGURING AUDIT LOGS
# =====================================================================
logging.basicConfig(
    filename='traffic_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# =====================================================================
# STEP 1 & 2: DATA LOADING & SPLITTING
# =====================================================================
print("=== Step 1 & 2: Loading & Splitting Dataset ===")
df = pd.read_csv("phishing_email.csv")
X = df['text_combined']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# =====================================================================
# STEP 3 & 4: VECTORIZATION & TRAINING
# =====================================================================
print("\n=== Step 3 & 4: Training Random Forest Model ===")
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1) 
model.fit(X_train_tfidf, y_train)

# =====================================================================
# STEP 5: EVALUATION & INDIVIDUAL CHART GENERATION
# =====================================================================
print("\n=== Step 5: Generating Evaluation Metrics & Charts ===")
y_pred = model.predict(X_test_tfidf)
y_probs = model.predict_proba(X_test_tfidf)[:, 1]
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
fpr, tpr, _ = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)
feat_importances = pd.Series(model.feature_importances_, index=vectorizer.get_feature_names_out()).nlargest(10)

# Chart 1: Dataset Class Distribution
plt.figure(figsize=(8, 6))
df_plot = df.copy()
df_plot['Class'] = df_plot['label'].map({0: 'Safe', 1: 'Phishing'})
sns.countplot(data=df_plot, x='Class', hue='Class', palette=['#2ecc71', '#e74c3c'], legend=False)
plt.title("1. Dataset Class Distribution")
plt.show()

# Chart 2: Confusion Matrix Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("2. Model Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()

# Chart 3: Top 10 Influential Words
plt.figure(figsize=(8, 6))
feat_importances.plot(kind='barh', color='#3498db')
plt.title("3. Top 10 Influential Words (Feature Importance)")
plt.gca().invert_yaxis()
plt.show()

# Chart 4: ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='#9b59b6', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.title('4. Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc="lower right")
plt.show()

# =====================================================================
# STEP 6: AUTOMATED TRAFFIC INSPECTION
# =====================================================================
print("\n=== Step 6: Running Project Test Cases ===")
inspection_stats = {'Safe': 0, 'Phishing': 0}

def inspect_traffic(email_text, case_name):
    email_tfidf = vectorizer.transform([email_text])
    prediction = model.predict(email_tfidf)[0]
    confidence = model.predict_proba(email_tfidf)[0][prediction] * 100
    
    if prediction == 1:
        print(f"[{case_name} ALERT]: Phishing Detected! (Confidence: {confidence:.2f}%)")
        inspection_stats['Phishing'] += 1
    else:
        print(f"[{case_name} SAFE]: Traffic Processed. (Confidence: {confidence:.2f}%)")
        inspection_stats['Safe'] += 1

# Running test cases
inspect_traffic("Meeting reminders: Please review the Q3 corporate reports.", "Case A")
inspect_traffic("Urgent: Click the link to verify your password.", "Case B")
inspect_traffic("Hey, are we still on for lunch?", "Sim C")
inspect_traffic("URGENT: Your account has been compromised.", "Sim D")
inspect_traffic("Your package has been shipped.", "Sim E")

# Chart 5: Live Traffic Distribution (Pie Chart)
plt.figure(figsize=(6, 5))
plt.pie([inspection_stats['Safe'], inspection_stats['Phishing']], 
        labels=['Safe Traffic', 'Phishing Alerts'], 
        autopct='%1.1f%%', startangle=140, colors=['#2ecc71', '#e74c3c'], explode=(0.1, 0))
plt.title("5. Live Inspection Traffic Distribution")
plt.show()

print("\n--- End of Execution ---")