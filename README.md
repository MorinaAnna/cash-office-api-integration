# Лабораторна робота №6  
## Використання і створення API  
**Студентка:** Моріна Анна  
**Курс:** 2  
**Група:** ІС-33  
**Логін Moodle:** is-33fiot-23-137  

---

## Вправа 6.1 — Сценарій використання зовнішнього API

### Обрана предметна область:
**Облік готівки в касі (гривня)**. У системі передбачається введення касових операцій (прихід та видаток готівки) з можливістю зазначення валюти.

### Обраний зовнішній API:
**Національний банк України — API курсів валют**  
🔗 URL: `https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json`

### Сценарій використання:
При введенні операції з іноземною валютою (наприклад, долар США або євро), система автоматично підтягує актуальний курс з API НБУ, конвертує вказану суму у гривні та зберігає результат у базі даних. Це забезпечує точність та актуальність при відображенні еквіваленту у гривнях.

---

## Вправа 6.2 — Виклик API та візуалізація відповіді

У файлі `main.py` реалізовано підключення до API НБУ, отримання курсу валют (USD, EUR) та вивід результатів у консоль.

### 📎 main.py:
```python
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

get_exchange_rate("USD")
get_exchange_rate("EUR")
