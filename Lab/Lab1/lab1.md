# Lab 1: Cyber Threat Intelligence Report Mapping

**Group Members:** Amit Mitzmacher, Tal Mitzmacher  
**Course:** Cyber Threat Intelligence  
**Date:** February 26, 2026  

## 1. Source CTI Report
**Report Title:** Muddled Libra: Evolution to Cloud and SaaS Attacks   
**Organization:** Palo Alto Networks (Unit 42)   
**Link:** https://unit42.paloaltonetworks.com/muddled-libra-evolution-to-cloud/ 

## 2. Description & Attack Schema
**Description:** This report analyzes "Muddled Libra" (Scattered Spider), focusing on their shift to Cloud and SaaS attacks using social engineering and session token theft.  
**Attack Schema:** Includes Reconnaissance via social media, Vishing for initial access, and the use of Rclone for exfiltration.  

## 3. MITRE ATT&CK Mapping
| Tactic | Technique ID | Technique Name | Behavior |
| :--- | :--- | :--- | :--- |
| Initial Access | T1566.004 | Vishing | [cite_start]Calling help desk pretending to be employees[cite: 21]. |
| Credential Access | T1539 | Steal Web Session Cookie | [cite_start]Theft of session tokens to bypass MFA[cite: 21]. |
| Persistence | T1098.005 | Device Registration | [cite_start]Registering unauthorized MFA devices[cite: 21]. |
| Exfiltration | T1567.002 | Exfiltration to Cloud | [cite_start]Using Rclone to transfer stolen data[cite: 21]. |
