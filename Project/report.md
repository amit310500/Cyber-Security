# AI-Powered Phishing Email Detection System (AI Cyber Shield)

**Course:** Artificial Intelligence in Cybersecurity  
**Institution:** Holon Institute of Technology (HIT)  
**Submitted by:** Amit Mitzmacher & Tal Mitzmacher  

---

## 📌 Project Overview
This repository contains an **MVP (Minimum Viable Product) Phishing Detection System** developed to counter sophisticated social engineering attacks. Traditional security controls rely heavily on static signature-based filters (e.g., known malicious URLs or specific blacklisted domains), which frequently fail against **"semantic camouflage"**—where malicious intent is cloaked in polite, professional, and corporate language.

To solve this, our system employs a machine learning pipeline pairing **TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization** with a **Random Forest Classifier** to analyze email payloads in real-time. Crucially, the system acts as an intelligent layer for a Security Operations Center (SOC) by automatically mapping flagged anomalies directly to the **MITRE ATT&CK® Framework**.

### Key Features
* **Real-time Payload Classification:** High-throughput prediction engineered using multi-core parallel computing.
* **Semantic Camouflage Detection:** Detects malicious intent even when stripped of obvious malicious triggers or bad indicators.
* **MITRE ATT&CK Mapping:** Instantly translates alerts into actionable adversarial tactics and techniques for triage.
* **Production-Ready Logging:** Outputs structured events to `traffic_logs.log` for direct SIEM/SOC ingestion.

---

## 📊 Dataset & Architecture

The model was built and verified using a vast dataset comprising **82,486 email samples**, featuring a balanced distribution of benign corporate correspondence and active threats.

* **Safe Corporate Emails (Class 0):** 39,634 samples (~48.0%)
* **Phishing Threats (Class 1):** 42,852 samples (~52.0%)

### Data Split Strategy
To guarantee strict independent evaluation, the dataset was split into an **80/20 ratio**:
* **Training Set:** 65,988 samples
* **Testing Set:** 16,498 samples *(held out entirely for final verification)*[cite: 1]

---

## 📈 Performance & Evaluation Metrics

The system achieved a **99% Macro Accuracy** and an **Area Under the Curve (AUC) of 1.00** during evaluation against the unseen test partition[cite: 1]. 

### Classification Report[cite: 1]

| Class | Traffic Type | Precision | Recall | F1-Score | Support |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **0** | Safe Corporate Traffic | 0.99 | 0.99 | 0.99 | 7,935 |
| **1** | Phishing Threat | 0.99 | 0.99 | 0.99 | 8,563 |

### Confusion Matrix Insights
