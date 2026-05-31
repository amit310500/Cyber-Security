# AI Cyber Shield: Phishing Email Detection System MVP

An intelligent Machine Learning Minimum Viable Product (MVP) designed to detect sophisticated phishing attacks by leveraging token-level statistical classification, continuous traffic simulation, and automated threat context enrichment mapped directly to the **MITRE ATT&CK Framework**.

---

## 👥 Authors
* **Amit Mitzmacher** - *Holon Institute of Technology (HIT)*
* **Tal Mitzmacher** - *Holon Institute of Technology (HIT)*
* **Course:** Artificial Intelligence in Cybersecurity

---

## 📌 1. Introduction and Objectives
In this project, we developed an MVP system to detect phishing attacks using Machine Learning. Traditional tools rely on signature-based filters (like known bad URLs), which easily fail against "semantic camouflage"—malicious intent hidden inside polite, professional corporate language.

Our main objective was to train a Random Forest model combined with TF-IDF vectorization to analyze text traffic in real-time. Additionally, the system automatically maps flagged threats to the MITRE ATT&CK framework to provide security teams with immediate context.

---

## 📊 2. Dataset and Data Distribution
We utilized a dataset containing 82,486 email samples. The raw distribution consists of:
* **Safe Corporate Emails (Class 0):** 39,634 samples (~48.0%)
* **Phishing Threats (Class 1):** 42,852 samples (~52.0%)

We split the data using an 80/20 ratio:
* **Training Set:** 65,988 samples
* **Testing Set:** 16,498 samples (held out entirely for final verification)

<p align="center">
  <img src="image_b1eb63.png" alt="Dataset Distribution" width="60%">
</p>

---

## ⚡ 3. Performance Evaluation
The model was trained using parallel computing (`n_jobs=-1`). Evaluating the model against the 16,498 independent test samples yielded an overall macro accuracy of 99%.

### A. Classification Metrics
```text
Class 0 (Safe Traffic):     Precision: 0.99 | Recall: 0.99 | F1-Score: 0.99 | Support: 7,935
Class 1 (Phishing Threats): Precision: 0.99 | Recall: 0.99 | F1-Score: 0.99 | Support: 8,563
