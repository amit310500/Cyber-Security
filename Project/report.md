# Project Report: AI Cyber Shield MVP System

**Course:** Artificial Intelligence in Cybersecurity  
**Submitted by:** Amit Mitzmacher, Tal Mitzmacher  
**Institution:** Holon Institute of Technology (HIT)  

---

## 1. Introduction and Objectives
In this project, we built an MVP (Minimum Viable Product) system designed to detect phishing attacks using Machine Learning. Traditional security mechanisms usually rely on signature-based detection, meaning they look for specific blacklisted links or known malicious senders. However, modern cybercriminals frequently use "semantic camouflage" to bypass these filters, wrapping their malicious intent inside polite, professional corporate emails.

Our main objective was to train a Random Forest model combined with TF-IDF vectorization to scan incoming text traffic in real-time. Beyond basic binary classification (Safe/Phishing), our goal was to automatically map detected anomalies to the MITRE ATT&CK framework. This helps security analysts in a Security Operations Center (SOC) quickly understand the exact nature and strategy of the incoming threat.

---

## 2. Dataset and Data Distribution
We worked with a comprehensive dataset containing a total of 82,486 email samples. Before starting the training process, we analyzed the class distribution to ensure the dataset was balanced. This is a crucial step in machine learning pipelines because an imbalanced dataset can cause the model to develop a strong bias toward the majority class.

The dataset is divided almost perfectly, with roughly 50% safe corporate emails and 50% phishing messages. We split the data using a standard 80/20 ratio:
* **Training Set:** 65,988 samples (used for training the model)
* **Testing Set:** 16,498 samples (held out entirely and used only for final evaluation)

---

## 3. Performance Evaluation
We trained the Random Forest classifier using all available CPU cores (`n_jobs=-1`) to optimize computational efficiency. After running the model against our 16,498 independent test samples, we generated the following evaluation metrics.

### A. Classification Report Metrics
The model achieved an overall accuracy rate of 99%. Below is the breakdown of the precision, recall, and F1-score for each class:

* **Class 0 (Safe Traffic):**
  * Precision: 0.99
  * Recall: 0.99
  * F1-Score: 0.99
  * Support: 7,935

* **Class 1 (Phishing Threats):**
  * Precision: 0.99
  * Recall: 0.99
  * F1-Score: 0.99
  * Support: 8,563

* **Overall Macro Accuracy:** 0.99 (Total Support: 16,498)

### B. Confusion Matrix Analysis
To understand the exact operational errors behind the 99% accuracy rate, we evaluated the raw confusion matrix results:
* **True Negatives (TN):** 7,827 safe emails were correctly classified as legitimate.
* **True Positives (TP):** 8,452 phishing attacks were successfully intercepted and blocked.
* **False Positives (FP):** 108 benign messages were wrongly flagged as phishing (False Alarms).
* **False Negatives (FN):** 111 malicious emails managed to slip through the text filter (Missed Threats).

### C. ROC Curve and AUC Value
We also plotted the Receiver Operating Characteristic (ROC) curve to evaluate how well our model separates the two classes at different decision thresholds. Our model reached an Area Under the Curve (AUC) of 1.00 (rounded). This strong result proves that the features extracted by the TF-IDF vectorizer allow the Random Forest classifier to establish sharp decision boundaries between legitimate corporate communications and social engineering attempts.

---

## 4. Feature Importance Insights
One of the key reasons we chose a Random Forest architecture is its transparency. It allows us to inspect the `feature_importances_` attribute to see exactly which words had the most influence on its classification choices. We extracted and reviewed the top 10 most important features.

We observed that terms like "2008", "wrote", and "aug" carry significant statistical weight. This happens because our training dataset contains historical email archives that include these metadata fragments. However, looking past this dataset noise, the model strongly relies on words that indicate urgency, financial operations, and immediate credential verification—such as "urgent", "invoice", and "password". For future iterations, we plan to implement a cleaner text preprocessing step to strip out dates and metadata tokens so the model can focus purely on security-relevant vocabulary.

---

## 5. Live Simulation and MITRE ATT&CK Mapping
To see how our MVP performs in an operational context, we set up a testing macro that injected 100 random email samples through the pipeline. In this live run, the system classified 63.0% of the simulation traffic as safe and flagged 37.0% as phishing anomalies.

We paid close attention to how the system handled our two core project test cases:

* **Test Case A (Routine Workspace Email):**
  * *Text Content:* "Meeting reminders: Please review the Q3 corporate reports before tomorrow's sync..."
  * *System Output:* Classified as **SAFE** with a high confidence level of **95.00%**. This confirms that the model will not cause operational friction or block routine business tasks.
* **Test Case B (Deceptive Phishing Simulation):**
  * *Text Content:* "Dear employee... please find attached the urgent project expense invoice... click the link to verify your password immediately..."
  * *System Output:* Intercepted and raised a **PHISHING ALERT** with a confidence score of **55.00%**.

### Operational Analysis of Test Case B:
A traditional, signature-based keyword filter would easily miss Test Case B because the text uses polite, professional language ("Dear employee", "project expense"). Our model caught the threat, but its confidence dropped to 55.00%. Architecturally, this lower score makes complete sense: it reflects the actual semantic battle happening within the text between the legitimate-looking phrasing (the camouflage) and the high-risk request to verify a password immediately. This specific case shows why static rules fall short and why a machine learning layer is necessary to catch sophisticated social engineering.

When a phishing threat is identified, the system automatically assigns the corresponding MITRE ATT&CK taxonomy:
* **Tactic Mapping:** Initial Access (TA0001) / Credential Access (TA0006)
* **Technique Mapping:** Phishing: Spearphishing Link (T1566.002)

Our live monitoring dashboard also compiled real-time telemetry from the simulation. The dashboards visualize the confidence distribution (showing that legitimate traffic is highly clustered around high-certainty bounds) and track the frequency of detected tactics, where "Phishing for Information" (T1598.003) was the most prominent threat type. Finally, every single classification was saved to the `traffic_logs.log` file, showing that the system is ready for standard SIEM log ingestion.

---

## 6. Conclusion
Our AI Cyber Shield MVP successfully achieved a 99% classification accuracy rate and an AUC of 1.00. By combining statistical text processing with a live audit trail and the MITRE ATT&CK framework, we built an MVP that goes beyond basic binary blocking to give security analysts actionable threat intelligence. For our next steps, we want to expand our testing dataset to evaluate how well this model holds up against more advanced phishing emails generated by large language models (LLMs).
