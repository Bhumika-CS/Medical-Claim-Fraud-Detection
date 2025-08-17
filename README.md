Medical Claims Fraud Detection - README

This project focuses on detecting fraudulent medical insurance claims using a rule-based anomaly detection system built in Python.  
The approach segments claims into different risk categories and provides visual insights on high-risk providers and suspicious claim patterns.  

---

## 📂 Project Structure  

medical-claims-fraud-detection/
│── MI fraud detection.py               # Python script with fraud detection logic
│── medical_claims_dummy_dataset_2000.xlsx # Simulated dataset (2000 rows)
│── Project Report - Medical Claims Fraud Detection.docx # Detailed report
│── README.md                           # Project documentation

---

## 🎯 Objectives  

- Identify potentially fraudulent (high-risk) claims using rule-based logic.  
- Categorize claims into High, Medium, and Normal risk.  
- Rank providers based on the number of high-risk claims.  
- Analyze monthly trends in suspicious claims.  
- Provide actionable insights for insurers and audit teams.  

---

## 📊 Dataset Summary  

The dataset contains 2000 simulated medical insurance claims with the following fields:  

- Patient ID – Unique identifier per patient  
- Claim Amount – Total billed amount (INR)  
- Claim Date – Date of claim submission  
- Provider ID – Unique ID of healthcare provider  
- Procedure Code – Medical procedure code billed  
- Procedure Count – Number of procedures per claim  
- Diagnosis Code – ICD diagnosis code  
- Length of Stay – Inpatient days (0 = outpatient)  
- Payment Mode – Cash / Card / Insurance  

---

## ⚙️ Methodology  

1. Data Generation  
   - Synthetic dataset of 2000 claims created using Python & NumPy.  

2. Rule-Based Risk Classification  
   - High Risk: Claim Amount > ₹100,000 AND Procedure Count > 6  
   - Medium Risk: Claim Amount > ₹50,000 OR Procedure Count > 4  
   - Normal Risk: Remaining claims  

3. Provider Risk Summary  
   - Counted number of high-risk claims per provider.  
   - Ranked top 10 providers with most suspicious claims.  

4. Temporal Analysis  
   - Grouped claims by month to observe suspicious claim spikes.  

---

## 🚀 How to Run  

1. Install required Python libraries:  
   pip install pandas matplotlib seaborn openpyxl

2. Run the Python script:  
   python "MI fraud detection.py"

3. Outputs:  
   - A dataset with new column Suspicion Score.  
   - Visuals:  
     - Top 10 providers with most high-risk claims  
     - Monthly trend of high-risk claims  

---

## 🛠️ Tools Used  

- Python (Pandas, NumPy) → Data handling & rule logic  
- Matplotlib / Seaborn → Visualizations  
- Excel → Input dataset (medical_claims_dummy_dataset_2000.xlsx)  

---

## 📈 Sample Insights  

- Providers P018, P012, and P008 flagged with unusually high risky claims.  
- Spikes in June and December suggest possible year-end fraud.  
- Rule-based system is simple and transparent but may miss complex fraud patterns.  

---

## 📌 Future Enhancements  

- Apply machine learning models (Isolation Forest, Random Forest).  
- NLP on claim descriptions for deeper audits.  
- Add geolocation & patient demographics for risk profiling.  
- Power BI dashboard integration for real-time fraud monitoring.  

---

## 👩‍💻 Author  

**Bhumika C S**  
