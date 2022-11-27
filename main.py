import requests
import smtplib

#Follow the steps below to run the code:
#1. Variable STOCK: Enter the Stock name of the stock you wish to get information about.
#2. Variable COMPANY_NAME: Enter the name of the company.
#3. Get free STOCK_API Key from https://www.alphavantage.co/
#4. Get free NEWS_API Key from https://newsapi.org/
#5. Variable FROM_EMAIL: Enter Email you want to send email from.
#6. Variable MY_PASSWORD: Enter the app password for that email.
#7. Variable SERVER_NAME: Enter the server name of the mail service used to send email from.

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_API = "Enter your own api key"
NEWS_API = "Enter your own api key"

FROM_EMAIL = "Enter the email that will send the alert"
TO_EMAIL = "Enter the email that will receive the alert"
MY_PASSWORD = "Enter the app password of the email used in T0_EMAIL"

SERVER_NAME = "smtp.gmail.com"


#this function finds the percentage decrease or increase in the value of the stock.
def stock_info():
    parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": STOCK_API
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    data = response.json()

    date_list = list(data["Time Series (Daily)"])

    close_value0 = float(data["Time Series (Daily)"][date_list[0]]["4. close"])
    close_value1 = float(data["Time Series (Daily)"][date_list[1]]["4. close"])

    percentage = ((close_value0 - close_value1) / close_value1) * 100

    get_news(percentage, date_list[1])


#this function gets 3 latest news regarding the stock highlighting the reasons of its fluctuation.
def get_news(percentage, date):
    parameters = {
        "q": COMPANY_NAME,
        "from": date,
        "apiKey": NEWS_API
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    data_list = response.json()["articles"]


    news1 = (data_list[0]['title'], data_list[0]['url'])
    news2 = (data_list[1]['title'], data_list[1]['url'])
    news3 = (data_list[2]['title'], data_list[2]['url'])


    send_mail(news1, news2, news3, percentage)


#this function sends the email with the stock percentage increase/decrease and the related news articles.
def send_mail(news1, news2, news3, percentage):
    percentage = round(percentage, 2)
    if percentage > 0:
        str = "Increase "
    else:
        str = "Decrease "


    msg_str =f"Subject:Stock News ALert!\n\n{STOCK}: {str}{abs(percentage)}%\n\nTitle: {news1[0]}\nLink: {news1[1]}\n\n" \
         f"Title: {news2[0]}\nLink: {news2[1]}\n\nTitle: {news3[0]}\nLink: {news3[1]}"


    with smtplib.SMTP(SERVER_NAME) as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=msg_str
        )


stock_info()

