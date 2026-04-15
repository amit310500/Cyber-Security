# Lab Work 1: Cyber Threat Intelligence Report Mapping 

**Group Members:** Amit Mitzmacher, Tal Mitzmacher  
**Course:** Cyber Threat Intelligence  
**Date:** February 26, 2026 

---

## 1. Source CTI Report
* **Report Title:** Muddled Libra: Evolution to Cloud and SaaS Attacks.
* **Organization:** Palo Alto Networks (Unit 42) 
* **Link:** https://unit42.paloaltonetworks.com/muddled-libra-evolution-to-cloud/

## 2. Short Description & Attack Schema
### Description
This report analyzes the activities of the threat group "Muddled Libra" (also known as Scattered Spider). The group is known for its sophisticated social engineering and its shift from attacking on-premise infrastructure to targeting Cloud and SaaS environments.    Their primary strategy is "logging in rather than breaking in," utilizing stolen session tokens and bypassing Multi-Factor Authentication (MFA) to gain high-level administrative access.

### Attack Schema
**Reconnaissance:** Identifying IT help desk employees via social media and LinkedIn.
**Initial Access:** Using Voice Phishing (Vishing) to trick help desk staff into resetting passwords or enrolling new MFA devices.
**Credential Access:** Stealing web session cookies to bypass MFA prompts.
**Persistence:** Registering unauthorized devices in the corporate identity provider (Okta/Azure AD).
**Lateral Movement:** Moving from the compromised identity provider into SaaS apps (Slack, AWS, GCP).
**Exfiltration:** Using automated tools like Rclone to move data to attacker-controlled cloud storage.

## 3. MITRE ATT&CK Mapping (Behaviors / Tactics / Techniques)

| Tactic | Technique ID | Technique Name | Behavior Observed in Report |
| :--- | :--- | :--- | :--- |
| Initial Access | T1566.004 | Phishing: Voice (Vishing) | Attackers called the help desk pretending to be employees to gain access. |
| Credential Access | T1539 | Steal Web Session Cookie | Theft of browser session tokens to bypass the need for a password or MFA. |
| Persistence | T1098.005 | Account Manipulation: Device Registration | The group registered their own mobile devices as trusted MFA factors for compromised accounts. |
| Discovery | T1087.004 | Account Discovery: Cloud Account | Scanning the environment to find high-privilege cloud administrators. |
| Defense Evasion | T1550.001 | Use Alternate Authentication Material | Using stolen OAuth tokens to maintain access without triggering alerts. |
| Lateral Movement | T1021.001 | Remote Services: RDP | Utilizing RDP to move between virtual machines within the internal network. |
| Collection | T1530 | Data from Cloud Storage | Accessing and collecting sensitive data from SharePoint and AWS S3 buckets. |
| Exfiltration | T1567.002 | Exfiltration Over Web Service | Using the Rclone utility to transfer stolen data to the attacker's cloud infrastructure. |

## 4. Advanced Search Queries 
site: unit42.paloaltonetworks.com "Muddled Libra" "MITRE ATT&CK"` 
tasklist /v site: attack.mitre.org/techniques/T1539` 
"MFA Fatigue" site: cloud.google.com/blog/topics/threat-intelligence`
