import requests

def get_exchange_rate(currency_code):
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Помилка при зверненні до API НБУ")
        return

    data = response.json()
    for item in data:
        if item['cc'] == currency_code:
            print(f"{item['txt']} ({item['cc']}): {item['rate']} грн")
            return

    print("Валюта не знайдена.")

# Приклад використання:
get_exchange_rate("USD")
get_exchange_rate("EUR")
