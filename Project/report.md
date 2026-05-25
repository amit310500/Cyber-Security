# Project Report: AI Cyber Shield MVP System
**Course:** Artificial Intelligence in Cybersecurity
**Submitted by:** Amit Mitzmacher, Tal Mitzmacher
**Institution:** Holon Institute of Technology (HIT)

### 1. Introduction and Objectives
This project focuses on building an MVP (Minimum Viable Product) system to detect phishing attacks using Machine Learning. Traditional security tools usually look for specific malicious links or known bad senders (signature-based detection). However, modern hackers use "semantic camouflage"—meaning they hide their bad intentions inside polite, professional corporate emails. 

Our main goal was to train a Random Forest model combined with TF-IDF vectorization to scan text traffic, catch these hidden phishing attempts in real-time, and automatically map them to the MITRE ATT&CK framework so security teams can understand the nature of the threat immediately.

### 2. Dataset and Data Distribution
For this project, we used a large dataset containing a total of 82,486 email samples. Before training, we analyzed the data distribution to make sure it was balanced, which is a critical step to prevent the model from being biased toward one specific class. 

The dataset is divided almost perfectly: about 50% are safe corporate emails and 50% are phishing emails. We split the data using an 80/20 ratio:
* **Training set:** 65,988 samples (used to train the model)
* **Testing set:** 16,498 samples (held out completely for the final evaluation)

### 3. Performance Evaluation
We trained the Random Forest model using all available CPU cores (`n_jobs=-1`) to speed up the process. After testing the trained model on our 16,498 test samples, we got the following results.

#### A. Classification Report Metrics
The model performed very well, reaching an overall accuracy of 99%. The detailed metrics for each class are presented below:

| Class | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **0 (Safe Traffic)** | 0.99 | 0.99 | 0.99 | 7,935 |
| **1 (Phishing)** | 0.99 | 0.99 | 0.99 | 8,563 |
| **Accuracy** | | | **0.99** | **16,498** |

#### B. Confusion Matrix Analysis
Looking at the confusion matrix, we can see exactly how many mistakes the model made out of the 16,498 test cases:
* **True Negatives (TN):** 7,827 safe emails were correctly identified as safe.
* **True Positives (TP):** 8,452 phishing emails were caught and blocked.
* **False Positives (FP):** 108 safe emails were wrongly flagged as phishing (false alarms).
* **False Negatives (FN):** 111 phishing emails slipped through the text filter.

#### C. ROC Curve and AUC Value
We also plotted the Receiver Operating Characteristic (ROC) curve to see how well our model separates the two classes at different thresholds. Our model achieved an Area Under the Curve (AUC) of 1.00 (rounded). This shows that the Random Forest classifier has a very strong ability to distinguish between legitimate corporate communication and phishing attempts.

### 4. Feature Importance Insights
One of the main benefits of using a Random Forest model is that it allows us to see which features (words) were the most important for its decisions. We extracted the top 10 most influential words from the model. 

We noticed that some words like "2008", "wrote", and "aug" have high statistical weight simply because of how the dataset was collected (historical email archives). However, looking past this dataset noise, the model heavily relies on words that indicate urgency, financial transactions, and credential verification (like "urgent", "invoice", and "password"). In our next project version, we plan to improve the text preprocessing step to strip out dates and metadata noise so the model can focus purely on cyber-related terms.

### 5. Live Simulation and MITRE ATT&CK Mapping
To see how the MVP behaves in a live environment, we ran a simulation testing pipeline with 100 random email samples. In this live run, the system classified **63% of the traffic as safe** and flagged **37% as phishing anomalies**.

We specifically tested the system with the two main project test cases to see if it handles semantic camouflage:

* **Test Case A (Routine Workflow):**
  * *Text:* "Meeting reminders: Please review the Q3 corporate reports before tomorrow's sync..."
  * *Result:* The model correctly classified this as **SAFE** with a high confidence score of **95.00%**, meaning it won't disrupt normal corporate communications.
* **Test Case B (Polite Attack Simulation):**
  * *Text:* "Dear employee... please find attached the urgent project expense invoice... click the link to verify your password immediately..."
  * *Result:* The system caught the attack and raised a **PHISHING ALERT** with a confidence score of **55.00%**.

#### Analysis of Test Case B:
A traditional, basic keyword filter would fail on Test Case B because it uses polite corporate language ("Dear employee", "project expense"). Our model managed to catch it, but the confidence score dropped to 55.00%. This lower score makes total sense architecturally: it reflects the "semantic battle" inside the text between the polite, normal phrasing and the malicious request to verify a password immediately. This proves why basic rules are not enough and why an AI layer is actually needed.

When an email is flagged as phishing, the system maps it to the MITRE ATT&CK framework:
* **Tactic:** Initial Access (TA0001) / Credential Access (TA0006)
* **Technique:** Phishing: Spearphishing Link (T1566.002)

We also generated real-time dashboards to track the system's live telemetry. The graphs show that safe emails usually cluster around very stable confidence scores, and they visualize the distribution of detected MITRE techniques, where "Phishing for Information" (T1598.003) was the most common threat. Finally, all classifications were logged into the `traffic_logs.log` file, showing that the system is ready to connect to a company's SOC system.

### 6. Conclusion
Our AI Cyber Shield MVP successfully achieves a 99% accuracy rate and a strong AUC of 1.00. By combining ML text classification with the MITRE ATT&CK framework and live logging, we built a tool that doesn't just block emails, but actually gives security analysts useful intelligence about the attacks. For future work, we want to test how the model handles more advanced, LLM-generated phishing emails.
