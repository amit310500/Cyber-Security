# [cite_start]Lab Work 1: Cyber Threat Intelligence Report Mapping [cite: 1]

**Group Members:** Amit Mitzmacher, Tal Mitzmacher  
**Course:** Cyber Threat Intelligence  
[cite_start]**Date:** February 26, 2026 [cite: 2, 3, 4]

---

## [cite_start]1. Source CTI Report [cite: 5]
* [cite_start]**Report Title:** Muddled Libra: Evolution to Cloud and SaaS Attacks [cite: 6]
* [cite_start]**Organization:** Palo Alto Networks (Unit 42) [cite: 7]
* [cite_start]**Link:** [https://unit42.paloaltonetworks.com/muddled-libra-evolution-to-cloud/](https://unit42.paloaltonetworks.com/muddled-libra-evolution-to-cloud/) [cite: 8]

## [cite_start]2. Short Description & Attack Schema [cite: 9]
### Description
[cite_start]This report analyzes the activities of the threat group "Muddled Libra" (also known as Scattered Spider)[cite: 10]. [cite_start]The group is known for its sophisticated social engineering and its shift from attacking on-premise infrastructure to targeting Cloud and SaaS environments[cite: 11]. [cite_start]Their primary strategy is "logging in rather than breaking in," utilizing stolen session tokens and bypassing Multi-Factor Authentication (MFA) to gain high-level administrative access[cite: 12].

### [cite_start]Attack Schema [cite: 13]
* [cite_start]**Reconnaissance:** Identifying IT help desk employees via social media and LinkedIn[cite: 14].
* [cite_start]**Initial Access:** Using Voice Phishing (Vishing) to trick help desk staff into resetting passwords or enrolling new MFA devices[cite: 15].
* [cite_start]**Credential Access:** Stealing web session cookies to bypass MFA prompts[cite: 16].
* [cite_start]**Persistence:** Registering unauthorized devices in the corporate identity provider (Okta/Azure AD)[cite: 17].
* [cite_start]**Lateral Movement:** Moving from the compromised identity provider into SaaS apps (Slack, AWS, GCP)[cite: 18].
* [cite_start]**Exfiltration:** Using automated tools like Rclone to move data to attacker-controlled cloud storage[cite: 19].

## [cite_start]3. MITRE ATT&CK Mapping (Behaviors / Tactics / Techniques) [cite: 20]

| Tactic | Technique ID | Technique Name | Behavior Observed in Report |
| :--- | :--- | :--- | :--- |
| Initial Access | T1566.004 | Phishing: Voice (Vishing) | [cite_start]Attackers called the help desk pretending to be employees to gain access. [cite: 21] |
| Credential Access | T1539 | Steal Web Session Cookie | [cite_start]Theft of browser session tokens to bypass the need for a password or MFA. [cite: 21] |
| Persistence | T1098.005 | Account Manipulation: Device Registration | [cite_start]The group registered their own mobile devices as trusted MFA factors for compromised accounts. [cite: 21] |
| Discovery | T1087.004 | Account Discovery: Cloud Account | [cite_start]Scanning the environment to find high-privilege cloud administrators. [cite: 21] |
| Defense Evasion | T1550.001 | Use Alternate Authentication Material | [cite_start]Using stolen OAuth tokens to maintain access without triggering alerts. [cite: 21] |
| Lateral Movement | T1021.001 | Remote Services: RDP | [cite_start]Utilizing RDP to move between virtual machines within the internal network. [cite: 21] |
| Collection | T1530 | Data from Cloud Storage | [cite_start]Accessing and collecting sensitive data from SharePoint and AWS S3 buckets. [cite: 21] |
| Exfiltration | T1567.002 | Exfiltration Over Web Service | [cite_start]Using the Rclone utility to transfer stolen data to the attacker's cloud infrastructure. [cite: 21] |

## [cite_start]4. Advanced Search Queries [cite: 22]
* [cite_start]`site: unit42.paloaltonetworks.com "Muddled Libra" "MITRE ATT&CK"` [cite: 24]
* [cite_start]`tasklist /v site: attack.mitre.org/techniques/T1539` [cite: 25]
* [cite_start]`"MFA Fatigue" site: cloud.google.com/blog/topics/threat-intelligence` [cite: 26]
