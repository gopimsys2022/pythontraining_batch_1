import requests
url = 'https://restcountries.eu/rest/v2/all'  
response = requests.get(url)
print(response) 
print(response.status_code)  
countries = response.json()
print(countries[:1])  