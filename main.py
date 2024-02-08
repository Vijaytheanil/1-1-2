import requests
url="https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url=url)
print(response.json())
data=response.json()
my_dict = {'time': {'updated': 'Feb 8, 2024 09:19:30 UTC', 'updatedISO': '2024-02-08T09:19:30+00:00', 'updateduk': 'Feb 8, 2024 at 09:19 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '44,636.449', 'description': 'United States Dollar', 'rate_float': 44636.4494}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '35,348.72', 'description': 'British Pound Sterling', 'rate_float': 35348.7202}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '41,406.467', 'description': 'Euro', 'rate_float': 41406.4667}}}
print(data['time'])
time={'updated': 'Feb 8, 2024 09:19:30 UTC', 'updatedISO': '2024-02-08T09:19:30+00:00', 'updateduk': 'Feb 8, 2024 at 09:19 GMT'}
print(data['time']['updated'])