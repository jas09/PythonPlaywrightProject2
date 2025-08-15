# 🔧 QA Automation Pipeline with Jenkins, Playwright, Allure & Jira Integration

## 🚀 Overview
This repository contains a robust QA automation framework built using **Playwright** for end-to-end testing, integrated with **Jenkins** for CI/CD, **Allure** for rich test reporting, and **Jira** for issue tracking and traceability.

## 📂 Project Structure

## 🧪 Technologies Used
- **Playwright** (Node.js or Python)
- **Jenkins** (Declarative Pipeline)
- **Allure Reports**
- **Jira Cloud Integration**
- **GitHub Actions** (optional for webhook triggers)

## ⚙️ Setup Instructions

1. Clone the Repository
git clone https://github.com/jas09/PythonPlaywrightProject2.git

3. Install Dependencies
npm install   # or pip install -r requirements.txt

4. Run Tests Locally
npx playwright test   # or pytest

5. Generate Allure Report
allure generate allure-results --clean -o reports
allure open reports


🧵 CI/CD Pipeline Flow
1. 	Code is pushed to GitHub
2. 	Jenkins pipeline is triggered
3. 	Tests are executed via Playwright
4. 	Allure report is generated and published
5. 	Jira issue is updated with test summary and report link
🧠 Jira Integration
• 	Commits must include Jira issue key (e.g., )
• 	Jenkins auto-comments on Jira issues post-test
• 	Failed tests can auto-create bugs in Jira
📈 Reporting
Allure reports include:
• 	Test status (pass/fail)
• 	Screenshots
• 	Logs
• 	Environment metadata

📬 Contact
For questions or demo requests, reach out to: Azharulla – Senior QA Automation Engineer/Certified Scrum Master
📧 azharulla.mohammed1701@gmail.com
