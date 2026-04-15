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
[cite_start]דוח זה מנתח את פעילות קבוצת האיום "Muddled Libra" (הידועה גם בשם Scattered Spider)[cite: 10]. [cite_start]הקבוצה מוכרת בזכות הנדסה חברתית מתוחכמת ומעבר מתקיפת תשתיות מקומיות (On-premise) למיקוד בסביבות ענן ו-SaaS[cite: 11]. [cite_start]האסטרטגיה העיקרית שלהם היא "להתחבר במקום לפרוץ", תוך שימוש באסימוני דלייה (Session tokens) גנובים ועקיפת אימות רב-שלבי (MFA) כדי להשיג גישת ניהול ברמה גבוהה[cite: 12].

### [cite_start]Attack Schema [cite: 13]
* [cite_start]**Reconnaissance:** זיהוי עובדי תמיכה טכנית (IT help desk) דרך רשתות חברתיות ו-LinkedIn[cite: 14].
* [cite_start]**Initial Access:** שימוש ב-Voice Phishing (Vishing) כדי להונות את צוות התמיכה לאפס סיסמאות או לרשום מכשירי MFA חדשים[cite: 15].
* [cite_start]**Credential Access:** גניבת עוגיות דפדפן (Session cookies) כדי לעקוף דרישות MFA[cite: 16].
* [cite_start]**Persistence:** רישום מכשירים לא מורשים בזהות הארגונית (Okta/Azure AD)[cite: 17].
* [cite_start]**Lateral Movement:** מעבר מזהות הארגון שנפרצה לתוך אפליקציות SaaS כמו Slack, AWS, ו-GCP[cite: 18].
* [cite_start]**Exfiltration:** שימוש בכלים אוטומטיים כמו Rclone להעברת נתונים לאחסון ענן בשליטת התוקף[cite: 19].

## [cite_start]3. MITRE ATT&CK Mapping [cite: 20]

| Tactic | Technique ID | Technique Name | Behavior Observed in Report |
| :--- | :--- | :--- | :--- |
| Initial Access | T1566.004 | Phishing: Voice (Vishing) | [cite_start]התוקפים התקשרו לצוות התמיכה והתחזו לעובדים כדי להשיג גישה[cite: 21]. |
| Credential Access | T1539 | Steal Web Session Cookie | [cite_start]גניבת אסימוני דלייה מהדפדפן כדי לעקוף צורך בסיסמה או MFA[cite: 21]. |
| Persistence | T1098.005 | Account Manipulation: Device Registration | [cite_start]הקבוצה רשמה את המכשירים הניידים שלהם כגורמי MFA מהימנים עבור חשבונות שנפרצו[cite: 21]. |
| Discovery | T1087.004 | Account Discovery: Cloud Account | [cite_start]סריקת הסביבה כדי למצוא מנהלי מערכת בענן עם הרשאות גבוהות[cite: 21]. |
| Defense Evasion | T1550.001 | Use Alternate Authentication Material | [cite_start]שימוש באסימוני OAuth גנובים כדי לשמור על גישה מבלי לעורר התראות[cite: 21]. |
| Lateral Movement | T1021.001 | Remote Services: RDP | [cite_start]שימוש ב-RDP כדי לנוע בין מכונות וירטואליות בתוך הרשת הפנימית[cite: 21]. |
| Collection | T1530 | Data from Cloud Storage | [cite_start]גישה ואיסוף נתונים רגישים מתוך SharePoint ודליי S3 ב-AWS[cite: 21]. |
| Exfiltration | T1567.002 | Exfiltration to Cloud Storage | [cite_start]שימוש בכלי Rclone להעברת נתונים גנובים לתשתית הענן של התוקף[cite: 21]. |

## [cite_start]4. Advanced Search Queries [cite: 22, 23]
* [cite_start]`site: unit42.paloaltonetworks.com "Muddled Libra" "MITRE ATT&CK"` [cite: 24]
* [cite_start]`tasklist /v site: attack.mitre.org/techniques/T1539` [cite: 25]
* [cite_start]`"MFA Fatigue" site: cloud.google.com/blog/topics/threat-intelligence` [cite: 26]
