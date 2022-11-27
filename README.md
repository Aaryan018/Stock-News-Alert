# Stock-News-Alert

Technologies/Concepts Used: Python, smtplib (Sending Emails), API Endpoints and API Parameters (requests module), Reading through API Documentations from different websites.

1. This Stock Alert program informs a user about the fluctuation in stock value and provides 3 related news articles in respect to that.
2. The user receives an email which highlights the percentage increase/decrease over the past 2 days along with the latest news articles.
3. Following are the websites who's API Endpoints were used for stock and news related information:

Stock: https://www.alphavantage.co
News: https://newsapi.org

Use the following steps to run this project:
Download the zip file and make following changes to the main.py

1. Variable **STOCK**:        Enter the Stock name of the stock you wish to get information about.
2. Variable **COMPANY_NAME**: Enter the name of the company.
3. Variable **FROM_EMAIL**:   Enter Email you want to send the email from.
4. Variable **MY_PASSWORD**:  Enter the app password for that email.
5. Variable **SERVER_NAME**:  Enter the smtp server name of the mail service used to send email from. (For ex, gmail smtp server name is smtp.gmail.com). 
6. Get free **STOCK_API** Key from https://www.alphavantage.co/ (Authentication required)
7. Get free **NEWS_API** Key from https://newsapi.org/ (Authentication required)
